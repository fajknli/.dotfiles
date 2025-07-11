Debian安装和配置
############################



1. Download image
=================

1.1 Debain镜像下载
-------------------

`Debian官网 <https://www.debian.org>`_

:download:`网络安装版下载 <https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.2.0-amd64-netinst.iso>`

1.2 Debian最小化安装
----------------------


1. 正常流程安装但是不要连网，到最后一步选择安装的软件时，只选择最后一个基础软件安装

#. 由于刚刚接触Debian不了解，一直找不到wifi网络工具,命令行里找不到nmcli,wpa_cli,什么的，其实debian有wpa_cli,只不过是在/sbin/wpa_cli,
   但是不能使用，即使开了 ``systemctl start wpa_supplicant`` 所以，就准备使用 ``wpa_supplicant`` 来手动连接

#. 第一步是通过 ``wpa_passphrase`` 来生成wifi的ssid和密码，保存到一个文件里，例如： ``/etc/wpa_supplicant.conf``

::

 wpa_passphrase hwifi 12345678

结果如下：

::

        zwron@localhost:~$ wpa_passphrase hwifi 12345678
        network={
                ssid="hwifi"
                #psk="12345678"
                psk=6ad6bc2f37b913e17ecc84155b4174144f19321fd37f6cc6cf07f08a0e9d3c9e
        }



然后删除或者注释下面那个加密的psk,再把第二个psk什么的给取消注释,如下：

::

        network={
                ssid="hwifi"
                psk="12345678"
                #psk=6ad6bc2f37b913e17ecc84155b4174144f19321fd37f6cc6cf07f08a0e9d3c9e
        }

保存后再使用 ``wpa_supplicant`` 进行连接:

::

        /sbin/wpa_supplicant -i wlp1s0 -c /etc/wpa_supplicant.conf


这个情况下按Ctrl + Alt + F2 进入tty2登陆然后执行 ``sudo dhclient <interface>`` 获取ip后，就可以联网


.. note::
   ``wpa_supplicant -i`` 连接网络需要网络接口，使用 ``ip address`` 查看wlan网卡名
  


Debian换源
----------

安装成功而且网络配置成功后，配置源：

我使用 `USTC源 <https://mirrors.ustc.edu.cn/help/debian.html>`_

编辑 /etc/apt/sources.list 文件（需要使用 sudo）。以下是 Debian unstable 参考配置内容：

::

        deb http://mirrors.ustc.edu.cn/debian unstable main contrib non-free non-free-firmware



Debian 命令
===============

:系统索引更新: sudo apt updae
:查看可更新的软件包: sudo apt list --upgradable
:安装可更新软件包: sudo apt upgrade
:安装全部可更新软件包: sudo apt full-upgrade
:修复失败依赖安装: sudo apt --fix-broken install
:安装新软件包: sudo apt install
:搜索软件包: sudo search
:卸载软件包: sudo remove
:删除软件包: sudo purge
:删除剩余无用软件包依赖: sudo apt autoremove
:清理软件包缓存: sudo apt clean
                  
:显示软件包信息: sudo apt-cache show
:显示软件包版本信息: sudo apt-cache policy
:下载软件包而不安装: sudo apt download
:Debian软件包仓库网站: packages.debian.org

:手动安装.deb格式的第三方包: dpkg -i
:查找已经安装的包: dpkg -l
:查看系统所以已安装软件包: dpkg -get-selections

