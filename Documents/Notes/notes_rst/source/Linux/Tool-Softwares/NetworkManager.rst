.. Author:       fajknli
.. Email:        fajknli@gmail.com
.. Created Time: 2026-04-07 15:03

另外，我感觉我使用nmcli con up .... 连接我的手机热点似乎有点不稳定，老是自己断开或者其他问题

- NetworkManager 默认开启 WiFi 省电模式，会导致连接间歇性断开

::

    sudo iw dev wlan0 get power_save
    # 如果显示 "Power save: on"，那就是问题所在

临时关闭（立即生效，重启后失效）

::

    sudo iw dev wlan0 set power_save off

针对特定连接关闭

::

    # 将 "Your_Hotspot_SSID" 替换为你的热点名称
    nmcli connection modify "Your_Hotspot_SSID" wifi.powersave 2
    nmcli connection up "Your_Hotspot_SSID"

全局关闭

::

    sudo mkdir -p /etc/NetworkManager/conf.d
    sudo tee /etc/NetworkManager/conf.d/wifi-powersave.conf <<EOF
    [connection]
    wifi.powersave = 2
    EOF
    sudo systemctl restart NetworkManager
