Use_of_Software
#################

.. wpa_cli使用和配置文件
.. ######################

NetworkManger(nmcli)使用
==================================

1. 查看所用网络设备状态

::

    nmcli device status

2. 查看所有可用的wifi网络

::

    nmcli device wifi list

3. 连接到wifi网络

::

    1. nmcli device wifi connect <ssid> --ask 

    2. nmcli device wifi connect <SSID> password <PassWord>

4. 断开wifi连接

::

    nmcli device disconnect wlan0

5. 查看当前活动的网络连接

::

    nmcli connection show --active

6. 创建一个新的网络连接

::

    nmcli connection add type wifi con-name "<WIFI_NAME>" ifname wlan0 ssid <SSID> wifisec.dev wifi-psk "<PASSWORD>"

7. 启用/禁用网络连接

::

    nmcli connection up/down id "<WIFI_NAME>"

8. 修改现有的网络连接

::

    nmcli connection modify <SSID> wifi-sec.dev <NEW_PASSWORD>

9. 删除网络

::

    nmcli connection delete id "<WIFI_NAME>"

10. 查看NetworkManager状态

::

    nmcli general status

11. 检查NetworkManager是否在运行

::

    nmcli -t -m device status

12. 设置网络连接的自动启动

::

    nmcli connection modify "<WIFI_NAME>" connection.autoconnect yes




1. wpa_cli 的使用
====================

首先要先把wpa_supplicant服务启用，我用的是voidlinux,启动服务的方法是把/etc/sv 下的wpa_supplicant服务添加到，/var/server/下，

::

	ln -s /etc/sv/wpa_supplicant /var/server/

那么对于wpa_cli命令的简单使用，我用的是wifi连接，WPA-PSK网络

使用 scan 和 scan_results 命令查看可用网络： 

::


	>scan # 进行wifi的扫描
	OK
	>scan_results  # 显示scan的结果
	>add_network 0
	0
	>set_network 0 ssid "wifi name"
	OK
	>set_network 0 psk "wifi password"
	Owctl [--options] [commands]

                                   Available optionsK
	>set_network 0 key_mgmt WPA-PSK  # 不知道怎么的，这个有没有无所谓
	OK
	# 如果对应的 SSID 无需密码验证，则需要将命令 set_network 0 psk "passphrase" 替换为 set_network 0 key_mgmt NONE ，以将网络指定为无密码。
	>enable_network 0
	OK
	# 最后，将网络保存到配置文件中
	>save_config
	OK

	......
	
.. note::

	每个网络都按照数字顺序进行排列，所以第一个网络的索引为 0。

连接成功后会出现成功的连接信息，然后输入 'quit' 退出


----


2. wpa_supplicant 的使用
-------------------------

在此之前，得先了解wpa_passphrase,利用这个附加工具可以生成加密密码的.conf文件，然后再利用wpa_supplicant来进行连接

::

	wpa_passphrase <wifi name> <wifi password> > /etc/wpa_supplicant/wpa_supplicant.conf

	# 这个命令可以在/etc/wpa_supplicant/下生成wpa_supplicant.conf的文件

内容差不多如下：

::

	network={
	        ssid="cme"
	        psk="zxcvbnm123"
	}

	network={
	        ssid="hwifi"
	        psk="8psv537r"
	}

然后就可以利用wpa_supplicant通过wpa_supplicant.conf来进行连接了

::

	wpa_supplicant -i <网络接口名称，一般为wlan0,使用ip link 来查询> -B -c /etc/wpa_supplicant/wpa_supplicant.conf 

3. 利用dhcpcd获取ip
-------------------

如果连接成功了，完成后，你需要获取一个 IP 地址，例如使用 dhcpcd 。

::

	dhcpcd <网络接口名称，一般为wlan0,使用ip link 来查询>


----


iwd 使用
=================

1. iwctl 使用
--------------

::

    ╔[Thu Feb 15]═[~]
    ╚$ iwctl
    NetworkConfigurationEnabled: disabled
    Sage
    ateDirectory: /var/lib/iwd
    Version: 2.13
    [iwd]# device list
                                        Devices                                   *
    --------------------------------------------------------------------------------
      Name                  Address               Powered     Adapter     Mode
    --------------------------------------------------------------------------------
      wlan0                 74:4c:a1:81:39:97     on          phy0        station

    [iwd]# station wlan0 scan
    [iwd]# station wlan0 get-networks
                                   Available networks                             *
    --------------------------------------------------------------------------------
          Network name                      Security            Signal
    --------------------------------------------------------------------------------
      >   Xiaomi_wyks                       psk                 ****
          hwifi                             psk                 ****
          Asus_Game                         psk                 ****
          midea_da_1076                     psk                 ****
          lzh                               psk                 ****
          黑人                              psk                 ****
          岁月静好                          psk                 ****
          CU-515F                           psk                 ****
          midea_ca_3968                     psk                 ****
          309                               psk                 ****
          iTV-AYtf                          psk                 ****
          ChinaNet-AYtf                     psk                 ****
          CU-515F-5G                        psk                 ****
          Asus_wyks                         psk                 ****

    [iwd]# station wlan0 connect Xiaomi_wyks
    [iwd]# station wlan0 show
                                     Station: wlan0
    --------------------------------------------------------------------------------
      Settable  Property              Value
    --------------------------------------------------------------------------------
                Scanning              no
                State                 connected
                Connected network     Xiaomi_wyks
                IPv4 address          192.168.31.33
                IPv6 address        fd00:6868:6868::f9f
                IPv6 address        fd00:6868:6868:0:764c:a1ff:fe81:3997
                ConnectedBss          9c:9d:7e:7a:b9:25
                Frequency             2462
                Security              WPA2-Personal
                RSSI                  -62 dBm
                AverageRSSI           -62 dBm
                RxMode                802.11n
                RxMCS                 2
                RxBitrate             21700 Kbit/s

    [iwd]# station wlan0 connect-hidden hwifi
    Already provisioned
    [iwd]#


