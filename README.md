# Advent of Code '22

## Format
1 folder for each day, within each folder, create a file/folder after your name & add the code there.

`main` isn't protected so you can commit directly, or create branches & open PRs.

`.venv` is configured at a repo level.

## How to set up a Python 3 project
### Install Python
 - Install [pyenv](https://github.com/pyenv/pyenv)
 - `pyenv install 3.XX.XX` where XX is the version (see `pyenv install --list`)
 - `python shell 3.XX.XX` where XX is the version installed

### Create venv
 - `python --version` - confirm it's 3.XX.XX
 - `python -m venv .venv`
 - `source .venv/bin/activate` - `(.venv)` should appear in the terminal before your directory name.
 - `pip install -r requirements.txt`

###  Running a script
 - `python ./path/to/file`
