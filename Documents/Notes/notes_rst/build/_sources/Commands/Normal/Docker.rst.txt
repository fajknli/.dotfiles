Docker For beginner
#######################

1. 命令
===============

1. 安装docker

``docker --version``

2. 运行你的第一个容器

::

    docker run hello-world

3. 查看已下载的镜像

::

    docker images

删除镜像

::

    docker rmi images

4. 运行一个交互式容器

::

    docker run -it alpine sh


*-it：这两个选项是让容器可以交互式运行的,其中 -i 是“保持标准输入开启”，-t 是“分配一个伪终端”*
*sh :这告诉容器启动一个 Bash shell*

5. 退出容器

::

    exit

6. 查看当前运行的容器

::

    docker ps

5. 查看所有容器（包括已经停止的容器)

::

    docker ps -a


2. Dockerfile
=================

1. 创建一个新目录，进入它： 

::

    mkdir my-docker-test
    cd my-docker-test

2. 创建一个叫 Dockerfile 的文件，内容如下：

::

    FROM alpine
    RUN apt update && apt install -y cowsay
    CMD ["cowsay", "Hello from my custom Docker image!"]






