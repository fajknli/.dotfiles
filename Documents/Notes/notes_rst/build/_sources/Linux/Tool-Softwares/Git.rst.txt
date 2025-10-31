Git 日常使用
#############

…or create a new repository on the command line

::

    echo "# .dotfiles" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/fajknli/.dotfiles.git
    git push -u origin main

…or push an existing repository from the command line

::

    git remote add origin https://github.com/fajknli/.dotfiles.git
    git branch -M main
    git push -u origin main

.. note::

    git add -u      # for remove file push to remote repository

Common Commands
-------------------------------------------------------

--force-with-lease	            安全强制推送，避免覆盖他人提交(比--force安全)。

git diff --quiet --cached	    检测暂存区是否有变动，用于脚本判断(--quiet不输出变动信息,而是输出0/1)。

${1:-main}	                    Shell 参数默认值，未提供 $1 参数时使用 main。

-u in git push	                首次推送时建立追踪关系(git push origin main 选择main,适合脚本使用)-u 只是建立分支追踪。

--all vs -u in git add --all    包含新增文件，-u 仅限已跟踪文件的修改和删除。

1. .dotfile 初始设置步骤
===========================

在 ~/.dotfiles 创建一个裸 Git 仓库

.. code-block:: bash

    git init --bare ~/.dotfiles

创建一个名为 dotfiles 的别名，它指向 git 但特别指定：1.Git 目录(--git-dir)指向裸仓库 2.工作目录(--work-tree)指向你的家目录

.. code-block:: bash

   alias dotfiles='/usr/bin/git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME"'

配置 Git 不显示未跟踪文件的状态,这很重要，因为家目录下有许多你不想跟踪的文件

.. code-block:: bash

   dotfiles config status.showUntrackedFiles no

::

    检查当前仓库配置
    dotfiles config --list


1. 日常dotfile更新使用git管理.dotfiles
==========================================

1. 日常操作流程
-------------------

添加新配置文件：

::

    # 1. 添加文件到跟踪
    dotfiles add ~/.config/nvim/init.vim

    # 2. 提交变更
    dotfiles commit -m "feat(nvim): add init config"

    # 3. 推送到远程
    dotfiles push origin main

修改现有配置：

::

    # 1. 编辑文件
    vim ~/.bashrc

    # 2. 查看变更
    dotfiles diff

    # 3. 暂存并提交
    dotfiles add -p ~/.bashrc  # 交互式选择变更
    dotfiles commit -m "fix(bash): update aliases"

撤销操作：

::

    # 撤销工作区修改
    dotfiles restore ~/.vimrc

    # 撤销暂存
    dotfiles restore --staged ~/.ssh/config

    # 修改上次提交
    dotfiles commit --amend



**日常使用大全**

