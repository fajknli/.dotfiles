#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-13 17:22


you_words="$1"
OPENROUTER_API_KEY="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"

temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT


# 流式输出处理
echo "AI 正在生成回答..."

xh --stream POST https://openrouter.ai/api/v1/chat/completions \
    Content-Type:application/json \
    Authorization:"Bearer $OPENROUTER_API_KEY" \
    model="deepseek/deepseek-chat-v3.1:free" \
    messages:='[{"role": "user", "content": "'"$you_words"'"}]' \
    stream:=true 2>/dev/null | \
while IFS= read -r line; do
    [ -z "$line" ] && continue
    [ "$line" = "data: ping" ] && continue

    # 使用case语句处理数据行
    case "$line" in
        data:*)
            data="${line#data: }"
            [ "$data" = "[DONE]" ] && break

            content=$(echo "$data" | jq -r '.choices[0].delta.content? // empty' 2>/dev/null)
            if [ -n "$content" ]; then
                # 追加到文件
                printf "%s" "$content" >> "$temp_file"

            fi
            ;;
    esac
done

glow "$temp_file" 2>/dev/null
