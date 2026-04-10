# chown - 修改文件所有者

## 一句话理解

chown（change owner）修改文件或目录的所有者和所属组。

```bash
# 修改文件所有者
sudo chown user file.txt

# 同时修改所有者和组
sudo chown user:group file.txt
```

## 常用场景

### 1. 修改文件所有者

```bash
# 只修改所有者
sudo chown fajknli file.txt

# 只修改所属组
sudo chown :fajknli file.txt

# 同时修改所有者和组
sudo chown fajknli:users file.txt

# 使用点号分隔（同上）
sudo chown fajknli.users file.txt
```

### 2. 递归修改目录

```bash
# 递归修改目录及内部所有文件
sudo chown -R fajknli:users myfolder/

# 只修改目录本身（不递归）
sudo chown fajknli myfolder/
```

### 3. 参考其他文件

```bash
# 复制参考文件的所有者/组
sudo chown --reference=template.txt target.txt
```

### 4. 修改符号链接

```bash
# 修改链接本身（默认）
sudo chown -h user symlink

# 修改链接指向的文件
sudo chown user symlink
```

### 5. 批量修改

```bash
# 修改当前目录下所有文件
sudo chown user:group *

# 修改特定类型文件
sudo chown user:group *.txt

# 使用 find 批量修改
sudo find /path -type f -user olduser -exec chown newuser {} \;
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-R` | 递归修改 | `sudo chown -R user:group dir/` |
| `-h` | 修改符号链接本身 | `sudo chown -h user symlink` |
| `-v` | 显示详细信息 | `sudo chown -v user file` |
| `-c` | 只在修改时显示 | `sudo chown -c user file` |
| `-f` | 静默模式（不报错） | `sudo chown -f user file` |
| `--reference` | 参考其他文件 | `sudo chown --reference=ref target` |
| `-L` | 跟随符号链接 | `sudo chown -L user link` |
| `-P` | 不跟随符号链接（默认） | `sudo chown -P user link` |

## 格式说明

| 格式 | 说明 | 例子 |
|------|------|------|
| `user` | 只改所有者 | `chown fajknli file` |
| `:group` | 只改组 | `chown :users file` |
| `user:` | 改所有者，组清空 | `chown fajknli: file` |
| `user:group` | 改所有者和组 | `chown fajknli:users file` |
| `user.group` | 同上（不推荐） | `chown fajknli.users file` |

## 常见问题

### 1. chown 和 chgrp 有什么区别？

| 命令 | 功能 |
|------|------|
| `chown` | 修改所有者和组 |
| `chgrp` | 只修改组 |

```bash
# 等价
sudo chown :group file
sudo chgrp group file
```

### 2. 为什么需要 sudo？

普通用户不能修改其他用户拥有的文件。只有 root 可以修改所有者。

```bash
# 需要 sudo
sudo chown root file

# 普通用户只能修改自己文件的组（需属于该组）
chown :mygroup file
```

### 3. 如何修复家目录权限？

```bash
# 修改所有者
sudo chown -R fajknli:fajknli /home/fajknli/

# 修改目录权限
chmod 755 /home/fajknli/
chmod 700 /home/fajknli/.ssh
```

### 4. 如何批量修改所有者为当前用户？

```bash
# 当前目录下所有文件
sudo chown -R $USER:$USER .

# 特定目录
sudo chown -R $USER:$USER /path/to/dir/
```

## 快捷别名

```bash
alias chownr='sudo chown -R'
alias chownv='sudo chown -v'
alias chownow='sudo chown -R $USER:$USER'
```

## 一句话总结

chown 核心：`sudo chown user file` 改所有者，`sudo chown :group file` 改组，`sudo chown user:group file` 同时改，`-R` 递归。普通用户只能改自己文件的组。修复权限用 `sudo chown -R $USER:$USER .`。
