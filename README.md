# Mac App Version Finder

Quick and dirty python script to scrape application versions

### Running `app_version_finder.py`

This script takes in a filename to which the version numbers are written.  
To run the script, do the following
`cd <THIS_DIRECTORY>`
`python app_version_finder.py <FILENAME>`

> I included the source code for [BiPlist](https://github.com/wooster/biplist) because I needed to use it without installing new libraries

### Running `plist_parser.py`

This script takes in two arguments: input System Information Plist file and the output file for the app versions

`cd <THIS_DIRECTORY>`
`python plist_parser.py <INPUT_PLIST> <OUTPUT_FILE>`