::

    # 先添加远程仓库地址
    dotfiles remote add origin git@github.com:你的用户名/.dotfiles.git
    # 如果已经有了，修改的方法如下
        # 删除原地址
        git remote remove origin
        # 添加地址
        git remote add origin git@github.com:your_username/your_repository.git
    # 查看当前远程仓库配置
    # dotfiles remote -v

    # 添加到暂存区
    # 添加单个文件（如 .bashrc）
    dotfiles add ~/.bashrc
    # 添加多个文件
    # dotfiles add ~/.vimrc ~/.zshrc
    # 添加整个目录（如 .config/ 下的配置）
    # dotfiles add ~/.config/nvim/
    # dotfiles add -u  # 更新已经添加的追逐文件，只添加已被跟踪文件的修改（不添加新文件）
    dotfiles add -A  # 添加所有变更（包括新文件，慎用）
    dotfiles add -p  # 交互式选择要暂存的修改（可精确控制）

    #暂存区删除/撤回------------------------------------------------------------------

    # 删除已经追踪的添加到暂存区的文件/目录
    从 Git 跟踪中删除（保留本地文件）
    # 删除单个文件（保留工作区文件）
    dotfiles rm --cached ~/.config/waybar/config.json
    # 删除整个目录（保留工作区目录）
    dotfiles rm --cached -r ~/.config/waybar/
    # 效果：
    # 文件/目录将不再被 Git 跟踪
    # 本地文件仍保留在磁盘中

    # 彻底删除（Git + 本地文件）
    # 删除文件（同时从磁盘和Git删除）
    dotfiles rm ~/.bash_history
    # 删除目录（递归删除）
    dotfiles rm -r ~/.cache/
    # 危险操作：本地文件会被永久删除！
    # 补救措施：
    # 若误删，可用 dotfiles checkout HEAD -- <文件> 恢复。

    # 仅从暂存区撤回（保留修改）
    # 撤回单个文件的暂存状态
    dotfiles restore --staged ~/.ssh/config
    # 撤回所有暂存文件
    dotfiles reset
    # 效果：
    # 文件会回到 "Changes not staged for commit" 状态
    # 适用场景：
    # 暂存后发现有不需要提交的修改

    # 暂存区------------------------------------------------------------------

    # 查看已经添加追踪的文件
    dotfiles ls-files
    # 树状结构显示，方便看
    dotfiles ls-files | sed "s|^|$HOME/|" | tree -a -F --fromfile

    # 查看所有文件变更状态（最常用）
    dotfiles status -v
    # 或简洁模式：
    dotfiles status -s
    # 输出标记说明：
    # M：工作区文件已修改（未暂存）
    # M ：修改已暂存（未提交）
    # A ：新增文件已暂存
    # ??：未跟踪文件
    # D：文件已删除（未暂存）

    # 查看工作区文件的具体修改
    # 显示所有未暂存的详细变更（行级对比）
    dotfiles diff
    # 查看特定文件：
    dotfiles diff -- ~/.bashrc

    #查看提交------------------------------------------------------------------
    
    # 查看提交的历史记录和详细信息
    # 1. 查看简洁提交历史
    dotfiles log --oneline
    # 每行显示：提交哈希(前7位) 分支/HEAD位置 提交信息

    # 2. 查看完整提交详情
    dotfiles log -p
    # 包含：
    # 提交哈希、作者、日期
    # 提交信息
    # 文件变更内容（-p 表示显示差异）

    # 3. 查看特定文件的修改历史
    dotfiles log --follow -- ~/.bashrc
    # --follow：跟踪文件重命名历史
    # -- <文件路径>：必须用绝对路径

    # 4. 图形化分支历史
    dotfiles log --graph --all --decorate

    # 5. 查看最近 N 次提交
    dotfiles log -n 2  # 查看最近2次提交

    # 6. 按时间/作者筛选
    dotfiles log --since="2023-10-01" --until="2023-10-31" --author="fajknli"

    # 7. 查看某次提交的完整内容
    dotfiles show a1b2c3d
    # 或
    dotfiles log -1 -p a1b2c3d

    # 8. 查看提交统计
    dotfiles shortlog -sn  # 按作者统计提交次数
    dotfiles log --stat    # 显示每次提交的文件变更统计

    # 查看远程提交
    dotfiles fetch origin  # 先获取远程更新
    dotfiles log origin/main  # 查看远程分支历史

    # 撤回提交------------------------------------------------------------------

    # 1. 撤回最新提交但保留修改（最常用） 
    dotfiles reset --soft HEAD~1
        # 效果：
        # 撤销最近一次提交
        # 所有更改保留在暂存区（如同刚执行过 dotfiles add）
    # 适用场景：
    # 提交信息写错了，或需要补充文件到这次提交

    # 2. 撤回提交并取消暂存（保留工作区修改）
    dotfiles reset HEAD~1
    或等效命令：
    dotfiles reset --mixed HEAD~1
        # 效果：
        # 撤销提交
        # 更改保留在工作目录（需重新 add）
    # 适用场景：
    # 需要重新组织提交内容

    # 3. 彻底丢弃提交和修改（谨慎！）
    dotfiles reset --hard HEAD~1
        # 效果：
        # 撤销提交
        # 丢弃所有修改（工作区和暂存区都恢复到上一次提交状态）
    # 危险操作：所有未提交的更改将永久丢失！

    # 4. 撤回已推送到远程的提交
    # 先本地撤回（参考上述方法）
    dotfiles reset --soft HEAD~1
    # 强制推送到远程（需协作成员知晓）
    dotfiles push -f origin main
        # 警告：
        # 会重写远程历史
        # 如果其他人已基于该提交工作，会导致协作混乱

    # 5. 创建反向提交（最安全）
    dotfiles revert HEAD
    例如:
    dotfiles revert a1b2c3d  # 撤销特定提交
        # 效果：
        # 生成一个新提交，内容与指定提交相反
        # 不改变历史，适合已公开的提交

    完整工作流示例
    # 1. 查看提交历史确认要撤回的提交
    dotfiles log --oneline
    # 2. 撤回提交但保留修改（假设要撤销 HEAD）
    dotfiles reset --soft HEAD~1
    # 3. 重新提交
    dotfiles commit -m "新的提交信息"
    # 4. 如果之前已推送，强制更新远程
    dotfiles push -f origin main

    # 推送------------------------------------------------------------------

    # 首次推送（使用 -u 设置上游分支）
    dotfiles push -u origin main
    # 后续常规推送
    dotfiles push

    # 查看推送------------------------------------------------------------------

    # 查看已经推送到远程仓库的提交记录
    # 1. 查看本地与远程的差异
    dotfiles log origin/main..main
    # 显示已提交但未推送的提交
    # 如果无输出，表示所有本地提交已推送

    # 2. 查看远程分支最新状态
    dotfiles fetch origin  # 先更新远程信息
    dotfiles log --oneline origin/main

    # 3. 查看所有分支的推送状态
    dotfiles branch -vv
    # 输出示例：
    # * main a1b2c3d [origin/main: ahead 1] 最新提交
    # ahead 1 表示有1个提交未推送
    # behind 2 表示远程有2个新提交未拉取

    # 5. 图形化查看
    dotfiles log --graph --all --decorate

    # 撤回推送------------------------------------------------------------------

    # 1. 撤回已推送到远程的提交
    # 先本地撤回（参考上述方法）
    dotfiles reset --soft HEAD~1
    # 强制推送到远程（需协作成员知晓）
    dotfiles push -f origin main
        # 警告：
        # 会重写远程历史
        # 如果其他人已基于该提交工作，会导致协作混乱

    # 2. 创建反向提交（最安全）
    dotfiles revert HEAD
    例如:
    dotfiles revert a1b2c3d  # 撤销特定提交
        # 效果：
        # 生成一个新提交，内容与指定提交相反
        # 不改变历史，适合已公开的提交

