#!/usr/bin/env python3

import argparse
import os
import textwrap

import iterm2
import yaml

default_config = 'itomate.yml'
version = '0.2.14'


class ItomateException(Exception):
    """Raise for our custom exceptions"""


# Gets the current window or creates one if needed
async def get_current_window(app, connection):
    curr_win = app.current_window
    if not curr_win:
        curr_win = await iterm2.Window.async_create(connection)

    await curr_win.async_activate()

    return curr_win


def read_config(config_path):
    if not os.path.isfile(config_path):
        raise ItomateException(f"Config file does not exist at {config_path}")

    with open(r'%s' % config_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        return yaml.load(file, Loader=yaml.FullLoader)


async def render_tab_panes(tab, panes):
    # Create a dictionary with keys set to positions of panes
    positional_panes = {pane.get("position"): pane for pane in panes}

    sessions_ref = {}
    current_session = tab.current_session

    # Render the top level/vertically positioned panes i.e. 1/1, 2/1, 3/1, 4/1, 5/1
    for vertical_pane_counter in list(range(1, 10)):
        current_position = f"{vertical_pane_counter}/1"
        pane = positional_panes.get(current_position)
        if pane is None:
            continue

        # For the first counter, we don't need to split because
        # we have the currently opened empty session already
        if vertical_pane_counter != 1:
            current_session = await current_session.async_split_pane(vertical=True)

        # Cache the pane reference for further divisions later on
        sessions_ref[current_position] = current_session

        # Execute the commands for this pane
        pane_commands = pane.get('commands') or []
        for command in pane_commands:
            await current_session.async_send_text(f"{command}\n")

    # For each of the vertical panes rendered above, render the sub panes now
    # e.g. 1/2, 1/3, 1/4, 1/5 ... 2/2, 2/3, 2/4, ... and so on
    for vertical_pane_counter in list(range(1, 10)):
        # Reference to 1/1, 2/1, 3/1 and so on. We are going to split that horizontally now
        parent_session_ref = sessions_ref.get(f"{vertical_pane_counter}/1")
        # Ignore if we don't have the session for this root position
        if parent_session_ref is None:
            continue

        current_session = parent_session_ref

        # Horizontal divisions start from 2 e.g. 1/2, 1/3, 1/4, 1/5 .. 2/2, 2/3 and so on
        for horizontal_pane_counter in list(range(2, 11)):
            horizontal_position = f"{vertical_pane_counter}/{horizontal_pane_counter}"
            horizontal_pane = positional_panes.get(horizontal_position)
            if horizontal_pane is None:
                continue

            # split the current session horizontally
            current_session = await current_session.async_split_pane(vertical=False)
            # Cache the pane reference for later use
            sessions_ref[horizontal_position] = current_session

            # Execute the commands for this pane
            pane_commands = horizontal_pane.get('commands') or []
            for command in pane_commands:
                await current_session.async_send_text(f"{command}\n")

    return sessions_ref


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Workflow automation and layouts for iTerm',
        epilog=textwrap.dedent("""\
        For details on creating configuration files, please head to:

        https://github.com/kamranahmedse/itomate
        """),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument('-c', '--config', help='Path to the configuration file')
    parser.add_argument('-v', '--version', help='Show version', action='store_true')

    return vars(parser.parse_args())


async def activate(connection):
    args = parse_arguments()
    if args.get('version'):
        print(version)
        return

    config_path = args.get('config') if args.get('config') is not None else default_config
    config = read_config(config_path)

    # Get the instance of currently running app
    app = await iterm2.async_get_app(connection, True)
    initial_win = await get_current_window(app, connection)
    curr_tab = initial_win.current_tab

    # Render all the required tabs and execute the commands
    for counter, tab_id in enumerate(config['tabs']):
        # Don't create a new tab for the first iteration because
        # we have the current tab where the command was run
        if counter != 0:
            curr_tab = await initial_win.async_create_tab()

        tab_config = config['tabs'][tab_id]
        tab_title = tab_config.get('title')
        tab_panes = tab_config.get('panes')

        # Ignore if there are no tab panes given
        if len(tab_panes) <= 0:
            continue

        await curr_tab.async_set_title(tab_title)
        await render_tab_panes(curr_tab, tab_panes)


def main():
    iterm2.run_until_complete(activate)


if __name__ == "__main__":
    main()
