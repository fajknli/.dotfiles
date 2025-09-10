#!/bin/sh

case "$1" in
    start)
        time=$(date +'%Y-%m-%d_%H-%M-%S')
        save_dir="$HOME/Videos/screen_records"
        audio_device=$(pactl list short sources | grep monitor | grep RUNNING | awk '{print $2}')
        mkdir -p "$save_dir"
        wf-recorder -f "$save_dir/record_$time.mp4" \
            -c h264_vaapi \
            -d /dev/dri/renderD128 \
            -a"$audio_device" \
            -p "qp=18" \
            -B 60 > /tmp/record.log 2>&1 &
        echo "$!" > /tmp/wf-record.pid
        #echo "录制开始，PID: $!"
        notify-send -u low "录制开始，PID: $!"
        ;;

    stop)
        if [ -f /tmp/wf-record.pid ]; then
            pid=$(cat /tmp/wf-record.pid)
            kill $(cat /tmp/wf-record.pid)
            rm /tmp/wf-record.pid
            notify-send -u low "停止录制 (PID: $pid)"
        else
            #echo "没有正在进行的录制"
            notify-send -u low "没有正在进行的录制"
        fi
        ;;

    *)
        echo "用法: $0 {start|stop}"
        ;;

esac
