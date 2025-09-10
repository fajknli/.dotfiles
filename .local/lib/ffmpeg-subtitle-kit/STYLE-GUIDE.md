<!--
  Author:       fajknli
  Email:        fajknli@gmail.com
  Created Time: 2025-09-05 15:44
  Filename:     STYLE-GUIDE.md
-->


# FFmpeg 字幕样式参数速查手册

## 🎯 最常用参数

### 1. 字体 & 大小
- `FontName=Microsoft YaHei` (微软雅黑，最通用)
- `FontName=Source Han Sans SC` (思源黑体)
- `FontSize=24` (正常大小)
- `FontSize=32` (较大，适合手机)

### 2. 颜色 (PrimaryColour)
- 白色: `&H00FFFFFF`
- 黄色: `&H0000FFFF` 
- 红色: `&H000000FF`
- 格式: `&H00BBGGRR` (AA=透明度, BB=蓝, GG=绿, RR=红)

### 3. 位置 (Alignment)
- `1`=底部左, `2`=底部中, `3`=底部右
- `4`=中部左, `5`=中部中, `6`=中部右  
- `7`=顶部左, `8`=顶部中, `9`=顶部右
- `10`=居中 (有些版本FFmpeg支持)

### 4. 边距 (MarginV)
- 当 Alignment=2 (底部中): `MarginV=50` (距离底部50像素)
- 当 Alignment=8 (顶部中): `MarginV=50` (距离顶部50像素)

## ⚙️ 效果参数
- `BorderStyle=3` (必须为3)
- `Outline=1` (描边粗细，1-4)
- `Shadow=0` (阴影深度，0-4)
- `BackColour=&H80000000` (半透明背景，让文字更清晰)

## 🧩 预设组合示例

### 底部通用字幕
`FontName=Microsoft YaHei,FontSize=24,PrimaryColour=&H00FFFFFF,BorderStyle=3,Outline=1,Alignment=2,MarginV=20`

### 顶部标题
`FontName=Microsoft YaHei,FontSize=28,PrimaryColour=&H00FFFFFF,BorderStyle=3,Outline=1,Alignment=8,MarginV=30`
