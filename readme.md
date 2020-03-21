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
| `commands` | List of commands to execute in the current pane.                                                                                                                                                                                                                     |



## Layouts
The parameter `position` in each pane decides where each of the window panes will be displayed. The position value has the format below

```shell
x / y – both x and y are required parameters

x: refers to the column in the window
y: refers to the row of the given column x
```

Here are some of the examples for different pane layouts

## Single Pane Window

For single pane, since there is one column and one row, the position for pane would be `1/1`
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
Here is how the configuration would look like
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
For two panes with equal split or in other words two columns with one row in each, the positions would be `1/1` for the pane on the left and `2/1` for the pane on the right i.e. the second column.
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
Here is how it would look in the configuration
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
## Two Columns, Three Panes Layout

The layout below now has two columns. First column has only one row so position for that would be `1/1`. For the second column we have two panes i.e. two rows; first pane in the second column would be `2/1` and the second one would be `2/2`.

```
.------------------.------------------.
| 1/1              | 2/1              |
|                  |                  |
|                  |                  |
|                  |                  |
|                  |------------------|
|                  | 2/2              |
|                  |                  |
|                  |                  |
|                  |                  |
'------------------'------------------'
```

Configuration for that would be:

```yml
version: "1.0"
tabs:
  some-project:
    title: "Some Project"
    panes:
      - position: "1/1"    # <-- Notice the position
      - position: "2/1"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/dev-server"
          - "./run"
      - position: "2/2"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/project"
          - "git standup"
```
Note that the `commands` and `title` are optional parameters in panes. Only `position` is required.

## Two Columns, Four Panes Layout

```
.------------------.------------------.
| 1/1              | 2/1              |
|                  |                  |
|                  |                  |
|                  |                  |
|------------------|                  |
| 1/2              |                  |
|                  |                  |
|                  |                  |
|------------------|                  |
| 1/3              |                  |
|                  |                  |
|                  |                  |
'------------------'------------------'
```
Configuration for that would be:
```yml
version: "1.0"
tabs:
  some-project:
    title: "Some Project"
    panes:
      - position: "1/1"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/project"
          - "Make clean"
      - position: "1/2"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/project"
          - "git standup"
      - position: "1/3"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/project"
          - "git standup"
      - position: "2/1"    # <-- Notice the position
        commands:
          - "cd ~/Workspace/dev-server"
          - "./run"
```

## Three Columns Five Pane Layout

```
.------------------.------------------.------------------.
| 1/1              | 2/1              | 3/1              |
|                  |                  |                  |
|                  |                  |                  |
|                  |                  |                  |
|                  |------------------|                  |
|                  | 2/2              |                  |
|                  |                  |                  |
|                  |                  |                  |
|                  |------------------|                  |
|                  | 2/3              |                  |
|                  |                  |                  |
|                  |                  |                  |
'------------------'------------------'------------------'
```
Configuration for that would be

```yml
version: "1.0"
tabs:
  some-project:
    title: "Some Project"
    panes:
      - position: "1/1"    # <-- Notice the position
      - position: "2/1"    # <-- Notice the position
      - position: "2/2"    # <-- Notice the position
      - position: "2/3"    # <-- Notice the position
      - position: "3/1"    # <-- Notice the position
```

## Similar Projects

There is [itermocil](https://github.com/TomAnthony/itermocil/blob/master/README.md) which relies on [Applescript that has been deprecated by iTerm](https://www.iterm2.com/documentation-scripting.html), has limited layout options, and is pretty limited in terms of what it can achieve because of AppleScript. iTomate uses the iTerm's [newly introduced Python API](https://www.iterm2.com/python-api/), has flexible layouts support and can be extended using iTerm's pretty powerful API.

## Contributions
Feel free to submit pull requests, create issues, spread the word.

## License 

MIT &copy; [Kamran Ahmed](https://twitter.com/kamranahmedse)
