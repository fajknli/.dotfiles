Software_install
############################################


1. 代理软件
===========

1. v2rayA
----------

**下载:**

::

        sudo sh -c "$(wget -qO- https://hubmirror.v2raya.org/v2rayA/v2rayA-installer/raw/main/installer.sh)" @ --with-v2ray

**使用:**

::



        Commands:
        Start v2rayA service now:
        systemctl start v2raya
        Start v2rayA service at system boot:
        systemctl enable v2raya
        --------------------------------------------------------------------------------
        1. v2rayA has been installed to your system, the configuration directory is
           /usr/local/etc/v2raya.
        2. v2rayA will not start automatically, you can start it by yourself.
        3. If you want to uninstall v2rayA, please run uninstaller.sh.
        4. If you want to update v2rayA, please run installer.sh again.
        5. Official website: https://v2raya.org.
        6. If you forget your password, run "v2raya-reset-password" to reset it.
        --------------------------------------------------------------------------------


----------

2. 输入法软件
=============

1. fcitx5
----------

**下载:**

各大软件管理器下载：

- fcitx5

- fcitx5-chinese-addons




**使用:**

打开 ``fcitx5-configtool`` 然后查找并选择pinyin

使用 ``Ctrl + Shift + F`` 切换中文简体和繁体

把fcitx5配置加到环境变量里:

编辑 ``/etc/environment`` 并添加以下几行，然后重新登录

::

        GTK_IM_MODULE=fcitx
        QT_IM_MODULE=fcitx
        XMODIFIERS=@im=fcitx
        SDL_IM_MODULE=fcitx
        GLFW_IM_MODULE=ibus

更多详细关于fcitx5的内容可以查看 `ArchWiki的fcitx5介绍 <https://wiki.archlinuxcn.org/wiki/Fcitx5#>`_



3. 通讯软件
===========

1. QQ
------

**下载:**

`QQ官网下载 <https://im.qq.com/linuxqq/index.shtml>`_,可以下载debian包，然后使用 ``sudo dpkg -i <包名>`` 

或者，在其他发行版上的包管理器上找，例如Arch

或者直接使用 ``Appimage``

**使用:**

Debian 自定义包安装：

::

        sudo dpkg -i <包名>

Debina 自定义包删除：

::

        sudo dpkg -r linuxqq


4. 办公软件 
==============

1. WPS
-------

**下载:**

`WPS官网下载 <https://www.wps.com/office/linux/>`_


**使用:**

Debian 下:

::

        sudo dpkg -i <包名>

        sudo dpkg -r wps-office

.. note::
   目前最新版本为11.1.0,这个版本下的wps,在粗体字显示方面有bug,可以通过以下方法解决。

   下载 https://mirrors.ustc.edu.cn/debian/pool/main/f/freetype/libfreetype6_2.12.1%2Bdfsg-5_amd64.deb
   然后 用 dpkg -i 安装它就可以解决此问题。


