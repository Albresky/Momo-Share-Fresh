# Momo-Share-Fresh
**墨墨背单词**分享链接刷新点击量（IP代理池方式）

## 运行方式

### 1 `Python` 环境运行main.py

#### 1.1 克隆本仓库

```
git clone https://github.com/Albresky/Momo-Share-Fresh.git
```

#### 1.2 安装模块

```
cd src && pip install -r requirements.txt
```

#### 1.3 运行`main.py`

```
python main.py
```

### 2 运行可执行文件（`无需Python环境`）

#### 2.1 进入[Release](https://github.com/Albresky/Momo-Share-Fresh/releases)下载对应版本

#### 2.2 `Windows` 平台

```
.\momo_windows_amd64.exe
```

#### 2.3 `Linux` 平台

```
./momo_linux_x86_64
```

### 3 参数说明

- 以Windows平台（`momo_windows_amd64.exe`）为例，运行exe时添加选项 `-h` 以查看说明
```
.\momo_windows_amd64.exe -h
```

- 输出如下
```
PS C:\Users\Albre\Desktop\sd> .\momo_windows_amd64.exe -h
usage: momo_windows_amd64.exe [-h] --url URL [URL ...] [--num [NUM]] [--delay [DELAY]]

Momo Share Flash

optional arguments:
  -h, --help            show this help message and exit
  --url URL [URL ...], -url URL [URL ...]
                        墨墨背单词分享链接
  --num [NUM]           点击量
  --delay [DELAY]       刷新延时(ms)
```

- `--url或-url` 为 **必选选项**，用于输入分享链接
  - 例如：`.\momo_windows_amd64.exe -url "https://xxxxxxxxx"`，或多个分享链接：`.\momo_windows_amd64.exe -url "https://aaaa" "https://bbbb"`   
- `-num`和`-delay`为 **可选选项**，用于指定刷新次数（默认30次）、每次刷新的延时（默认5，单位：ms）
  - 例如：`.\momo_windows_amd64.exe -url "https://xxxxxxxxx" -num 25`，或 `.\momo_windows_amd64.exe -url "https://aaaa" "https://bbbb" -num 25 -delay 3` 
  - `-delay` 延时请不要设置太低，或许会被ban
- 如果在Python环境运行 `main.py`，方法同上。将 `momo_windows_amd64.exe` 替换为 `python main.py` 即可