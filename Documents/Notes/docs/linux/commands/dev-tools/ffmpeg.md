# ffmpeg 命令详解

## 一句话理解 ffmpeg

ffmpeg 是音视频处理工具，可以**转换格式、剪辑、合并、压缩**视频音频。

```bash
# 格式转换
ffmpeg -i input.mp4 output.avi

# 压缩视频
ffmpeg -i input.mp4 -b:v 1M output.mp4

# 提取音频
ffmpeg -i video.mp4 -vn audio.mp3
```

## 最常用场景

### 1. 格式转换

```bash
# 视频格式转换
ffmpeg -i input.mkv output.mp4
ffmpeg -i input.avi output.mp4
ffmpeg -i input.webm output.mp4

# 音频格式转换
ffmpeg -i input.wav output.mp3
ffmpeg -i input.flac output.mp3
ffmpeg -i input.ogg output.mp3

# 只转换封装格式（不重新编码，速度快）
ffmpeg -i input.mp4 -c copy output.mkv
```

### 2. 压缩视频

```bash
# 按比特率压缩（1Mbps）
ffmpeg -i input.mp4 -b:v 1M output.mp4

# 按 CRF 压缩（18-28，越小质量越好，23为默认）
ffmpeg -i input.mp4 -crf 23 output.mp4

# 压缩并调整分辨率
ffmpeg -i input.mp4 -b:v 1M -vf scale=1280:720 output.mp4
```

### 3. 剪辑视频

```bash
# 从第30秒开始剪10秒
ffmpeg -i input.mp4 -ss 00:00:30 -t 00:00:10 -c copy output.mp4

# 从第30秒到第40秒
ffmpeg -i input.mp4 -ss 00:00:30 -to 00:00:40 -c copy output.mp4

# 精确剪辑（重新编码，慢但精确）
ffmpeg -i input.mp4 -ss 00:00:30 -t 00:00:10 output.mp4
```

### 4. 提取音频

```bash
# 提取为 MP3
ffmpeg -i video.mp4 -vn -acodec mp3 audio.mp3

# 提取为 AAC
ffmpeg -i video.mp4 -vn -acodec aac audio.aac

# 提取原始音频流（不编码）
ffmpeg -i video.mp4 -vn -c copy audio.aac
```

### 5. 合并文件

```bash
# 先创建列表文件 list.txt
# file '1.mp4'
# file '2.mp4'
# file '3.mp4'

# 合并
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4
```

## 核心参数

| 参数 | 说明 | 例子 |
|------|------|------|
| `-i` | 输入文件 | `-i input.mp4` |
| `-c` | 编解码器 | `-c copy`（复制不重编码） |
| `-c:v` | 视频编解码器 | `-c:v libx264` |
| `-c:a` | 音频编解码器 | `-c:a aac` |
| `-b:v` | 视频比特率 | `-b:v 1M` |
| `-b:a` | 音频比特率 | `-b:a 128k` |
| `-crf` | 视频质量（0-51，越小越好） | `-crf 23` |
| `-r` | 帧率 | `-r 30` |
| `-s` | 分辨率 | `-s 1920x1080` |
| `-vf` | 视频滤镜 | `-vf scale=1280:720` |
| `-ss` | 开始时间 | `-ss 00:01:30` |
| `-t` | 持续时间 | `-t 00:00:10` |
| `-to` | 结束时间 | `-to 00:01:40` |
| `-vn` | 不包含视频 | 提取音频时用 |
| `-an` | 不包含音频 | 提取视频时用 |
| `-y` | 覆盖输出文件 | `-y output.mp4` |

## 实际例子

### 视频处理

```bash
# 压缩手机视频（常用）
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -c:a aac -b:a 128k output.mp4

# 调整分辨率到1080p
ffmpeg -i input.mp4 -vf scale=1920:1080 output.mp4

# 保持比例调整宽度（高度自动）
ffmpeg -i input.mp4 -vf scale=1280:-1 output.mp4

# 裁剪视频画面（从(100,100)开始取500x400区域）
ffmpeg -i input.mp4 -vf crop=500:400:100:100 output.mp4

# 旋转90度
ffmpeg -i input.mp4 -vf transpose=1 output.mp4

# 加速2倍
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" output.mp4

# 减速0.5倍
ffmpeg -i input.mp4 -vf "setpts=2.0*PTS" output.mp4
```

### 音频处理

