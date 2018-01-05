import os
import sys

def rename(self_name,prefix,begin_offset,suffix):
	#print self_name
	path= os.getcwd()
	num = int(begin_offset)
	filelist = os.listdir(path)
	for file in filelist:
		# prevent from modifing the name of program self
		if file in self_name:
			continue
		Olddir = os.path.join(path,file)
		# judge whether it is a folder
		if os.path.isdir(Olddir):
			continue
		filename = prefix + '_' + str(num)+ '.' + suffix
		Newdir = os.path.join(path,filename)
		os.renames(Olddir,Newdir)
		num = num + 1



if __name__ == '__main__':
    if len(sys.argv) == 3:
        print 'please input a the filename\'s prefix & begin_offset & suffix!'
        print 'For example:rename.py image 0 png,then get image_0.png,image_1.png......'
        exit()
    else:
    	self_name = sys.argv[0]
        filename_prefix = sys.argv[1]
        begin_offset = sys.argv[2]
        suffix = sys.argv[3]
    rename(self_name,filename_prefix,begin_offset,suffix)