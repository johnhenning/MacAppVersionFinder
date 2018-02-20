import plistlib
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input', help='input plist file')
parser.add_argument('output', help='Filename for output')
args = parser.parse_args()

input_filename = args.input
output = open(args.output, 'w')

plist = plistlib.readPlist(input_filename)
apps = plist[2]['_items']
third_party_apps = list()

for app in apps:
    if app['obtained_from'] != 'apple':
        if 'version' in app.keys():
            output.write(app['_name'] + ' ' + app['version'] + '\n')
        else:
            output.write(app['_name'] + ' No Version Found\n')
output.close()