2. 同步与维护
------------------

从远程更新：

::

    dotfiles fetch origin
    dotfiles merge origin/main
    # 或使用 pull：
    dotfiles pull origin main

清理旧文件：

::

    # 从Git删除但保留本地文件
    dotfiles rm --cached ~/.oldconfig

    # 彻底删除文件
    dotfiles rm ~/.deprecated_file

3. 多机器同步策略
--------------------

首次在新机器设置：

::

    # 克隆仓库（裸模式）
    git clone --bare  https://github.com/fajknli/.dotfiles.git$HOME/.dotfiles

    # 设置别名
    echo "alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> ~/.bashrc
    source ~/.bashrc

    # 尝试检出文件（冲突文件需处理）
    dotfiles checkout 2>&1 | grep -E "\s+\." | awk {'print $1'} | xargs -I{} mv {} {}.bak
    dotfiles checkout

定期同步：

::

    # 拉取远程更新（自动处理冲突）
    dotfiles pull --autostash

2. 在新系统上恢复配置
=======================

将你的点文件仓库克隆为裸仓库

.. code-block:: bash

    git clone --bare https://github.com/fajknli/.dotfiles.git $HOME/.dotfiles

    alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

    dotfiles checkout #尝试将文件检出到家目录

    # 如果文件已存在会报错，可强制检出覆盖：
    dotfiles checkout -f

    dotfiles config --local status.showUntrackedFiles no


3. git-crypt 部分加密 
======================

实现部分配置文件公开、部分加密的混合管理

0. 备份,因为这个会加密文件
----------------------------

:: 

    cp -r ~/.dotfiles ~/.dotfiles-backup  # 备份裸仓库

1. 初始化加密
----------------

::

    # 安装git-crypt
    pacman -S git-crypt

    # 在 dotfiles 仓库初始化加密
    cd ~
    git-crypt init

2. 创建加密规则
-----------------



3. 添加协作开发者
-------------------

::

    # 导出密钥给可信设备
    git-crypt export-key ~/dotfiles.key

    # 在其他设备导入密钥
    git-crypt import-key ~/dotfiles.key


- 加密文件：匹配 .gitattributes 规则的文件会自动加密

- 公开文件：其他文件正常显示

- 推送后效果：

  - 公开文件：GitHub 上可直接查看
 
  - 加密文件：显示为加密二进制 blob

4. git-crypt 密钥备份与恢复
================================

1. 多重密钥备份策略
-----------------------

::

    # 1. 生成主密钥（默认）
    git-crypt init && echo ".gitattributes !filter !diff" >> .gitattributes

    # 2. 导出加密密钥（建议至少备份3份）
    git-crypt export-key ~/dotfiles-key-1.key
    gpg --encrypt -r your@email.com ~/dotfiles-key-1.key  # 加密备份

    # 3. 存储到安全位置：
    #    - 密码管理器（Bitwarden/1Password）
    #    - 加密的云存储（Cryptomator + Google Drive）
    #    - 物理介质（加密的USB驱动器）

