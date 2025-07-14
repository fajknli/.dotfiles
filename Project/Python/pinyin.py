#!/user/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-07-07 00:10
# Filename:     pinyin.py


from pypinyin import lazy_pinyin

with open("china_city2", "r", encoding="utf-8") as f:
    text = f.read()

pinyin = "".join(lazy_pinyin(text))

with open("city2", "w", encoding="utf-8") as f:
    f.write(pinyin)
