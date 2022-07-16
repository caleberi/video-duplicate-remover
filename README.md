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
(venv) ➜  video-cleaner git:(main) ✗ video-cleaner-cli clean --help
Usage: video-cleaner-cli clean [OPTIONS]

  Remove all video files from a folder

  :params `folder_path` - path to clean :params `out` - output folder path
  :params `regex` - regular expression pattern :params  `delete_output` - flag
  to delete the output folder

Options:
  -f, --folder-path TEXT  the video folder path to clean up  [required]
  -o, --out TEXT          the output folder path to store duplicates
                          [required]
  -r, --regex TEXT        filter pattern for movies
  -d, --delete-output     delete the copies
  --help                  Show this message and exit.
```