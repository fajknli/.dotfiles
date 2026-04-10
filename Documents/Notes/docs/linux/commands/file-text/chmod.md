# chmod - 修改文件权限

## 一句话理解

chmod（change mode）修改文件或目录的读、写、执行权限。

```bash
# 给文件添加执行权限
chmod +x script.sh

# 设置文件权限为 755
chmod 755 script.sh
```

## 常用场景

### 1. 符号方式修改权限

```bash
# 添加执行权限
chmod +x file.sh

# 移除写权限
chmod -w file.txt

# 设置所有用户可读
chmod a+r file.txt

# 用户（owner）添加执行权限
chmod u+x file.sh

# 组添加写权限
chmod g+w file.txt

# 其他用户移除读权限
chmod o-r file.txt
```

### 2. 数字方式修改权限

```bash
# 755：rwxr-xr-x
chmod 755 script.sh

# 644：rw-r--r--
chmod 644 file.txt

# 600：rw-------
chmod 600 private.key

# 700：rwx------
chmod 700 .ssh

# 777：rwxrwxrwx（危险）
chmod 777 temp.sh
```

### 3. 递归修改目录权限

```bash
# 递归修改目录及内部文件
chmod -R 755 myfolder/

# 只修改目录权限（不修改文件）
find . -type d -exec chmod 755 {} \;

# 只修改文件权限
find . -type f -exec chmod 644 {} \;
```

### 4. 参考其他文件权限

```bash
# 复制参考文件的权限
chmod --reference=template.txt target.txt
```

### 5. 特殊权限位

```bash
# SUID（以文件所有者身份运行）
chmod u+s /usr/bin/passwd

# SGID（以目录所属组创建文件）
chmod g+s shared_dir/

# Sticky Bit（只有文件所有者可删除）
chmod +t /tmp
```

## 权限说明

### 数字权限表

| 数字 | 权限 | 说明 |
|------|------|------|
| 0 | --- | 无权限 |
| 1 | --x | 执行 |
| 2 | -w- | 写入 |
| 3 | -wx | 写入+执行 |
| 4 | r-- | 读取 |
| 5 | r-x | 读取+执行 |
| 6 | rw- | 读取+写入 |
| 7 | rwx | 全部权限 |

### 权限位组成

```
755 = 7 5 5
       │ │ └── 其他用户（other）
       │ └──── 组（group）
       └────── 所有者（user）

7 = 4+2+1 = rwx
5 = 4+0+1 = r-x
```

### 符号权限

| 符号 | 说明 |
|------|------|
| `u` | 所有者（user） |
| `g` | 组（group） |
| `o` | 其他用户（others） |
| `a` | 所有用户（all） |
| `+` | 添加权限 |
| `-` | 移除权限 |
| `=` | 设置权限 |

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-R` | 递归修改 | `chmod -R 755 dir/` |
| `-v` | 显示详细信息 | `chmod -v 755 file` |
| `-c` | 只在修改时显示 | `chmod -c 755 file` |
| `-f` | 静默模式（不报错） | `chmod -f 755 file` |
| `--reference` | 参考其他文件 | `chmod --reference=ref target` |

## 常见问题

### 1. 常见权限组合

| 权限 | 命令 | 适用场景 |
|------|------|----------|
| `-rw-------` | `chmod 600` | 私钥、密码文件 |
| `-rw-r--r--` | `chmod 644` | 普通文件 |
| `-rwx------` | `chmod 700` | 私有脚本 |
| `-rwxr-xr-x` | `chmod 755` | 可执行文件 |
| `drwx------` | `chmod 700` | 私密目录 |
| `drwxr-xr-x` | `chmod 755` | 普通目录 |
| `drwxrwxr-x` | `chmod 775` | 共享目录 |

### 2. 为什么脚本执行权限不够？

```bash
# 添加执行权限
chmod +x script.sh

# 检查权限
ls -l script.sh
# -rwxr-xr-x script.sh
```

### 3. 如何批量修改文件权限？

```bash
# 所有文件 644，目录 755
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;

# 使用 xargs 更快
find . -type f -print0 | xargs -0 chmod 644
find . -type d -print0 | xargs -0 chmod 755
```

### 4. 如何让目录内新文件继承组权限？

```bash
# 设置 SGID
chmod g+s shared_dir/

# 新文件会继承目录的组
```

## 快捷别名

```bash
alias chmodx='chmod +x'
alias chmodr='chmod -R'
alias chmod755='chmod 755'
alias chmod644='chmod 644'
```

## 一句话总结

chmod 核心：`chmod +x file` 加执行权限，`chmod 755 file` 设置 rwxr-xr-x，`chmod 600 key` 私钥权限，`chmod -R 755 dir/` 递归修改。数字权限：4读2写1执行。目录需要有执行权限才能进入。
