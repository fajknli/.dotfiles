Linux-Tricks
##############

1. 使用ntp调整时间
===================

1. 下载 ntp 

::

	xbps-install ntp

2. 启动ntp 服务

::

	ln -s /etc/sv/ntpd /var/service/

3. 找一个合适的ntp服务器

::

	cn.ntp.org.cn #中国
	edu.ntp.org.cn #中国教育网
	ntp1.aliyun.com #阿里云
	ntp2.aliyun.com #阿里云
	cn.pool.ntp.org #最常用的国内NTP服务器

4. 使用ntpdate根据提供的ntp服务器，调整时间

::

	sudo ntpdate cn.pool.ntp.org

5. 硬件时钟问题，重启后无法正确保持时间，可以尝试同步硬件时钟和系统时钟

::

	sudo hwclock --systohc

2. Compress and Decompress
============================

Compress
------------



Decompress
------------------


.gz File
'''''''''''''

1. gzip -d <file>


.zip File
'''''''''''''

1. unzip <file>

3. keybinding 
================

::

    xkbcli interactive-wayland

4. Screen capturing
========================

1.wf-recorder

wf-recorder -f example.mp4

5. Check Hardwork Info
========================

1. check GPU type

::

    lspci -k | grep -A 2 VGA

2. did installed VA-API drive

::

   vainfo 

3. user groups

::

    sudo usermod -aG video,input $(whoami)
    sudo chmod 660 /dev/dri/renderD*
