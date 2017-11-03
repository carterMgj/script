#!encoding=utf-8
'''
该脚本功能：给定一个根目录，计算其下所有py文件的有效代码行数。
统计时可识别注释代码种类（#，\'\'\'）
'''

import os  
import string  

# 基本配置
log = 0
rootdir = "D://test/"  


# 自定义函数
def sum_list(a_list,b_list):
    res=[]
    for i in range(len(a_list)):
        res.append(a_list[i]+b_list[i])
    return res

def print_list(a_list):
    if len(a_list)==4:
        print("countBlank:%d" % a_list[0])  
        print("countPound:%d" % a_list[1])  
        print("countCode:%d" % a_list[2])
        print("total:%d" % a_list[3])  

def startwith(aline,char):    # startwith(line,'#')  判断line是不是以#开头
    count = aline.find(char)
    if count==0:
        return True
    elif count>0:
        for i in range(count):
            if aline[i]==' ' or aline[i]=='\t':
                continue
            else:
                return False        
        return True
    else:
        return False

def startPound(aline):
    if startwith(aline,'\''):
        count = aline.find('\'')
        if aline[count+1]=='\'' and aline[count+2]=='\'':
            return True
    else:
        return False
        
def endPound(aline):
    aline.strip()
    if aline[-3:]=='\'\'\'':
        return True
    else:
        return False

def py_count(file):  
    total = 0 #总行数  
    countPound = 0 #注释行数  
    countBlank = 0 #空行数  
    countCode = 0   #有效代码行数
    multiPoundFlag = 0 # 1表示当前行正在多行注释中
    line = open(file,'r') #打开文件，因为注释有中文所以使用utf-8编码打开  
    for li in line.readlines(): #readlines()一次性读完整个文件  
        total += 1  
        #判断是否在多行注释中
        if startPound(li):  #判断是否以 ''' 开头
            countPound += 1
            if not endPound(li):  #判断是否以 ''' 结束
                multiPoundFlag=1
                continue
        if multiPoundFlag:
            countPound += 1
            if endPound(li):
                multiPoundFlag=0
            continue

        #判断是否为空行
        if not li.split():   
            countBlank +=1  
        li.strip() 

        #判断是否为单行注释
        if startwith(li,'#'):  
            countPound += 1  
    countCode = total-countBlank-countPound
    if log:
        print(file)  
        print("countBlank:%d" % countBlank)  
        print("countPound:%d" % countPound)  
        print("countCode:%d" % countCode)
        print("total:%d" % total)  
    return [countBlank,countPound,countCode,total]


if __name__=='__main__':
    res = [0,0,0,0]   #[空格行数，注释行数，有效代码行数，总代码行数]
    g = os.walk(rootdir)  
  
    for path,d,filelist in g:   
        for filename in filelist:  
            AbsPath = os.path.join(path, filename)
            if AbsPath[-3:]=='.py':  #只统计py文件的行数
                res = sum_list(res,py_count(AbsPath))

    print_list(res)

  