import os
import sys

def rename(prefix,begin_offset):
	path= os.getcwd()
	num = int(begin_offset)
	filelist = os.listdir(path)
	for file in filelist:
		Olddir = os.path.join(path,file)
		if not os.path.isdir(Olddir):
			continue
		filename = prefix + '_' + str(num)
		Newdir = os.path.join(path,filename)
		os.renames(Olddir,Newdir)
		num = num + 1



if __name__ == '__main__':
    if len(sys.argv) == 2:
        print 'please input a the filename\'s prefix and begin_offset!'
        print 'For example:rename.exe movie 0'
        exit()
    else:
        filename_prefix = sys.argv[1]
        begin_offset = sys.argv[2]
    rename(filename_prefix,begin_offset)
