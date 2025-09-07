.. Author:       fajknli
.. Email:        fajknli@gmail.com
.. Created Time: 2025-08-06 18:25
.. Filename:     Proxy.rst


Proxy Setting
###################

1. dae
=========




2. reverse proxy
=================

1. frp
----------

version: frp_0.64.0_linux_amd64

usage:

::

    # for server
    frps -c frps.toml

    # for client
    frpc -c frpc.toml

config file:

- frps.toml

::

    bindPort = <server_open_port_for_frp>

- frpc.toml

::

    serverAddr = "<server_ip>"
    serverPort = <remote_server_open_port_for_frp>

    [[proxies]]
    name = "<your_server_name>"
    type = "tcp"
    localIP = "127.0.0.1"
    localPort = <local_server_open_port>
    remotePort = <remote_server_open_another_free_port>


frp persistent server
----------------------

systemctl daemon `/etc/systemd/system/frps.service`

::

    [Unit]
    Description = frps for minecraft
    After = network.target syslog.target
    Wants = network.target

    [Service]
    Type = simple
    Restart = always
    RestartSec = 3s
    ExecStart = frps -c /root/frps.toml

    [Install]
    WantedBy = multi-user.target

usage:

::

    systemctl daemon-reload
    systemctl status frps
    systemctl start frps
    systemctl stop frps
    systemctl restart frps
