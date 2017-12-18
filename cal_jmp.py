#!/usr/bin/python


def print_v(string):
	assert len(string)==10
	result = ''
	for i in range(5):
		result += string[i*2]+string[i*2+1]+' '
	print result	

def cal_jmp():
	# start_addr = '0x804862e'
	# dst_addr = '0x8048460'
	start_addr = raw_input('begin instr addr:')
	dst_addr = raw_input('dst instr addr:')
	offset = int(dst_addr,16) - int(start_addr,16)
	if offset>0:   #0x56a
		return 'E8'+hex(offset)[2:][::-1].ljust(8,'0')
	else:
		return 'E8'+hex(0xffffffff + offset + 1)[2:][::-1]
		
if __name__=='__main__':
		print_v(cal_jmp())