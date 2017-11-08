# -*- coding:utf-8 -*-

import os 
import time
import multiprocessing


# global variable
process_name='IEXPLORE.EXE'
process_path="C:\Program Files\Internet Explorer\IEXPLORE.EXE"
windbg_path="C:\Program Files\Debugging Tools for Windows (x86)\windbg.exe"
command_list=["bp kernel32!Winexec","bp kernel32!CopyFileA","lm","!heap -h"]


# write commands to command.txt
def write_to_commandScript():
	global command_list
	length = len(command_list)
	with open('command.txt','wb') as fp:
		for i in range(length-1):
			fp.write(command_list[i] + ';')
		fp.write(command_list[i+1])
	fp.close()


# use tasklist to get the process_id
def get_process_id():
	global process_name
	result = os.popen('tasklist|findstr %s'%(process_name))
	res = result.read()
	if len(res)==0:
		print '%s not found...'%(process_name)
		exit(0)
	else:
		pid  = res.split(' ')[16].replace(',','')
		return pid

# make windbg attach to the process. When windbg runs over, delete tmp files automatic
def attach(pid):
	global windbg_path,command_file
	write_to_commandScript()
	command = "\"%s\" -p %s -c \"$$><command.txt\""%(windbg_path,pid)
	with open('execute.bat','wb') as f:
		f.write(command)
	f.close()
	os.system('execute.bat')
	clear_file()

# delete tmp files
def clear_file():
	os.system('del execute.bat')
	os.system('del command.txt')


def run_process():
	global process_path
	os.system('"'+process_path+'"')

if __name__=='__main__':
	# start multiprocessing to start process
	p = multiprocessing.Process(target=run_process,args=())
	p.start()
	time.sleep(5)
	pid = get_process_id()
	print 'attach to process %s'%(pid)
	attach(pid)
	