:device list: 列出网络接口设备
:station wlan0 scan: 使用wlan0接口扫描wifi
:station wlan0 get-networks: 列举出扫描到的wifi
:station wlan0 connect Xiaomi_wyks: 连接到Xiaomi_wyks网络
:station wlan0 connect-hidden hwifi: 连接到隐藏的hwifi
:station wlan0 show: 显示已经连接的wifi信息
:known-networks list:                                 列出已经知道的网络,List known networks             
:known-networks <"network name"> forget:              忘掉已经知道的网络，Forget known network            
:known-networks <"network name"> show:                Show known network              


如果连接上了wifi还是没有网络的话:

1. 检查DHCP,iwd默认没有启动DHCP,创建/编辑 `` /etc/iwd/main.conf `` ,其内容如下:

::

    [General]
    EnableNetworkConfiguration=true

再重启iwd服务

2. DNS解析问题

检查 `` /etc/resolv.conf `` 文件, 确认内容里是否有DNS服务器

::

    nameserver 114.114.114.114
    nameserver 8.8.8.8

3. 检查对应网络接口是否开启

::

    查看接口
    ip link show wlan0

    如果接口没有开启,就开启
    ip link set wlan0 up

4. 如果提示RF-Kill, 说明网卡被禁用,使用下面的命令解决

::

    检查所有无线设备的软阻止/硬阻止的状态
    sudo rfkill list

    找到对应网络接口并解除其的软硬阻止
    sudo rfkill unblock wifi/索引号

然后重启对应的网络服务,iwd 或者 NetworkManager

建议多重启来查看是否成功更改设置并生效







Whiptail
=============


**Whiptail 是 Linux 中的一种实用程序，可通过 shell 脚本创建对话框。它提供了一种在终端环境中通过简单的图形用户界面（GUI）与用户交互的方式。Whiptail 允许你显示各种类型的对话框，如消息框、输入框、菜单框等等。该工具通常用于在 Linux 系统中创建交互式脚本或菜单。**


1. 选项
---------

:--title: 设置对话框的标题
:--backtitle: 设置对话框背景的标题
:--yesno: 显示一个简单的 Yes/No 对话框
:--msgbox: 显示一个包含信息的对话框，用户点击OK后关闭
:--inputbox: 显示一个输入框，用户可以输入文本
:--passwordbox: 显示一个密码框，用户输入的文本不可见
:--textbox: 显示一个包含文本内容的框，用户只能查看，不能编辑
:--radiolist: 显示一个包含单选选项的对话框
:--checklist: 显示一个包含多选选项的对话框
:--menu: 显示一个包含菜单选项的对话框
:--gauge: 显示一个进度条对话框

::

    whiptail --menu "xxxxx" 20 50 10 "{list}" 3>&1 1>&2 2>&3

    其中，20 50 10 的意思是 高度：20 ，宽度：50，显示几列：10

    "{list}" 就是将显示的列内容

    3>&1 1>&2 2>&3 意思是先把3区域内容给1(标准输出),
    然后1的内容再给2(标准错误输出),然后2的错误输出再给3,但是之前已经把3指向了1,
    所以2的内容传给了1,所以总的来说就是1给了2,2给了1,就是交换了一下


----


GIT 使用
========

1. git 基础命令
------------------

:git config --global user.name "Your Name": 设置全局用户信息
:git config --global user.email "Email Address": 设置全局用户邮箱

:git init -b main: 初始化本地git仓库,并切换分支到main
:git checkout -b main: 切换到main分支
:git add <file>: 添加文件到暂存区
:git commit -m "comment": 提交到本地仓库
:git remote add origin <仓库网址>: 添加远程仓库
:git push -u origin main: 推送到远程仓库main主枝

:git remote -v: 查看远程仓库的概述,告诉你的仓库URL
:git remote show origin: 查看指导远程仓库(origin)的详细信息


2. 自动化提交，使用credential存储,实现自动提交，不需要每次输入用户名和密码
---------------------------------------------------------------------------
   
1.使用git config 设置全局的用户名和邮箱
::
    
    git config --global user.name "your name"
    git config --global user.emali "your@email.com"

2.生成一个包含用户名和密码的credential helper
::

    echo "https://username:password@github.com" > ~/.git-credentials

3.在git配置里启用credential存储
::

    git config --global credential.helper store

4.在git提交脚本里添加推送命令：

::

    git push origin master

这样每次运行提交脚本，git会自动从credential文件里读取用户名和密码，不需要手动输入

.. note::

    如果是想自动克隆仓库不想一直输入账号密码,在.bashrc 文件里输入：

    ``export GIT_ASKPASS="/path/to/.git-credentials"``

3. 本地仓库和远程仓库不匹配
-----------------------------

