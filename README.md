## Video-Duplicate-Remover Cli
This majorly a video duplicate remover application that helps to personally remove duplicate video files on unix-based or linux machine . But can provide some regular expression pattern to further enhance it capabilites.

## Contributors
- Caleb Adewole

### Usage
To use this application , first create a virtual enviroment and then run `pip install .`.
```bash
➜  video-cleaner git:(main) ✗ . venv/bin/activate
(venv) ➜  video-cleaner git:(main) ✗ video-cleaner-cli 
Usage: video-cleaner-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  clean   Remove all video files from a folder :params `folder_path` -...
  create  Creates a folder path using the specified destination path and...
  delete  Delete the provide folder path
  filter  Filter files based on provided regex expression and print it
  list    List out all filepath that is in the folder :params...
```
To view sub-commands use the  example below 
```bash
(venv) ➜  video-cleaner git:(main) ✗ video-cleaner-cli list -f ./command
 📁command
   ├── 📁utils
      ├── 📁__pycache__
      ├──🗒️ __init__.cpython-39.pyc
      └──🗒️ helpers.cpython-39.pyc
   ├──🗒️ __init__.py
   └──🗒️ helpers.py
   ├── 📁__pycache__
   ├──🗒️ __init__.cpython-39.pyc
   ├──🗒️ clean.cpython-39.pyc
   ├──🗒️ create.cpython-39.pyc
   ├──🗒️ filter.cpython-39.pyc
   ├──🗒️ list.cpython-39.pyc
   ├──🗒️ main.cpython-39.pyc
   └──🗒️ delete.cpython-39.pyc
├──🗒️ delete.py
├──🗒️ clean.py
├──🗒️ list.py
├──🗒️ create.py
├──🗒️ __init__.py
├──🗒️ filter.py
└──🗒️ main.py
> DONE .
```