import biplist
import glob, os

directory = '/Applications'
for path,dirs,files in os.walk(directory):
  for subdir in dirs:
    if subdir.endswith('.app'):
      plist_path = os.path.join(path,subdir,'Contents/Info.plist')
      print subdir
      try:
        plist = biplist.readPlist(plist_path)
      except:
        print 'No Version Found'
        continue
      if 'CFBundleShortVersionString' in plist.keys():
        print plist['CFBundleShortVersionString']
      elif 'CFBundleVersion' in plist.keys():
        print plist['CFBundleVersion']
      else:
        print 'No Version Found'
