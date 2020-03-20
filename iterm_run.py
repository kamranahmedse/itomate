#!/usr/bin/env python3

import iterm2
import yaml

backend_dir = '~/Workspace/module-catalog-pim'
frontend_dir = '~/Workspace/web-catalog-pim'
config_path = './setup.yml'


# Gets the current window or creates one if needed
async def get_current_window(app, connection):
    curr_win = app.current_window
    if not curr_win:
        curr_win = await iterm2.Window.async_create(connection)

    await curr_win.async_activate()

    return curr_win


def read_config():
    with open(r'%s' % config_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        return yaml.load(file, Loader=yaml.FullLoader)


async def render_tab_panes(tab, panes):
    commands = panes[0].get("commands") or []
    for command in commands:
        await tab.current_session.async_send_text(f"{command}\n")


async def main(connection):
    config = read_config()

    # Get the instance of currently running app
    app = await iterm2.async_get_app(connection, True)
    initial_win = await get_current_window(app, connection)
    curr_tab = initial_win.current_tab

    for counter, tab_id in enumerate(config['tabs']):
        # Don't create a new tab for the first iteration because
        # we have the current tab where the command was run
        if counter != 0:
            curr_tab = await initial_win.async_create_tab()

        tab_config = config['tabs'][tab_id]
        tab_title = tab_config['title']
        tab_panes = tab_config['panes']

        # Ignore if there are no tab panes given
        if len(tab_panes) <= 0:
            continue

        await curr_tab.async_set_title(tab_title)
        await render_tab_panes(curr_tab, tab_panes)

    return

    # Create two splits here
    left = initial_win.current_tab.current_session
    right = await left.async_split_pane(vertical=True)

    return

    # Set the tab title for this session
    await initial_win.async_set_title("Catalog PIM")

    # Move to the backend dir and run the setup
    await left.async_send_text(f"cd {backend_dir}\n")
    await left.async_send_text("yarn dev\n")

    # Start frontend by sending text sequences as if we typed them in the terminal
    await right.async_send_text(f"cd {frontend_dir}\n")
    await right.async_send_text("yarn dev\n")

    ########################################################################
    # Create tab for frontend; I have 1 tab for each service to run vim in
    ########################################################################
    frontend = await initial_win.async_create_tab()

    # Selects the newly created tab
    await frontend.async_select()
    await frontend.current_session.async_send_text(f"cd {frontend_dir}\n")
    await frontend.current_session.async_send_text("git status\n")


try:
    iterm2.run_until_complete(main, True)
except:
    print("""
Please ensure that iTerm is running and the Python API is
enabled in the iTerm2 configuration. Have a look at this
link: https://github.com/kamranahmedse/iterm-run#setup
""")