当你想推送一个本地仓库到远程的话，可能会出现本地仓库和远程仓库不一样的错误

我们只要执行以下命令就ok了

::

    git push -f ....

4. Git的HTTP/HTTPS缓冲区
---------------------------

Git的HTTP/HTTPS缓冲区默认大小是1MB。

在执行某些Git操作，特别是与大文件相关的操作时，可能会遇到需要调整缓冲区大小的情况。Git的HTTP/HTTPS缓冲区大小可以通过配置项http.postBuffer来设置。默认情况下，这个值通常被设置为较小的数值，比如1MB，这是为了减少内存消耗，特别是在处理大型文件或者大量数据时。然而，在实际使用中，如果经常遇到网络连接问题，或者是需要推送大文件，那么可能需要增加这个值以避免出现“remote end hung up unexpectedly”这类错误。

例如，如果在使用HTTP或HTTPS协议进行Git操作时，遇到了由于文件过大导致的传输失败，可以尝试增加http.postBuffer的值。通过命令git config --global http.postBuffer 524288000可以将缓冲区大小设置为500MB。这样做可以在一定程度上提高Git处理大文件的能力，减少因文件大小超出默认缓冲区限制而导致的问题。

需要注意的是，增加缓冲区大小会占用更多的内存资源，因此在使用完毕后，如果不希望一直保持较大的缓冲区设置，可以通过git config --unset http.postBuffer命令来取消设置，恢复到默认值。此外，如果是在团队环境中工作，建议与团队成员协调一致，避免因为个别成员的设置影响整个团队的Git操作效率。

::

    git config --global http.postBuffer 524288000


    这将把缓冲区大小设置为500MB，有助于解决大文件传输时的问题


要恢复默认设置，您可以使用以下命令：

::

    git config --global --unset http.postBuffer


- 50MB: 50 * 1024 * 1024 = 52428800 字节

- 100MB: 100 * 1024 * 1024 = 104857600 字节

- 150MB: 150 * 1024 * 1024 = 157286400 字节

- 200MB: 200 * 1024 * 1024 = 209715200 字节

- 300MB: 300 * 1024 * 1024 = 314572800 字节

- 500MB: 500 * 1024 * 1024 = 524288000 字节

5. 常用git用法
---------------

1. 先在git仓库网页上面创建一个仓库,在本机上面克隆这个仓库,正常使用，不用git config什么的麻烦

2. 想重新克隆一个大仓库的时候，使用 ``git clone https://xxx.com/xx/xx.git --depth=1`` 只克隆最新提交，减少下载空间


jujutsu(jj) 的使用
======================

jj 是一个git替代品

1. 下载
-------------

直接下载或者使用cargo

2. 使用
------------

1. 初始化仓库 

::

    jj git init

初始化当前目录作为仓库，使用git仓库，jujutsu的仓库还在开发

2. 查看仓库状态

::

    jj st

A:added M:modified D:deleted

按q来退出

3. 填写名字/邮箱

::

    jj config set --user.name "Your Name"
    jj config set --user user.email "YourEmail@mail.com"

4. 提交添加描述(description)

::

    jj describe -m "This is the first commit"

5. 打开pico编辑器查看description

::

    jj describe

没有pico编辑器会报错

6. 创建新的提交

jj 的提交信息包含两个ID,change ID 和 commit ID


::

    jj new

7. 查看提交信息

::

    jj log

8. 提交commit,but squash

::

    提交当前目录
    jj squash

    提交指定文件/目录
    jj squash /path/to/file




----


Man 手册的简单使用
=====================

1. 移动
--------

:k/j: 上下各一行的移动
:b/f,w/z: 上下各一面的移动
:u/d: 上下各半面的移动

2. 搜索
--------

:/: 向下搜索
:?: 向上搜索
:n: 向下定位到匹配行
:N: 向上定位到匹配行
:Esc-u: 关闭搜索匹配高亮
:/@: 从文件开头向下搜索
:?@: 从文件末行向上搜索

3. 跳转
--------

:g,<: 跳转到文件首行
:G,>: 跳转到文件末行
:p,%: 到文件开头
:t: 跳转到下一个标签
:T: 跳转到上一个标签
:m<letter>: 标记地点并记为<letter>
:'<letter>: 回到<letter>标记点
:''(两个单引号): 回到上一个地点
:ESC-m<letter>: 清除指定标记

.. note::
	设置标记的字符可以是大小写字母

	^和$为特殊标记，'^为跳转到文件开头，'$为跳转到文件末尾

----


Mpv 使用方法
=============

1. 播放目录下所有歌曲或者视频
------------------------------

mpv --playlist=/path/to/file

2. 单独播放歌曲或者视频
-----------------------

mpv /path/to/file

3. 播放时的快捷键
------------------

如果播放歌曲，没有GUI界面，可以使用快捷键来调整播放


<和>键
	下一首和上一首
Enter键
	下一首
p/SPACE键
	暂停播放
q键
	停止播放并退出
Q键
	停止播放并退出，但是重新打开文件将回到原来播放时退出的地方
/和*键,9和0键
	减少和增加音量
m键
	静音
l键
	设置A-B两个点，然后进行片段循环播放，再按l停止并清除此片段
L键
	单曲循环
小键盘左右方向键
	左减右加，每次5s
小键盘上下方向键
	上加下减，每次1min, 但是时长超过歌词时长将进入下一首歌曲
