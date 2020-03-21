<img width="450px" align="right" src="https://i.imgur.com/xHH6Ffr.png" />

# iTomate
> Automate your iTerm layouts and session setup

Define your iTerm layouts, commands to execute and sessions in the form of yaml files and run a single command to have iTerm prepare it self for you to start working.

## Requirements

* iTerm2 Version 3.3 or later
* Python 3.5 or later

## Installation

Make sure that you are running Python 3.5 or later

```shell
pip install itomate
```

Enable iTerm's Python API in the preferences

* Press <kbd>CMD</kbd> + <kbd>,</kbd> to open iTerm preferences
* Search for "Python API" in the top right search input
* Enable the checkbox for [Enable Python API](https://i.imgur.com/RVLW6eD.png)

Now run below to make sure that everything is setup properly

```shell
itomate --version
```
