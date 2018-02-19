import biplist
import glob, os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('output', help='Filename for output')
args = parser.parse_args()
output = open(args.output, 'w')
directory = '/Applications'
for path,dirs,files in os.walk(directory):
  for subdir in dirs:
    if subdir.endswith('.app'):
      plist_path = os.path.join(path,subdir,'Contents/Info.plist')
      output.write(subdir)
      output.write('\n')
      try:
        plist = biplist.readPlist(plist_path)
      except:
        output.write('No Version Found\n')
        continue
      if 'CFBundleShortVersionString' in plist.keys():
        output.write(plist['CFBundleShortVersionString'])
      elif 'CFBundleVersion' in plist.keys():
        output.write(plist['CFBundleVersion'])
      else:
        output.write('No Version Found')
      output.write('\n')

output.close()