Linux系统命令
###############

1. linux 查看存储空间
======================

1. linux磁盘/挂载的文件系统使用量

::

    df -h

2. 检查文件和目录的磁盘使用量

::

    du -sh *

3. 列出块设备以及其挂载点

::

    lsblk

4. 监视系统输入/输出设备负担

::

    iostat

5. 一次性创建多个嵌套文件夹

::

    mkdir -p ~/some/nested/directory/structure

2. linux查看系统信息
=======================

1. uname查看系统信息

2. lscpu查看cpu信息

3. lspci列出所有pci设备

4. lsusb列出所有usb设备

3. 文件权限所有权
=====================

1. chmod改变文件权限

2. chown 改变文件所有者

3. chgrp 改变文件所属组

4. 用户和组操作
===============

1. Creat a User
-----------------
chech user information ``cat /etc/passwd``

.. note::
    format:
    username:password-placeholder:UID:GID:comment-for-user:user-home-dir:login-shell

- creat a user and give it a password

::

    $useradd [name]
    $passwd [***]

- creat a user and give it a UID(the UID will copy to GID),add a comment with a ``-c`` argument

::

    $ useradd -u [UID] [name] -c "This is a comment"

- creat a user and give it a HOME_DIR

::

    $ useradd [name] -d /path/to/HOME_DIR

- creat a user and give it a defalt name HOME_DIR and give it a group

::

    $ useradd -m -G [groupname] [username]

- modify homedir for user

::

    sudo usermod -d /new/home/dir -m username

- creat a homedir for new user

::

    sudo mkhomedir_helper username

::

    sudo mkdir /home/username
    sudo cp -r /etc/skel. /home/username
    sudo chown -R username:useername /home/username
    sudo chmod 700 /home/username

2. Modify a user's informations
--------------------------------

- modify the user name

::

    $ usermod -l name_new name

- modify user's HOME_DIR ``-m`` for move data from old user HOME_DIR to new USER_DIR

::

    $ usermod -d /path/to/New_HOME_DIR [name] # just modify the HOME_DIR
    $ usermod -d /path/to/New_HOME_DIR -m [name] # change HOME_DIR and move
    the dsata from old to new

- add expiredate to a user

chage command

::

    $ chage -E "YYYY-MM-DD" [username]
    # then u can use chage -l to check it. notice the Account expires
    $ chage -l [username]
    # and if u want to back to infinte expires
    $ chage -E -1 [username]

usermod command

::

    $ usermod -e "YYYY-MM-DD" [username]
    # this is for infinte expires
    $ usermod -e "" [username]

3. delete user
------------------

- delete user but save the home dir

::

    $ userdel [username]
    # delete user but save home dir and the mail dir /var/mail/[username] 
    $ userdel -f [username]
    # you can use id [username] to check if the account is alive or not

- delete all of things for the user, even HOME_DIR and mail dir

::

    $ userdel -r [username]
    # if the user is alive and the process is on, stop them by pkill
    $ pkill -u [username]

2. groups manage
================

1. creat and manage groups
---------------------------

- creat a normal group

::

    $ groupadd [groupname]

- creat a system group GID < 1000

::

    $ groupadd -r [groupname]
    # use -g to specify a uniqe GID like 500
    $ groupadd -g 500 [groupname]

- add user to group

::

    $ usermod -aG [groupname] [username]
    # -a means append on, not to cover original group
    # -G means to specify a group to append on
    # the uid of normal group begain with 1000,the system group is not less 
    # than 1000

- check groups

::

    $ cat /etc/group
    # check which group belones to user
    $ groups [username]

- delete a group

::

    $ groupdel [groupname]

when u delete a user, its group didn't delete,this is for protect share group

2. group permission
--------------------

- share dirctory

::

    $ mkdir /shared
    $ chgrp [groupname] /shared # change dir's group owner
    $ chmod 775 /shared
    $ chmod g+s /shared # set SGID for inherit group ower,when creat new file
      in this shared directory

- creat a user and set default group for it

::

    $ useradd -m -g [groupname] -G [groupname] [username]
    # -m is for his HOME_DIR
    # -g is setting a main group for it
    # -G is setting a append group for it

systemd daemon 编写
====================

一、万能模板结构
文件通常放在 /etc/systemd/system/ 目录下，文件名必须以 .service 结尾（例如 myapp.service）。

::

    [Unit]
    # 1. 服务描述
    Description=这里是服务的简短描述
    # 2. 依赖关系（确保网络或其他服务先启动）
    After=network.target
    # 3. 强制依赖（如果 mysql 挂了，这个服务也不启动）
    # Requires=mysql.service

    [Service]
    # 1. 服务类型（最常用 simple）
    Type=simple
    # 2. 启动命令（必须写绝对路径！）
    ExecStart=/usr/bin/my-program --config /etc/myapp/config.ini
    # 3. 运行用户（安全起见，不要用 root）
    User=www-data
    Group=www-data
    # 4. 工作目录（程序运行时的当前目录）
    WorkingDirectory=/var/www/myapp
    # 5. 重启策略（崩溃后自动重启）
    Restart=on-failure
    RestartSec=5
    # 6. 环境变量（如果程序需要）
    Environment="JAVA_OPTS=-Xmx2G"
    # 7. 限制打开文件数（MC 服务器必备）
    LimitNOFILE=65535

    [Install]
    # 1. 开机自启的目标
    WantedBy=multi-user.target

1. [Unit] 部分：管理依赖
---------------------------

============    ====================================    ===============================
参数            说明                                    示例
============    ====================================    ===============================
Description     服务描述，systemctl status 时显示       Description=Minecraft Server
After           在哪些服务之后启动（不强制依赖）        After=network.target (联网后)
Requires        强制依赖，如果它挂了，本服务也不启动    Requires=docker.service
Wants           弱依赖，它挂了，本服务照常启动          Wants=network-online.target
============    ====================================    ===============================

2. [Service] 部分：核心配置
---------------------------

================    ==============  ===========================================================================
参数                说明            常见值/示例
================    ==============  ===========================================================================
Type                进程类型        simple (默认，前台运行)forking (后台守护进程)oneshot (运行完就退出，如脚本)
ExecStart           启动命令        /usr/bin/java -jar server.jar⚠️ 必须绝对路径
ExecStop            停止命令        /usr/bin/kill $MAINPID
ExecReload          重载配置命令    /bin/kill -HUP $MAINPID
User / Group        运行身份        User=root 或 User=mc
WorkingDirectory    工作目录        /home/mc/server
Restart             重启策略        no (默认)always (总是重启)on-failure (非正常退出重启)
RestartSec          重启间隔秒数    5 (防止重启循环过快)
Environment         环境变量        Environment="PATH=/usr/bin"
LimitNOFILE         最大文件打开数  65535 (MC 服必设，防止玩家多报错)
StandardOutput      日志输出        journal (默认，用 journalctl 看)    file:/var/log/app.log
================    ==============  ===========================================================================

3. [Install] 部分：安装配置
------------------------------

========    ==============  ==========================================
WantedBy    哪个目标下启用  multi-user.target (多用户模式，即正常启动)
========    ==============  ==========================================
