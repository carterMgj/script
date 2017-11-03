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

###rename
将同一目录下的所有文件夹，按照同一格式命名并编号
**usage:**

```python
python rename.py movie 0
rename.exe movie 0
```
表示将该目录下的文件夹，从'movie_0'依次递增命令

###cal_ip_and_mask.py
输入ip地址和子网掩码，计算其相与后的值

###count_python_code.py
统计指定目录下，python文件中代码行数（空格、注释、有效代码）。运行结果格式如下：

```python
countBlank:18
countPound:99
countCode:90
total:207
```
