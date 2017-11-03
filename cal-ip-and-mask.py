ip = raw_input('ip_addr = ')
mask = raw_input('mask = ')

ip_array = ip.split('.')
mask_array = mask.split('.')

print ip_array
print mask_array

res = []
for i in range(len(ip_array)):
	res.append(int(ip_array[i]) & int(mask_array[i]))

print 'res = ',
for item in res:
	print str(item)+'.',
