from PIL import Image

with open('TiMu.txt','rb') as f:
	pixels = f.read().split(',')

leng = len(pixels)-1
print leng

#---------------三个数值一组，构建像素列表
pis = []
for i in range(0,leng,3):
	r = (int(pixels[i]), int(pixels[i+1]), int(pixels[i+2]))
	pis.append(r)

#---------------生成指定长宽的空图片
height = 307
width = 311

assert len(pis)==height*width

pic = Image.new("RGB",(height,width))


#---------------根据像素列表里的值，重新绘制图像
for x in range(0,height):
	for y in range(0,width):
		pic.putpixel([x,y],pis[width*x+y])


#---------------保存文件
filename = 'flag.jpg'
pic.show()
pic.save(filename)