[和]键
	每次增加或者减少10%的歌曲播放速度，]加,[减
{和}键
	每次增加或者减少一倍的歌曲播放速度
Backspace键，退格键
	恢复默认播放速度

----


Tar 使用
==========

1. tar 实例
-----------



1.1 压缩例子
''''''''''''

1. **tar** (创建标准tar文件格式的归档文件)
::

    tar cvf archive.tar file1 file2

2. **tar.gz** (创建gzip压缩过的tar文件)
::

    tar zcvf archive.tar.gz file1 file2

3. **tar.bz2** (创建bzip2压缩过的tar文件)
::

    tar jcvf archive.tar.bz2 file1 file2

4. **tar.xz** (创建xz压缩过的tar文件)
::

    tar Jcvf archive.tar.xz file1 file2

5. **tar.Z** (创建compress压缩过的tar文件)
::

    tar Zcvf archive.tar.Z file1 file2

6. **tar.lz** (创建lzip压缩过的tar文件)
::

    tar cvf --lzip -f archive.tar.lz file1 file2

7. **tar.lz4** (创建lz4压缩过的tar文件)
::

    tar cvf --lz4 -f archive.tar.lz4 file1 file2

8. **tar.lzma** (创建lzma压缩过的tar文件)
::

    tar cvf --lzma -f archive.tar.lzma file1 file2

9. **tar.lzo** (创建lzo压缩过的tar文件)
::

    tar cvf --lzo -f archive.tar.lzo file1 file2

10. **tar.zst** (创建zstd压缩过的tar文件)
::

    tar cv --zstd -f archive.tar.zst file1 file2


1.2 解压例子
''''''''''''''

和压缩命令差不多，相当于把参数-c 换成-x,以下是一些例子。

:tar -jxvf archive.tar.bz2: 解压tar.bz2
:tar -Jxvf archive.tar.xz: 解压tar.xz
:tar -Zxvf archive.tar.Z: 解压tar.Z
:tar -xvf archive.tar: 解压tar
:unrar e archive.rar: 使用unrar解压rar
:7z x archive.7z: 使用7z解压文件


1.3 tar命令常用参数简述
''''''''''''''''''''''''

-c
    创建新的压缩文件
-x
    解压或提取压缩文件
-t
    显示压缩文件内容
-r
    向压缩文件追加文件
-u
    仅追加比压缩文件更新的文件
-f
    使用档案文件名
-v
    显示操作过程
-z
    通过gzip压缩或者解压
-j
    通过bzip2压缩或解压
-J
    通过xz压缩或解压
-Z
    通过compress压缩或解压
-C
    解压或者压缩到指定目录
--exclude
    排除某些文件
-k
    保留原有文件不覆盖
-numeric-owner
    仅使用数字表示user/group
--mtime
    设置时间戳
-P
    使用绝对路径
--checkpoint
    保存操作进度
--totals
    显示压缩详细信息





2. tar 选项
-----------

2.1 压缩选项
''''''''''''

-a, --auto-compress
    使用归档后缀名来决定压缩程序
-j, --bzip2
    通过 bzip2 过滤归档 
-J, --xz
    通过 xz 过滤归档
-z, --gzip, --gunzip, --ungzip
    通过 gzip 过滤归档
-Z, --compress, --uncompress
    通过 compress 过滤归档
--lzip
    通过 lzip 过滤归档
--lzma
    通过 xz 过滤归档
--lzop
    通过 lzop 过滤归档
--no-auto-compress    
    不使用归档后缀名来决定压缩程序
--zstd 
    通过 zstd 过滤归档


2.2 主操作模式
''''''''''''''

-A, --catenate, --concatenate  
    追加 tar 文件至归档
-c, --create 
    创建一个新归档
--delete      
    从归档(非磁带！)中删除
-d, --diff, --compare   
    找出归档和文件系统的差异
-r, --append       
    追加文件至归档结尾
--test-label  
    测试归档卷标并退出
-t, --list   
    列出归档内容
-u, --update  
    仅追加比归档中副本更新的文件
-x, --extract, --get 
    从归档中解出文件

2.3 提示性输出
''''''''''''''

-v, --verbose
    详细地列出处理的文件
-w, --interactive, --confirmation
    每次操作都要求确认

2.4 选择归档格式:
'''''''''''''''''

-H, --format=FORMAT
    创建指定格式的归档

FORMAT 是以下格式中的一种:

======                 ==================================
名字                     描述

======                 ==================================
gnu                      GNU tar 1.13.x 格式
oldgnu                   GNU 格式，其中 tar 版本 <= 1.12
pax                      POSIX 1003.1-2001 (pax) 格式
posix                    等同于 pax
ustar                    POSIX 1003.1-1988 (ustar) 格式
v7                       旧的 V7 tar 格式
======                 ==================================


2.5 选择输出流
'''''''''''''''

 -O, --to-stdout          
     解压文件至标准输出


2.6 设备选择和切换：
''''''''''''''''''''

-f, --file=ARCHIVE
    使用归档文件或 ARCHIVE 设备


2.7 操作文件属性
'''''''''''''''''

-m, --touch
    不要解压文件的修改时间


Screen
============

安装好screen后，直接执行screen,就启动了它

1. 快捷键
----------

===============     ========================================
快捷键              作用
===============     ========================================
Ctrl + a + c        创建一个新窗口(带shell)
Ctrl + a + n/p      切换到下/上一个会话
Ctrl + a + "        列出所有窗口
Ctrl + a + 0        切换到窗口0(按编号，但是得先创建)
Ctrl + a + A        重新命名当前窗口
Ctrl + a + S        当前区域水平分割为两个区域(不带shell)
Ctrl + a + |        当前区域垂直分割为两个区域(不带shell)
Ctrl + a + tab      将焦点切换到下一个区域
Ctrl + a 两次       切换到上一个区域
Ctrl + a + Q        关闭除了当前区域外的其他所有区域
Ctrl + a + X        关闭当前区域
Ctrl + a + x        锁定当前会话
Ctrl + a + d        从当前会话中分离出来
Ctrl + a + \        终止所有会话并关闭screen
Ctrl + a + ?        显示按键绑定
===============     ========================================

2. screen会话
--------------------

::

    screen -r   恢复screen会话
    screen -ls  列出当前运行的会话列表



Make&Makefile
==================

1. make 命令
-----------------

Make命令本身的命令行选项较多，这里只介绍在开发程序时最为常用的三个，它们是：

–k：
    如果使用该选项，即使make程序遇到错误也会继续向下运行；如果没有该选项，在遇到第一个错误时make程序马上就会停止，那么后面的错误情况就不得而知了。我们可以利用这个选项来查出所有有编译问题的源文件。

–n：
    该选项使make程序进入非执行模式，也就是说将原来应该执行的命令输出，而不是执行。

–f ：
    指定作为makefile的文件的名称。 如果不用该选项，那么make程序首先在当前目录查找名为makefile的文件，如果没有找到，它就会转而查找名为Makefile的文件。如果您在Linux下使用GNU Make的话，它会首先查找GNUmakefile，之后再搜索makefile和Makefile。按照惯例，许多Linux程序员使用Makefile，因为这样能使Makefile出现在目录中所有以小写字母命名的文件的前面。所以，最好不要使用GNUmakefile这一名称，因为它只适用于make程序的GNU版本。


2. Makefile文档编写
----------------------

主要结构：

::

	# 变量
	CC = gcc

	# 规则
	$(TARGET): $(OBJS)
			 $(CC) $(CFLAGS) -o $@ $(OBJS)

:前面指定要生成的文件(TARGET)，后面是需要的依赖(OBJS)，下一行指定行为规则，一般为编译或者链接，也可以是命令。TARGET 和 OBJS其中一个可以省略。

-----

示例
'''''

下面是一个简单的示例 Makefile，用于编译一个包含一个源文件的 C 语言程序：# Makefile示例

::

    # 定义编译器和编译选项
    CC = gcc
    CFLAGS = -Wall -Wextra

    # 定义目标文件名和依赖关系
    TARGET = myprogram
    SRCS = main.c
    OBJS = $(SRCS:.c=.o)

    # 默认目标
    all: $(TARGET)

    # 生成目标文件
    $(TARGET): $(OBJS)
        $(CC) $(CFLAGS) -o $@ $(OBJS)

    # 编译源文件为目标文件
    %.o: %.c
        $(CC) $(CFLAGS) -c $< -o $@

    # 清理生成的文件
    clean:
        $(RM) $(TARGET) $(OBJS)在同一目录下创建一个名为 Makefile 的文件，并将上面的内容复制到文件中。然后，在同一目录下创建一个名为 main.c 的源文件，其中包含你的 C 代码。现在你可以在命令行中运行 make 命令来编译你的程序，运行 ./myprogram 来执行它，或者运行 make clean 来清理生成的文件。


-----

让我们一步步来理解这个 Makefile。
''''''''''''''''''''''''''''''''''''''

1. **定义编译器和编译选项**：
''''''''''''''''''''''''''''''''''''''

::

    CC = gcc
    CFLAGS = -Wall -Wextra

- `CC` 定义了编译器为 `gcc`，也就是 GNU Compiler Collection

- `GS` 是编译选项，包括 `-Wall` 和 `-Wextra` ，它们告诉编译器显示所有警告信息。



-----


2. **定义目标文件名和依赖关系**：
''''''''''''''''''''''''''''''''''''''

::

	TARGET = myprogram
	SRCS = main.c
	OBJS = $(SRCS:.c=.o)

- `TARGET` 是目标文件的名称，即最终生成的可执行文件名为 `myprogram` 。
- `SRCS` 是源文件的名称，这里只有一个源文件 `main.c` 。
- `OBJS` 是由源文件编译而来的目标文件的列表，通过将 `.c` 替换为 `.o` 来生成。


-----

3. **默认目标**：
'''''''''''''''''''''''

::

	all: $(TARGET)

- `all` 是默认目标，也就是在运行 `make` 命令时将会执行的目标。在这里，它依赖于 `$(TARGET)` ，所以会先编译 `$(TARGET)` 。


-----

4. **生成目标文件**：
'''''''''''''''''''''''
::

   $(TARGET): $(OBJS)
       $(CC) $(CFLAGS) -o $@ $(OBJS)

- 这个规则告诉 Make 如何生成目标文件 `$(TARGET)` 。它依赖于 `$(OBJS)` ，然后使用 `gcc` 编译器将目标文件链接在一起生成最终的可执行文件。

-----

5. **编译源文件为目标文件**：
'''''''''''''''''''''''''''''''''

::

	%.o: %.c
	   $(CC) $(CFLAGS) -c $< -o $@

- 这个规则告诉 Make 如何将源文件编译为目标文件。`%.o` 表示所有的目标文件，`%.c` 表示对应的源文件。然后使用 `gcc` 编译器将源文件编译成目标文件。

- `-c` ：这是编译器选项，表示编译成目标文件而不是可执行文件。因为这里是将源文件编译成目标文件，所以使用 `-c` 选项告诉编译器只进行编译而不进行链接。

- `$<` ：这是一个自动变量，表示规则中的第一个依赖文件，即源文件。在这个模式规则中，它表示对应的源文件名。



- `%.o: %.c` ：这是规则的模式。`%.o` 表示匹配所有以 `.o` 结尾的目标文件，`%.c` 表示匹配对应的以 `.c` 结尾的源文件。

- `-o $@` : 这部分是链接器选项，它告诉链接器要生成一个输出文件，并指定输出文件的名称。`$@` 是一个特殊的变量，在 Make 中表示当前目标的名称。在这个例子中，`$@` 就是 `myprogram` ，因为它是我们目标文件的名字。`-o`  选项后面紧跟着的是输出文件的名称，即可执行文件的名称。


-----

6. **清理生成的文件**：
'''''''''''''''''''''''''

::

	clean:
	   $(RM) $(TARGET) $(OBJS)

- 这个规则定义了一个目标 `clean` ，它会删除生成的可执行文件和目标文件。`$(RM)` 是一个预定义的变量，用于执行删除操作。

这就是整个 Makefile 的结构和功能。它通过定义规则来告诉 Make 如何根据文件之间的依赖关系来构建目标文件。

Top
=====

内容说明：
------------

第一行：系统的运行时间和平均负载

第二行：当前运行的进程和线程数目

第三行：总体 CPU 使用率和各个核心的使用情况

第四行：总体内存使用情况、可用内存和缓存


- PID：进程的标识符。
- USER：运行进程的用户名。
- PR（优先级）：进程的优先级。
- NI（Nice值）：进程的优先级调整值。
- VIRT（虚拟内存）：进程使用的虚拟内存大小。 
- RES（常驻内存）：进程实际使用的物理内存大小。
- SHR（共享内存）：进程共享的内存大小。
- %CPU：进程占用 CPU 的使用率。
- %MEM：进程占用内存的使用率。
- TIME+：进程的累计 CPU 时间。

CPU 内容说明:
''''''''''''''''''

- top命令可以看到总体的系统运行状态和cpu的使用率 。
- 
- %us：表示用户空间程序的cpu使用率（没有通过nice调度）
- 
- %sy：表示系统空间的cpu使用率，主要是内核程序。
- 
- %ni：表示用户空间且通过nice调度过的程序的cpu使用率。
- 
- %id：空闲cpu
- 
- %wa：cpu运行时在等待io的时间
- 
- %hi：cpu处理硬中断的数量
- 
- %si：cpu处理软中断的数量
- 
- %st：被虚拟机偷走的cpu


参数说明：
------------

- -d <秒数>：指定 top 命令的刷新时间间隔，单位为秒。
- -n <次数>：指定 top 命令运行的次数后自动退出。
- -p <进程ID>：仅显示指定进程ID的信息。
- -u <用户名>：仅显示指定用户名的进程信息。
- -H：在进程信息中显示线程详细信息。
- -i：不显示闲置（idle）或无用的进程。
- -b：以批处理（batch）模式运行，直接将结果输出到文件。
- -c：显示完整的命令行而不截断。
- -S：累计显示进程的 CPU 使用时间。

sddm
===========

sddm是一个跨平台显示管理器

1. 安装

2. 配置

   - sddm配置文件通常位于 ``/etc/sddm.conf`` 或者 ``/etcsddm/sddm.conf`` ，可以设置主题、自动登录、界面语言等。

3. 启动

   - 在systemd下, ``sudo systemctl enable sddm``

4. 设置主题

::

    [Theme]
    Current=breeze

Steam Game Platform
======================

1. Use Flatpak
2. sudo flatpak remote-modify flathub --url=https://mirror.sjtu.edu.cn/flathub 换源
3. flatpak remotes  查看相关源
4. flatpak remote-delete <name> 删除源
5. 添加到.bashrc:export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:/home/zwron/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"
6. 通过flatpak下载steam:  flatpak --user install flathub com.valvesoftware.Steam
7. 启动steam:  flatpak run com.valvesoftware.Steam

吃鹅直通手册
=============

Linux 内核要求
--------------

内核版本
'''''''''

使用 ``uname -r`` 来查看内核版本。

.. note::
   如果你的内核版本低于 ``5.17`` ，可以参考 `Upgrade Guide <../en/user-guide/kernel-upgrade.md>`_ 升级你的内核。

绑定到 LAN 接口: >= 5.17
'''''''''''''''''''''''''''''''

如果你想作为路由器、网桥等中间设备，为其他设备提供代理服务，需要把 dae 绑定到 LAN 接口上。

该特性要求 dae 所在的设备的内核版本 >= 5.17。

如果你只在 ``lan_interface`` 中填写了接口，而未在 ``wan_interface`` 中填写内容，那么本地程序将无法被代理。如果你期望代理本地程序，需要在 ``wan_interface`` 中填写 ``auto`` 或是手动输入 WAN 接口。

绑定到 WAN 接口: >= 5.17
'''''''''''''''''''''''''''''''

如果你想为本地程序提供代理服务，需要把 dae 绑定到 WAN 接口上。

该特性要求 dae 所在的设备的内核版本 >= 5.17。

如果你只在 ``wan_interface`` 中填写了接口或 ``auto``，而未在 ``lan_interface`` 中填写内容，那么从局域网中传来的流量将无法被代理。如果你想同时代理本机和局域网流量，请同时填写 ``wan_interface`` 和 ``lan_interface`` 。

使用 trace 命令
'''''''''''''''''''''''''''''''

如果你想用 ``dae trace`` 命令来诊断网络连通性问题，所在的设备内核版本要求 >= 5.15。

内核配置选项
------------

通常，主流桌面发行版都会打开这些选项。但是为了减小内核大小，在嵌入式设备发行版（如 OpenWRT、Armbian 等）上这些选项可能处于关闭状态。使用以下命令在你的设备上显示内核配置选项：

.. code-block:: shell

    zcat /proc/config.gz || cat /boot/{config,config-$(uname -r)}

dae 需要以下内核选项：

::

    CONFIG_BPF=y
    CONFIG_BPF_SYSCALL=y
    CONFIG_BPF_JIT=y
    CONFIG_CGROUPS=y
    CONFIG_KPROBES=y
    CONFIG_NET_INGRESS=y
    CONFIG_NET_EGRESS=y
    CONFIG_NET_SCH_INGRESS=m
    CONFIG_NET_CLS_BPF=m
    CONFIG_NET_CLS_ACT=y
    CONFIG_BPF_STREAM_PARSER=y
    CONFIG_DEBUG_INFO=y
    # CONFIG_DEBUG_INFO_REDUCED is not set
    CONFIG_DEBUG_INFO_BTF=y
    CONFIG_KPROBE_EVENTS=y
    CONFIG_BPF_EVENTS=y

你可以通过以下命令检查他们：

bash和其他POSIX兼容的shell:

.. code-block:: shell

    (zcat /proc/config.gz || cat /boot/{config,config-$(uname -r)}) | grep -E 'CONFIG_(DEBUG_INFO|DEBUG_INFO_BTF|KPROBES|KPROBE_EVENTS|BPF|BPF_SYSCALL|BPF_JIT|BPF_STREAM_PARSER|NET_CLS_ACT|NET_SCH_INGRESS|NET_INGRESS|NET_EGRESS|NET_CLS_BPF|BPF_EVENTS|CGROUPS)=|# CONFIG_DEBUG_INFO_REDUCED is not set'

fish shell:

.. code-block:: fish

    begin; zcat /proc/config.gz || bat /boot/config "/boot/config-"(uname -r); end | grep -E 'CONFIG_(DEBUG_INFO|DEBUG_INFO_BTF|KPROBES|KPROBE_EVENTS|BPF|BPF_SYSCALL|BPF_JIT|BPF_STREAM_PARSER|NET_CLS_ACT|NET_SCH_INGRESS|NET_INGRESS|NET_EGRESS|NET_CLS_BPF|BPF_EVENTS|CGROUPS)=|# CONFIG_DEBUG_INFO_REDUCED is not set'

.. note::
    `Armbian` 用户可以参考 `Upgrade Guide <../en/user-guide/kernel-upgrade.md>`_ 升级到支持的内核。

    `Arch Linux ARM` 用户可以使用支持 dae 的 `linux-aarch64-7ji <https://github.com/7Ji-PKGBUILDs/linux-aarch64-7ji>`_ 内核。


使用
------

1.配置好文件，然后启动/重载服务

2.启动ip转发 

sudo vim /etc/sysctl.conf

文件内容如下:

.. code-block::

    net.ipv4.ip_forward = 1
    net.ipv6.conf.all.forwarding = 1

生效配置:

::

    sysctl -p


安装
----

Arch Linux / Manjaro
''''''''''''''''''''''''

dae 已发布于 `AUR <https://aur.archlinux.org/packages/dae>`_ 和 `archlinuxcn <https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/dae>`_ ，使用下述命令安装：

AUR
"""

最新稳定版 (针对 x86-64 v3 / AVX2 优化)

.. code-block:: shell

    [yay/paru] -S dae-avx2-bin

最新稳定版 (x86-64 或 aarch64 通用版)

.. code-block:: shell

    [yay/paru] -S dae

最新 Git 版

.. code-block:: shell

    [yay/paru] -S dae-git

archlinuxcn
"""""""""""

最新稳定版 (针对 x86-64 v3 / AVX2 优化)

.. code-block:: shell

    sudo pacman -S dae-avx2-bin

最新稳定版 (x86-64 或 aarch64 通用版)

.. code-block:: shell

    sudo pacman -S dae

最新 Git 版

.. code-block:: shell

    sudo pacman -S dae-git

安装后，使用 systemctl 对服务进行控制：

.. code-block:: shell

    # 启动 dae
    sudo systemctl start dae

    # 开机自动启动 dae
    sudo systemctl enable dae

Gentoo Linux
''''''''''''

dae 已发布于 `gentoo-zh <https://github.com/microcai/gentoo-zh>`_ ，可以使用 ``app-eselect/eselect-repository`` 启用此 overlay:

.. code-block:: shell

    eselect repository enable gentoo-zh
    emaint sync -r gentoo-zh
    emerge -a net-proxy/dae

Fedora
''''''

dae 已发布于 `Fedora Copr <https://copr.fedorainfracloud.org/coprs/zhullyb/v2rayA/package/dae>`_ 。

.. code-block:: shell

    sudo dnf copr enable zhullyb/v2rayA
    sudo dnf install dae

Alpine
''''''

详见 `run on alpine <../en/tutorials/run-on-alpine.md>`_ 。

macOS
'''''

我们提供了一种比较 hacky 的方式在 macOS 上运行 dae，见 `run on macOS <../en/tutorials/run-on-macos.md>`_ 。

Docker
''''''''''''''''''''

预编译镜像可相关文档请查阅：https://hub.docker.com/r/daeuniverse/dae。

作为替代，你也可以使用 ``docker compose``:

.. code-block:: shell

    git clone --depth=1 https://github.com/daeuniverse/dae
    docker compose up -d --build

手动安装
''''''''

.. note:: 这种方法仅建议高级用户使用。采用这种方法，用户可以灵活地测试各个版本的 dae。请注意，新引入的功能有时可能存在 bug，因此请自行承担风险。

dae 可以以守护进程（systemd）的形式运行，见 `run as daemon <../en/user-guide/run-as-daemon.md>`_

安装脚本
''''''''

见 `daeuniverse/dae-installer <https://github.com/daeuniverse/dae-installer>`_（或使用 `镜像站 <https://hubmirror.v2raya.org/daeuniverse/dae-installer>`_ ）。

手动构建
''''''''''''''''''''''''''''''''''''''''''

见 `Build Guide <../en/user-guide/build-by-yourself.md>`_ 。

最小 dae 配置
-------------

最小可启动的配置：

.. code-block:: shell

    global{}
    routing{}

然而，此配置使 dae 处于空载状态。如果你希望 dae 能正常工作，以下是较小配置下的最佳实践：

.. code-block:: shell

    global {
      # 绑定到 LAN 和/或 WAN 接口。将下述接口替换成你自己的接口名。
      #lan_interface: docker0
      wan_interface: auto # 使用 "auto" 自动侦测 WAN 接口。

      log_level: info
      allow_insecure: false
      auto_config_kernel_parameter: true
    }

    subscription {
      # 在下面填入你的订阅链接。
    }

    # 更多的 DNS 样例见 https://github.com/daeuniverse/dae/blob/main/docs/en/configuration/dns.md
    dns {
      upstream {
        googledns: 'tcp+udp://dns.google:53'
        alidns: 'udp://dns.alidns.com:53'
      }
      routing {
        request {
          qtype(https) -> reject
          fallback: alidns
        }
        response {
          upstream(googledns) -> accept
          ip(geoip:private) && !qname(geosite:cn) -> googledns
          fallback: accept
        }
      }
    }

    group {
      proxy {
        #filter: name(keyword: HK, keyword: SG)
        policy: min_moving_avg
      }
    }

    # 更多的 Routing 样例见 https://github.com/daeuniverse/dae/blob/main/docs/en/configuration/routing.md
    routing {
      pname(NetworkManager) -> direct
      dip(224.0.0.0/3, 'ff00::/8') -> direct

      ### 以下为自定义规则

      # 禁用 h3，因为它通常消耗很多 CPU 和内存资源
      l4proto(udp) && dport(443) -> block
      dip(geoip:private) -> direct
      dip(geoip:cn) -> direct
      domain(geosite:cn) -> direct

      fallback: proxy
    }

如果你不在乎极致速度，而是更注重隐私和 DNS 泄露，使用以下配置替换上述的 dns 部分：

.. code-block:: shell

    dns {
      upstream {
        googledns: 'tcp+udp://dns.google:53'
        alidns: 'udp://dns.alidns.com:53'
      }
      routing {
        request {
          qname(geosite:cn) -> alidns
          fallback: googledns
        }
      }
    }

完整样例：`example.dae <https://github.com/daeuniverse/dae/blob/main/example.dae>`_。

如果你使用 PVE，可以参考 `#37 <https://github.com/daeuniverse/dae/discussions/37>`_ 。

PPPoE
-----

如果希望代理 pppoe 接口, 请将 wan/lan_interface 设置为 pppd 生成的接口 (即 ppp0 / pppoe-wan) 而不是物理接口, 对于 wan 接口是 pppoe 的情况, 使用 auto 即可。

热重载和暂停
------------

当配置变化时，可以方便使用命令进行配置的热重载，在该过程中不会中断已有连接。当想暂停代理时，可使用命令进行暂停。

详见 `Reload and suspend <../en/user-guide/reload-and-suspend.md>`_ 。

错误排查
--------

详见 `Troubleshooting <../en/troubleshooting.md>`_ 。


zoxide
======================

现代化cd,可以使用权重记住常用路径，1w条 简化cd

::

    Test/
    └── file1
        └── subfile
            └── file2

zoxide add 加入路径到权重路径
zoxide query 查询权重路径
zoxide remove 删除权重路径
zoxide edit 修改权重路径文件


1. 查看权重: zoxide query -l -s | less
2. 如果已经被记录权重，可以使用简化路径: zoxide subfile file2 
   - 不区分大小写
   - file2 必须在 subfile里面，不能写file2 subfile
   - file2 必须写在最后，不然会进错
3. zi:通过使用fzf搜索权重进入目录

::

    eval "$(zoxide init --cmd cd bash)"
    设置每次打开终端自动启动zoxide并替换掉原始cd
