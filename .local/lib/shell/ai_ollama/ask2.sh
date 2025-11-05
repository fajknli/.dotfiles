#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-13 17:22


#!/bin/bash

you_words="$1"
OPENROUTER_API_KEY="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"
term_prompt=$(cat << 'EOF'
你是一个终端输出优化专家。请使用ANSI颜色代码格式化回答：

格式规范：
- 主标题: \033[1;36m粗体青色\033[0m
- 子标题: \033[1;35m粗体紫色\033[0m
- 重要内容: \033[1;33m粗体黄色\033[0m
- 代码/命令: \033[36m青色\033[0m
- 列表项: \033[32m绿色\033[0m
- 错误警告: \033[31m红色\033[0m

请直接输出带ANSI代码的文本，不要使用Markdown语法。
EOF
)

# 流式输出处理
echo "🤖 正在生成回答..."
echo "========================================"

xh --stream POST https://openrouter.ai/api/v1/chat/completions \
    Content-Type:application/json \
    Authorization:"Bearer $OPENROUTER_API_KEY" \
    model="deepseek/deepseek-chat-v3.1:free" \
    messages:='[
        {"role": "user", "content": "'"$you_words"'", "stream": true}
        {"role": "system", "content": "'"$term_prompt"'", "stream": true}
        ]' \
    stream:=true 2>/dev/null | \
while IFS= read -r line; do
    [ -z "$line" ] && continue
    [[ "$line" == "data: ping" ]] && continue

    if [[ "$line" == data:* ]]; then
        data="${line#data: }"
        [[ "$data" == "[DONE]" ]] && break

        content=$(echo "$data" | jq -r '.choices[0].delta.content? // empty' 2>/dev/null)
        [ -n "$content" ] && printf "%s" "$content"
    fi
done

echo -e "\n========================================"
echo "✅ 完成"
