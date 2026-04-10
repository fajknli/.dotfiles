# HTTP 状态码大全

## 常见状态码

| 状态码 | 含义 | 说明 |
|--------|------|------|
| 200 | OK | 正常访问网页或 API |
| 301 | 永久重定向 | 网站换域名 |
| 302 | 临时重定向 | 登录后跳转 |
| 304 | 未修改 | 浏览器缓存有效 |
| 400 | 请求错误 | API 参数缺失 |
| 401 | 未授权 | 未登录访问受限资源 |
| 403 | 禁止访问 | 无权限访问 |
| 404 | 不存在 | 页面删除或 URL 错误 |
| 500 | 服务器错误 | 后端代码崩溃 |
| 502 | 网关错误 | 后端服务宕机 |

## 1xx - 信息性状态码

| 状态码 | 含义 |
|--------|------|
| 100 | Continue - 客户端应继续发送请求 |
| 101 | Switching Protocols - 服务器同意切换协议 |
| 102 | Processing - 服务器已收到请求但尚未完成 |
| 103 | Early Hints - 用于预加载资源 |

## 2xx - 成功状态码

| 状态码 | 含义 |
|--------|------|
| 200 | OK - 请求成功 |
| 201 | Created - 资源创建成功 |
| 202 | Accepted - 请求已接受但未处理完成 |
| 203 | Non-Authoritative Information - 元信息来自副本 |
| 204 | No Content - 请求成功但无内容返回 |
| 205 | Reset Content - 客户端应重置文档视图 |
| 206 | Partial Content - 返回部分内容（断点续传） |
| 207 | Multi-Status - 多状态响应（WebDAV） |
| 208 | Already Reported - 成员已报告（WebDAV） |

## 3xx - 重定向状态码

| 状态码 | 含义 |
|--------|------|
| 300 | Multiple Choices - 多种选择 |
| 301 | Moved Permanently - 永久移动到新位置 |
| 302 | Found - 临时移动到新位置 |
| 303 | See Other - 应使用 GET 访问 |
| 304 | Not Modified - 资源未修改（缓存） |
| 307 | Temporary Redirect - 临时重定向（保持方法） |
| 308 | Permanent Redirect - 永久重定向（保持方法） |

## 4xx - 客户端错误状态码

| 状态码 | 含义 |
|--------|------|
| 400 | Bad Request - 请求语法错误 |
| 401 | Unauthorized - 需要身份验证 |
| 402 | Payment Required - 保留状态码 |
| 403 | Forbidden - 服务器拒绝请求 |
| 404 | Not Found - 资源不存在 |
| 405 | Method Not Allowed - 请求方法不被允许 |
| 406 | Not Acceptable - 无法满足要求的格式 |
| 407 | Proxy Authentication Required - 需要代理认证 |
| 408 | Request Timeout - 请求超时 |
| 409 | Conflict - 与当前资源状态冲突 |
| 410 | Gone - 资源已永久删除 |
| 411 | Length Required - 需要 Content-Length |
| 412 | Precondition Failed - 前提条件失败 |
| 413 | Payload Too Large - 请求实体过大 |
| 414 | URI Too Long - 请求 URI 过长 |
| 415 | Unsupported Media Type - 不支持的媒体类型 |
| 416 | Range Not Satisfiable - 请求范围不符合要求 |
| 418 | I'm a teapot - 愚人节玩笑 |
| 421 | Misdirected Request - 请求发送到错误服务器 |
| 422 | Unprocessable Entity - 语义错误（WebDAV） |
| 423 | Locked - 资源被锁定（WebDAV） |
| 426 | Upgrade Required - 客户端应升级协议 |
| 428 | Precondition Required - 需要条件请求 |
| 429 | Too Many Requests - 请求过于频繁 |
| 431 | Request Header Fields Too Large - 请求头字段过大 |
| 451 | Unavailable For Legal Reasons - 因法律原因不可用 |

## 5xx - 服务器错误状态码

| 状态码 | 含义 |
|--------|------|
| 500 | Internal Server Error - 服务器内部错误 |
| 501 | Not Implemented - 不支持请求的功能 |
| 502 | Bad Gateway - 网关收到无效响应 |
| 503 | Service Unavailable - 服务不可用 |
| 504 | Gateway Timeout - 网关超时 |
| 505 | HTTP Version Not Supported - 不支持的 HTTP 版本 |
| 506 | Variant Also Negotiates - 内部配置错误 |
| 507 | Insufficient Storage - 存储空间不足（WebDAV） |
| 508 | Loop Detected - 检测到无限循环（WebDAV） |
| 510 | Not Extended - 需要进一步扩展 |
| 511 | Network Authentication Required - 需要网络认证 |

## 一句话总结

最常见的状态码：200（成功）、301/302（重定向）、304（缓存）、400（请求错误）、401（未授权）、403（禁止）、404（不存在）、500（服务器错误）、502/503（服务不可用）。调试 API 时先看状态码定位问题。
