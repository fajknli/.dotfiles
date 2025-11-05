#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-13 14:36

you_words="$1"
#OPENROUTER_API_KEY="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"
OPENROUTER_API_KEY="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"

# 获取响应并通过glow渲染
response=$(xh POST https://openrouter.ai/api/v1/chat/completions \
  Content-Type:application/json \
  Authorization:"Bearer $OPENROUTER_API_KEY" \
  model="deepseek/deepseek-chat-v3.1:free" \
  messages:='[{"role": "user", "content": "'"$you_words"'", "stream": true}]' | \
jq -r '.choices[0].message.content')

# 使用glow渲染Markdown
echo "$response" | glow -
