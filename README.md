## Video-Cleaner Cli
This majorly a video duplicate remover application that helps to personally remove duplicate video files on unix-based or linux machine . But can provide some regular expression pattern to further enhance it capabilites.

## Contributors
- Caleb Adewole

### Usage
To use this application , first run `python setup.py install` or create a virtual enviroment.
```bash
python main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  clean
  create  Creates a folder path using the specified destination path and...
  delete  delete the provide folder path :params folder_path - folder to...
  filter  filter files based on provided regex expression :params...
  list    :params `folder_name` - path to list out
```
To view sub-commands use the  example below 
```bash
python main.py clean --help
Usage: main.py clean [OPTIONS]

Options:
  -f, --folder-path TEXT  the video folder path to clean up  [required]
  -o, --out TEXT          the output folder path to store duplicates
                          [required]
  -r, --regex TEXT        filter pattern for movies
  -d, --delete-output     delete the copies
  --help                  Show this message and exit.
```