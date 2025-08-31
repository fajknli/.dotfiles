.. Author:       fajknli
.. Email:        fajknli@gmail.com
.. Created Time: 2025-08-15 22:15
.. Filename:     one-line-command.rst


one line command
#####################

server-client
'''''''''''''''

::

    rsync -avz -e "ssh -p 26059" frp_0.64.0_linux_amd.tar.gz root@119.188.232.23:/root/

    -a : keep file infomations
    -v : verbose
    -z : press transfor
    -e : spcify port for server

::

    scp -P 26059 frp_0.64.0_linux_amd.tar.gz root@119.188.232.23:/root/

::

    sftp -P 26059 root@119.188.232.23

    # interactive mod
    put frp_0.64.0_linux_amd.tar.gz /root/
    exit

::

    cat frp_0.64.0_linux_amd64.tar.gz | ssh -p 26059 root@119.188.232.23 "cat > /root/frp_0.64.0_linux_amd64.tar.gz"
