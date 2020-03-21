# iTomate

<img width="450px" align="right" src="./.github/assets/illustration.png" />

> Automate your iTerm layouts and session setup

Define your iTerm layouts, commands to execute in the form of yaml files and run a single command to have iTerm prepare it self for you to start working.

## Requirements

* iTerm2 Version 3.3 or later
* Python 3.5 or later

## Installation

Make sure that you are running Python 3.5 or later

```shell
pip install itomate
```

[Enable Python API usage](./.github/assets/preferences.png) in iTerm preferences.

```shell
itomate --version
```

## Example
> The layout, number of panes, tabs, titles and commands is configurable and is detailed below.

![](./.github/assets/itomate-demo.gif)

## Usage
Open iTerm and simply run the below command

```shell
itomate -c config.yml
```
If you don't provide `-c` flag, itomate will look for `itomate.yml` file in the current directory and use that.

Here is the list of options available

```shell
itomate [-c,--config <config-file>] # Sets up the iTerm session
        [-h,--help]                 # Shows the help screen
        [-v,--version]              # Shows the installed itomate version
```

## Configuration
Configuration file to set up the sessions has the format below

```yml
version: "1.0"
tabs:
  window-1:
    title: "Window 1"
    panes:
      - title: "Some Pane Title"
        position: "1/1"
        commands:
         - "some command"
         - "second command"
      - position: "1/2"
      - position: "2/1"
      - position: "2/2"
  window-2:
    title: "Window 2"
    panes:
      - position: "1/1"
      - position: "1/2"
      - position: "2/1"
```

Details for each of the configuration objects above is given below

| Key        | Description                                                                                                                                                                                                                                      |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `version`  | Refers to the itomate configuration version. Should always be 1.                                                                                                                                                                                 |
| `tabs`     | Windows or tabs in the iTerm window.                                                                                                                                                                                                             |
| `window-1` | Replace with the unique project id e.g. `web-catalog-pim`                                                                                                                                                                                        |
| `title`    | Title to be shown in the title bar of the current tab                                                                                                                                                                                            |
| `position` | Position of the pane in the window. It has the format of `number1/number2` where `number1` refers to the column and `number2` refers to the row in the column. More on this later in the readme. `position` is the only required key in a pane |
| `commands` | List of commands to execute.                                                                                                                                                                                                                     |



## Layouts
The parameter `position` in each pane is required and allows you to configure how the layout looks like. The position value has the format below:

```shell
x / y – both x and y are required parameters

x: refers to the column in the window
y: refers to the row of the given column x
```

Here are some of the examples for different pane layouts

## Single Pane Window

```
.------------------.
| 1/1              |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
'------------------'
```

```yml
version: "1.0"
tabs:
  some-project:
    title: "Some Project"
    panes:
      - title: "Single Pane"
        position: "1/1"
        commands:
          - "cd ~/Workspace/some-project"
          - "git pull origin master"
          - "yarn dev"
```

## Two Panes Vertical Split Layout

```
.------------------.------------------.
| 1/1              | 2/1              |
|                  |                  |
|                  |                  |
|                  |                  |
|                  |                  |
|                  |                  |
|                  |                  |
|                  |                  |
|                  |                  |
'------------------'------------------'
```

```yml
version: "1.0"
tabs:
  some-project:
    title: "Some Project"
    panes:
      - title: "First Half"
        position: "1/1"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/some-project"
      - title: "Second Half"
        position: "2/1"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/another-project"
```
