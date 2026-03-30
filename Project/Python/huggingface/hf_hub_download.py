#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-24 03:40


from huggingface_hub import hf_hub_download

file_path = hf_hub_download(
        repo_id="intfloat/multilingual-e5-large",
        filename="config.json"
        )

print(f"文件已下载到：{file_path}")
