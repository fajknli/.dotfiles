#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-24 03:49


from huggingface_hub import snapshot_download

snapshot_download(
        "intfloat/multilingual-e5-large"
        )
