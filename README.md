
### 比原版增加了文件夹目录地址

### 支持平台
Windows QQ 音乐最新版（QQMusic2005.22.47.07）

### 支持格式
理论支持所有格式，但仅适配了 mflac 和 mgg 格式。

### 使用方法
1. 开启 QQ 音乐，下载音乐到默认文件夹。
2. 执行python hook_qq_music.py "下载音乐文件夹(mflac目录)"

find_repeat.py 是处理重复文件的
使用方法

```
python find_repeat.py 文件夹A 文件夹B
```
该命令会找出同时存在A和B文件夹下面的文件(后缀名不同也算是相同文件)移动到文件夹A下面的repeat_move目录

执行前目录结构
--A
---B.mflac
---C.mflac

--B
--B.flac

执行命令

```
python find_repeat.py A B
```

处理后目录结构
--A
----repeat_move
------B.mflac
---C.mflac
--B
--B.flac

不会改变B目录结构，会把A目录下出现在B目录的同名文件(忽略后缀名不同)移动到repeat_move目录

如果转换失败了，重新执行就会有重复的被转换，这时候就可以使用find_repeat.py来移动以及转换的重名文件，repeat_move目录就可以自行处理