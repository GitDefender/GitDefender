from os import walk

mypath = '/home/tuuna/gitdefender/rules/'

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

f.remove('file')
print f
