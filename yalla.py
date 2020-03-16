#!/usr/bin/env python3
import iterm2
import AppKit

backendDir = '~/Workspace/module-catalog-pim'
frontendDir = '~/Workspace/web-catalog-pim'

# Launch the app if needed
bundle = "com.googlecode.iterm2"
if not AppKit.NSRunningApplication.runningApplicationsWithBundleIdentifier_(bundle):
  AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm")

# Gets the current window or creates one if needed
async def get_current_window(app):
  curr_win = app.current_window
  if not curr_win:
    curr_win = await iterm2.Window.async_create(connection)

  await curr_win.async_activate()

  return curr_win

async def main(connection):
  # Get the instance of currently running app
  app = await iterm2.async_get_app(connection, True)
  win = await get_current_window(app)

  # Create two splits here
  left = win.current_tab.current_session
  right = await left.async_split_pane(vertical=True)

  # Set the tab title for this session
  await win.async_set_title("Catalog PIM")

  # Move to the backend dir and run the setup
  await left.async_send_text(f"cd {backendDir}\n")
  await left.async_send_text("yarn dev\n")

  # Start frontend by sending text sequences as if we typed them in the terminal
  await right.async_send_text(f"cd {frontendDir}\n")
  await right.async_send_text("yarn dev\n")

try:
  iterm2.run_until_complete(main, True)
except:
  print("""
Please ensure that iTerm is running and the Python API is
enabled in the iTerm2 configuration. Have a look at this
link: https://github.com/kamranahmedse/yalla#setup
""")
