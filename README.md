### 一个脚本仓库，收集平时比赛工作中自己写的一些小脚本
### draw-imagePixel.py
使用python，指定像素值列表，画出图像
### divide-files
将文件夹中文件按照n个一组，重新生成新的文件夹。有两个版本，python & exe

usage:
```python
python divide-files.py 10
divide-files.exe 10
```

### rename_folder.py
将同一目录下的所有文件夹，按照同一格式命名并编号

usage:
```python
python rename_folder.py movie 0
rename.exe movie 0
```
表示将该目录下的文件夹，从'movie_0'依次递增命令

### rename_file.py
将同一目录下所有文件，按照同一格式命名并编号


usage:
```python
python rename_file image 0 png
```
表示将该目录下所有文件，命名为 imgas_0.png,image_1.png...


### cal_ip_and_mask.py
输入ip地址和子网掩码，计算其相与后的值

### count_python_code.py
统计指定目录下，python文件中代码行数（空格、注释、有效代码）。运行结果格式如下：

```python
countBlank:18
countPound:99
countCode:90
total:207
```
### windbg_attach.py
一键windbg调试利器。使用前，需要在脚本中指定：
 - windbg路径
 - 调试程序路径
 - 调试程序进程名称
 - 需要自动执行的windbg命令
 
即可自动化启动待调试程序 -- windbg附加 -- 执行指定的windbg指令（如下断点、查看内存等）

### cal_jmp.py
计算jmp跳转的指令偏移，输出完整的5字节jmp指令
 - 输入jmp指令下一条指令地址作为起始地址
 - 输入跳转目标地址
 - 得到jmp完整指令
