# git 命令详解

## 一句话理解 git

git 是版本控制工具，用来**跟踪文件变化**、协同开发、代码管理。

```bash
# 最常用三个命令
git add .          # 暂存修改
git commit -m "说明" # 提交到本地
git push           # 推送到远程
```

## 最常用场景

### 1. 日常提交

```bash
# 查看当前状态
git status

# 添加文件到暂存区
git add file.txt      # 添加单个文件
git add .             # 添加所有修改
git add *.py          # 添加所有 py 文件

# 提交
git commit -m "修复了某个bug"

# 推送到远程
git push origin main

# 拉取远程更新
git pull origin main
```

### 2. 克隆仓库

```bash
# 克隆仓库（你之前用的）
git clone https://github.com/fajknli/.dotfiles.git

# 克隆指定分支
git clone -b dev https://github.com/user/repo.git

# 浅克隆（只拉取最新一次提交，省空间）
git clone --depth 1 https://github.com/user/repo.git
```

### 3. 分支管理

```bash
# 查看分支
git branch              # 本地分支
git branch -r           # 远程分支
git branch -a           # 所有分支

# 创建分支
git branch feature-xxx

# 切换分支
git checkout feature-xxx
git switch feature-xxx  # 新命令

# 创建并切换
git checkout -b feature-xxx
git switch -c feature-xxx

# 合并分支
git checkout main
git merge feature-xxx

# 删除分支
git branch -d feature-xxx      # 删除本地
git push origin --delete feature-xxx  # 删除远程
```

## 核心概念

| 概念 | 说明 |
|------|------|
| 工作区 | 你正在修改的文件 |
| 暂存区 | `git add` 后的临时区域 |
| 本地仓库 | `git commit` 后的提交历史 |
| 远程仓库 | GitHub/GitLab 上的仓库 |

```
工作区 → git add → 暂存区 → git commit → 本地仓库 → git push → 远程仓库
```

## 常用命令速查

| 目的 | 命令 |
|------|------|
| 查看状态 | `git status` |
| 查看历史 | `git log --oneline` |
| 查看修改内容 | `git diff` |
| 添加文件 | `git add 文件名` |
| 提交 | `git commit -m "信息"` |
| 推送 | `git push` |
| 拉取 | `git pull` |
| 克隆 | `git clone 地址` |
| 查看分支 | `git branch` |
| 切换分支 | `git checkout 分支名` |
| 创建分支 | `git checkout -b 分支名` |
| 合并分支 | `git merge 分支名` |
| 撤销暂存 | `git reset HEAD 文件名` |
| 撤销提交 | `git reset --soft HEAD~1` |
| 放弃修改 | `git checkout -- 文件名` |

## 实际例子

### 1. 提交代码（标准流程）

```bash
# 查看修改了什么
git status
git diff

# 添加文件
git add .

# 再次确认
git status

# 提交
git commit -m "添加了用户登录功能"

# 推送到远程
git push origin main
```

### 2. 同步远程更新

```bash
# 拉取远程更新（推荐）
git pull origin main

# 等价于
git fetch origin main
git merge origin/main

# 只拉取不合并
git fetch origin
```

### 3. 撤销操作

```bash
# 放弃工作区的修改（未 add）
git checkout -- file.txt
git restore file.txt   # 新命令

# 撤销暂存（已 add）
git reset HEAD file.txt
git restore --staged file.txt   # 新命令

# 撤销上一次提交（保留修改）
git reset --soft HEAD~1

# 撤销上一次提交（丢弃修改）
git reset --hard HEAD~1

# 撤销提交并保留在暂存区
git reset --mixed HEAD~1
```

### 4. 查看历史

```bash
# 简洁历史
git log --oneline

# 图形化历史
git log --oneline --graph

# 最近5条
git log -5 --oneline

# 查看某个文件的修改历史
git log --oneline -- file.txt
```

### 5. 处理冲突

```bash
# 拉取时出现冲突
git pull

# 手动编辑冲突文件，删除 <<<<<<< ======= >>>>>>> 标记
vim file.txt

# 标记为已解决
git add file.txt

# 继续合并
git commit

# 或者放弃合并
git merge --abort
```

### 6. 裸仓库（你笔记里记的）

```bash
# 创建裸仓库
git clone --bare https://github.com/fajknli/.dotfiles.git $HOME/.dotfiles

# 设置别名
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# 检出配置
dotfiles checkout

# 忽略未追踪文件
dotfiles config --local status.showUntrackedFiles no
```

## 分支工作流

### 创建并切换分支

```bash
# 创建新分支
git checkout -b feature-login

# 做一些修改
git add .
git commit -m "添加登录功能"

# 推送到远程
git push origin feature-login

# 切换回主分支
git checkout main

# 合并分支
git merge feature-login

# 删除分支
git branch -d feature-login
```

### 查看分支差异

```bash
# 查看两个分支的差异
git diff main..feature

# 查看分支差异的文件列表
git diff --name-only main..feature
```

## 标签管理

```bash
# 创建标签
git tag v1.0.0

# 创建带注释的标签
git tag -a v1.0.0 -m "发布1.0版本"

# 推送标签到远程
git push origin v1.0.0

# 推送所有标签
git push --tags

# 查看标签
git tag -l

# 删除标签
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## 常见问题

### 1. 提交信息写错了

```bash
# 修改最近一次提交信息
git commit --amend -m "新的提交信息"

# 修改最近一次提交（不改变信息）
git commit --amend --no-edit
```

### 2. 忘记添加文件就提交了

```bash
# 添加漏掉的文件
git add forgotten.py

# 合并到上一次提交
git commit --amend --no-edit
```

### 3. 误提交到错误分支

```bash
# 撤销最后一次提交
git reset HEAD~1

# 切换到正确分支
git checkout correct-branch

# 重新提交
git add .
git commit -m "信息"
```

### 4. 查看某个文件的修改历史

```bash
# 查看文件每次提交的修改
git log -p -- file.txt

# 查看文件是谁改的
git blame file.txt
```

## .gitignore 常用内容

```gitignore
# Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*~

# 系统
.DS_Store
Thumbs.db

# 日志
*.log
*.pid

# 敏感文件
.env
*.key
*.pem
```

## 快捷命令别名

```bash
# 设置别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph"

# 使用
git st        # git status
git co main   # git checkout main
git br        # git branch
git ci -m "xx" # git commit -m "xx"
git lg        # 图形化历史
```

## 常用组合速查

| 目的 | 命令 |
|------|------|
| 克隆仓库 | `git clone url` |
| 查看状态 | `git status` |
| 添加所有 | `git add .` |
| 提交 | `git commit -m "msg"` |
| 推送 | `git push` |
| 拉取 | `git pull` |
| 查看历史 | `git log --oneline` |
| 查看分支 | `git branch -a` |
| 创建分支 | `git checkout -b branch` |
| 合并分支 | `git merge branch` |
| 放弃修改 | `git checkout -- file` |
| 撤销提交 | `git reset --soft HEAD~1` |
| 查看差异 | `git diff` |
| 暂存修改 | `git stash` |
| 恢复暂存 | `git stash pop` |

## 一句话总结

git 核心：`git add .` → `git commit -m "说明"` → `git push` 是日常三连。`git status` 随时看状态，`git log --oneline` 看历史，`git checkout -b 新分支` 建分支。