2. 协作密钥管理（团队场景）
------------------------------

::

    # 添加团队成员的公钥授权
    git-crypt add-gpg-user USER_ID  # 使用团队成员的GPG公钥

    # 导出所有授权用户列表（便于审计）
    git-crypt ls-gpg-users > gpg-users.txt

3. 自动化密钥轮换
---------------------

::

    # 每年轮换密钥（需更新所有备份）
    git-crypt revoke
    git-crypt init
    git-crypt export-key new-key.key
    # 通知协作者
    # 其他用户需执行：
    git-crypt unlock
    dotfiles pull

预提交钩子（防止再次泄露）

::

    cat > ~/.dotfiles/hooks/pre-commit <<'EOF'
    #!/bin/bash
    if git diff --cached | grep -qE "password|PRIVATE_KEY"; then
      echo "错误：提交包含敏感信息！"
      exit 1
    fi
    EOF
    chmod +x ~/.dotfiles/hooks/pre-commit

4. 加密规则测试
-----------------

加密规则编写

::

    cat > ~/.gitattributes <<'EOF'
    # 加密单个文件
    .env          filter=git-crypt diff=git-crypt

    # 加密整个目录
    .ssh/*        filter=git-crypt diff=git-crypt
    .aws/config   filter=git-crypt diff=git-crypt

    # 排除目录中的特定文件
    .config/sops/** filter=git-crypt diff=git-crypt
    !*.config/sops/public.yml  # 此文件不加密

    # 二进制文件加密（如图片/证书）
    *.key         filter=git-crypt diff=git-crypt
    *.pem         filter=git-crypt diff=git-crypt

    # 确保 .gitattributes 自身不被加密
    .gitattributes !filter !diff
    EOF


::

    # 测试文件是否被正确加密
    echo "test" > ~/.ssh/test-file
    dotfiles add ~/.ssh/test-file

    git-crypt status -e  # 应显示文件为加密状态,应显示 "encrypted"
    # 查看远程文件内容（应显示加密）

    curl -s https://raw.githubusercontent.com/you/repo/main/credentials.json | file -
    # 正确输出: data (加密二进制)

5. 先拉取加密内容，再解密
---------------------------

::

    # 1. 拉取远程加密文件（此时文件仍是加密状态）
    dotfiles pull

    # 2. 解密文件（需提前配置好密钥）
    git-crypt unlock

    # 3. 验证文件
    cat ~/.ssh/config  # 应显示解密后的明文

多设备同步场景

新设备初始化：

::

    # 1. 克隆仓库（文件以加密形式存在）
    git clone --bare git@github.com:you/dotfiles.git ~/.dotfiles
    alias dotfiles='git --git-dir=$HOME/.dotfiles --work-tree=$HOME'

    # 2. 拉取加密文件
    dotfiles checkout

    # 3. 导入密钥并解密
    git-crypt import-key ~/backup/dotfiles-key.key
    # 检查密钥是否导入
    git-crypt status -k
    git-crypt unlock

日常更新：

::

    # 1. 拉取远程加密更新
    dotfiles pull

    # 2. 自动解密（如果之前已unlock且密钥未变）
    # 无需重复unlock

6. 问题
-----------

- git-crypt 的局限性：仅对启用加密后的新提交生效，无法自动加密历史记录。

- 历史记录的危险性：即使最新提交已加密，通过 git checkout <旧提交> 仍可获取明文敏感信息。

1. 彻底重写历史

::

    # 安装 filter-repo

    # 重写历史并加密敏感文件
    git-filter-repo \
      --path .ssh/ \
      --path .aws/ \
      --force

    检查历史记录

    # 确认历史中无敏感信息
    dotfiles log -p | grep -E "password|api_key|PRIVATE"

    # 检查文件是否加密
    git-crypt status -e | grep "not encrypted" && echo "存在未加密文件！"

2. 强制同步到远程

::

    dotfiles push -f --all
    dotfiles push --tags --force

3. 通知所有协作者

::

    紧急通知：仓库历史已重写，请按以下步骤操作：
    1. 删除旧仓库克隆：
        rm -rf ~/.dotfiles ~/dotfiles

    2. 重新克隆：
        git clone --bare git@github.com:you/dotfiles.git ~/.dotfiles

    3. 导入密钥解密：
        git-crypt import-key ~/path/to/key.key
        git-crypt unlock


Hits
========

裸仓库特殊性：

通过 dotfiles 别名操作时，路径必须：

- 从 $HOME 开始的绝对路径（如 ~/.config/waybar/）,不能在/根目录或者/home目录下执行dotfiles命令
- 或从家目录操作的正确相对路径

==============  ==================================  ====================================================
场景	        推荐命令	                        说明
==============  ==================================  ====================================================
首次推送分支    dotfiles push -u origin main        必须用 -u 设置上游
后续常规推送    dotfiles push                       最简形式（依赖首次设置的 upstream）
推送到其他分支  dotfiles push origin other-branch   需明确指定远程和分支名
强制覆盖远程    dotfiles push -f                    危险操作！仅用于修复历史记录（需确保协作成员知晓）
==============  ==================================  ====================================================

- dotfiles status  # 只显示已跟踪文件的变化（因设置了 showUntrackedFiles no）
- dotfiles commit -m "添加 bash 和 vim 配置"  # 提交到本地
- dotfiles show <master 序列号>  # 查看提交的变化内容,和 ``dotfiles show HEAD`` , ``dotfiles log -p -1`` 是一样的，不过这个是查看最新提交的详细修改。 ``dotfiles diff HEAD~1 HEAD`` 这个是比较前一次提交和当前提交。

Git 遵循“显式操作”原则，只有通过 git add 添加的文件才会被跟踪。

手动复制文件后，git status 会显示这些文件是 Untracked files（未跟踪），除非你明确 add 它们。

.. 撤销本地修改	dotfiles restore ~/.file
.. 更新远程变更	dotfiles pull

.. 可用 git secret 等工具加密 重要文件

----

忽略文件：

::

    # 1. 全局忽略（不提交到仓库）
    echo ".cache/" >> $HOME/.dotfiles/info/exclude

    # 2. 仓库级忽略（需提交）
    dotfiles add ~/.gitignore

常见错误解决：

::

    # 错误：文件已存在阻止检出
    dotfiles checkout 2>&1 | grep -E "error: .* already exists" | awk {'print $3'} | xargs -I{} mv {} {}.bak

    # 错误：认证失败
    dotfiles remote set-url origin git@github.com:yourusername/dotfiles.git

检查仓库健康：

::

    dotfiles fsck
    dotfiles count-objects -v

github 的ssh 认证
======================

- 步骤 1：生成 SSH 密钥（如果尚未生成）

.. code-block:: bash

    ssh-keygen -t ed25519 -C "your_email@example.com"

（全程按 Enter 使用默认路径）

- 步骤 2：将公钥添加到 GitHub

.. code-block:: bash

    cat ~/.ssh/id_ed25519.pub

复制输出内容 → 进入 GitHub SSH Keys 设置页 → 点击 "New SSH key" 粘贴

- 步骤 3：修改远程仓库地址为 SSH 格式

.. code-block:: bash

    dotfiles remote set-url origin git@github.com:fajknli/.dotfiles.git

- 步骤 4：测试连接

.. code-block:: bash

    ssh -T git@github.com

看到 You've successfully authenticated 表示成功。

gpg 
==========================

1. 基础加密操作

::

    gpg --encrypt -r your@email.com -o dotfiles-key.key.gpg dotfiles-key.key

- -r your@email.com：指定接收者的 GPG 公钥（对应邮箱）

- -o：指定加密后的输出文件（默认会生成 .gpg 后缀的二进制文件）

- 输入文件：dotfiles-key.key 是原始的 git-crypt 对称密钥

验证加密文件：

::

    file dotfiles-key.key.gpg  # 应显示 "PGP RSA encrypted message"

2. 解密密钥（使用时）

::

    gpg --decrypt -o dotfiles-key.key dotfiles-key.key.gpg

- 需输入接收者的 GPG 私钥密码

- 解密后的文件 dotfiles-key.key 需严格限制权限：

  ::

      chmod 600 dotfiles-key.key

3. 安全增强技巧

使用 ASCII 格式（便于复制）：

::

    gpg --armor --encrypt -r your@email.com -o dotfiles-key.key.asc dotfiles-key.key

- --armor：生成 ASCII 格式（.asc 文件）而非二进制

指定加密算法（如强制使用 AES-256）：

::

    gpg --encrypt --cipher-algo AES256 -r your@email.com dotfiles-key.key