```bash
# 调整音量（2倍）
ffmpeg -i input.mp3 -af "volume=2.0" output.mp3

# 截取音频片段
ffmpeg -i input.mp3 -ss 00:01:00 -t 00:00:30 output.mp3

# 合并多个音频
ffmpeg -i "concat:1.mp3|2.mp3|3.mp3" -c copy output.mp3

# 降低比特率（减小文件）
ffmpeg -i input.mp3 -b:a 64k output.mp3

# 转换为单声道
ffmpeg -i input.mp3 -ac 1 output.mp3
```

### GIF 制作

```bash
# 视频转 GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=320:-1" output.gif

# 指定时间段转 GIF
ffmpeg -i input.mp4 -ss 00:00:05 -t 00:00:03 -vf "fps=10,scale=320:-1" output.gif
```

### 截图

```bash
# 每隔10秒截一帧
ffmpeg -i input.mp4 -vf fps=1/10 screenshot-%03d.png

# 截取第30秒的画面
ffmpeg -i input.mp4 -ss 00:00:30 -vframes 1 thumbnail.jpg

# 高质量截图
ffmpeg -i input.mp4 -ss 00:00:30 -vframes 1 -q:v 2 thumbnail.jpg
```

## 常用编码格式

| 格式 | 视频编码 | 音频编码 | 说明 |
|------|----------|----------|------|
| MP4 | H.264 (libx264) | AAC | 最通用 |
| MKV | H.264/H.265 | AAC/MP3 | 封装灵活 |
| AVI | mpeg4 | mp3 | 旧格式 |
| MOV | H.264 | AAC | Apple 格式 |
| WebM | VP9 | Opus | 网页用 |

```bash
# H.265/HEVC 压缩率更高（更小）
ffmpeg -i input.mp4 -c:v libx265 -crf 28 output.mp4

# VP9 编码（网页用）
ffmpeg -i input.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 output.webm
```

## 查看信息

```bash
# 查看视频信息
ffmpeg -i input.mp4

# 更详细的信息
ffprobe input.mp4

# 只显示关键信息
ffprobe -v quiet -show_format input.mp4

# 显示视频流信息
ffprobe -v quiet -select_streams v -show_streams input.mp4
```

## 批量处理

```bash
# 批量转换 mp4 为 avi
for i in *.mp4; do
    ffmpeg -i "$i" "${i%.mp4}.avi"
done

# 批量压缩所有 mp4
for i in *.mp4; do
    ffmpeg -i "$i" -c:v libx264 -crf 23 -c:a aac "compressed_$i"
done

# 并行处理（GNU parallel）
parallel ffmpeg -i {} -c:v libx264 -crf 23 {.}.mp4 ::: *.avi
```

## 常用组合速查

| 目的 | 命令 |
|------|------|
| MP4 转 AVI | `ffmpeg -i input.mp4 output.avi` |
| 压缩 MP4 | `ffmpeg -i input.mp4 -crf 23 output.mp4` |
| 剪视频片段 | `ffmpeg -i input.mp4 -ss 00:01:00 -t 00:00:30 -c copy output.mp4` |
| 提取音频 | `ffmpeg -i video.mp4 -vn -acodec mp3 audio.mp3` |
| 视频截图 | `ffmpeg -i video.mp4 -ss 00:00:30 -vframes 1 thumb.jpg` |
| 合并视频 | `ffmpeg -f concat -i list.txt -c copy output.mp4` |
| 调整分辨率 | `ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4` |
| 降低音频比特率 | `ffmpeg -i input.mp3 -b:a 64k output.mp3` |
| 视频转 GIF | `ffmpeg -i input.mp4 -vf fps=10,scale=320:-1 output.gif` |

## 快捷别名

```bash
# 添加到 .bashrc
alias ffcompress='ffmpeg -i "$1" -c:v libx264 -crf 23 -c:a aac -b:a 128k "${1%.*}_compressed.mp4"'
alias ffcut='ffmpeg -i "$1" -ss "$2" -t "$3" -c copy "${1%.*}_cut.mp4"'
alias ffinfo='ffprobe -v quiet -show_format'

# 使用
ffcompress video.mp4
ffcut video.mp4 00:01:30 00:00:10
ffinfo video.mp4
```

## 一句话总结

ffmpeg 核心：`-i` 指定输入，`-c copy` 快速复制流，`-crf 23` 平衡质量和大小，`-ss` 和 `-t` 剪辑。最常用是压缩：`ffmpeg -i input.mp4 -crf 23 output.mp4`。
