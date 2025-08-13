.. Author:       fajknli
.. Email:        fajknli@gmail.com
.. Created Time: 2025-08-12 11:56
.. Filename:     http-code-number.rst


HTTP 状态码大全
#################

1. 常见

200	    OK	        正常访问网页或 API

301     永久重定向	网站换域名

302	    临时重定向	登录后跳转

304	    未修改	    浏览器缓存有效

400	    请求错误	API 参数缺失

401	    未授权	    未登录访问受限资源

403	    禁止访问	无权限访问

404	    不存在	    页面删除或 URL 错误

500	    服务器错误	后端代码崩溃

502	    网关错误	后端服务宕机


HTTP 状态码是服务器对客户端请求的响应代码，由三位数字组成，第一位数字定义了响应类别。以下是主要的 HTTP 状态码分类和常见状态码：

1xx - 信息性状态码（Informational）
表示请求已被接收，需要继续处理

- 100 Continue - 客户端应继续发送请求
 
- 101 Switching Protocols - 服务器同意切换协议（如升级到WebSocket）
 
- 102 Processing - 服务器已收到请求但尚未完成处理
 
- 103 Early Hints - 用于预加载资源

2xx - 成功状态码（Success）
表示请求已成功被服务器接收、理解并接受

- 200 OK - 请求成功
 
- 201 Created - 资源创建成功（常用于POST请求）
 
- 202 Accepted - 请求已接受但尚未处理完成
 
- 203 Non-Authoritative Information - 返回的元信息来自副本
 
- 204 No Content - 请求成功但无内容返回
 
- 205 Reset Content - 请求成功，客户端应重置文档视图
 
- 206 Partial Content - 服务器返回部分内容（用于分块下载或断点续传）
 
- 207 Multi-Status - 多状态响应（WebDAV）
 
- 208 Already Reported - 成员已报告（WebDAV）

3xx - 重定向状态码（Redirection）
表示需要客户端采取进一步的操作才能完成请求

- 300 Multiple Choices - 多种选择（资源有多种表示）
 
- 301 Moved Permanently - 资源已永久移动到新位置
 
- 302 Found - 资源临时移动到新位置
 
- 303 See Other - 查看其他位置（应使用GET方法访问）
 
- 304 Not Modified - 资源未修改（缓存相关）
 
- 305 Use Proxy - 必须通过代理访问（已废弃）
 
- 307 Temporary Redirect - 临时重定向（保持方法不变）
 
- 308 Permanent Redirect - 永久重定向（保持方法不变）

4xx - 客户端错误状态码（Client Error）
表示客户端可能出错，妨碍了服务器的处理

- 400 Bad Request - 请求语法错误
 
- 401 Unauthorized - 需要身份验证
 
- 402 Payment Required - 保留状态码
 
- 403 Forbidden - 服务器拒绝请求
 
- 404 Not Found - 资源不存在

- 405 Method Not Allowed - 请求方法不被允许

- 406 Not Acceptable - 无法满足客户端要求的格式

- 407 Proxy Authentication Required - 需要代理认证

- 408 Request Timeout - 请求超时

- 409 Conflict - 请求与当前资源状态冲突

- 410 Gone - 资源已永久删除

- 411 Length Required - 需要Content-Length头

- 412 Precondition Failed - 前提条件失败

- 413 Payload Too Large - 请求实体过大

- 414 URI Too Long - 请求URI过长

- 415 Unsupported Media Type - 不支持的媒体类型

- 416 Range Not Satisfiable - 请求范围不符合要求

- 417 Expectation Failed - 无法满足Expect请求头

- 418 I'm a teapot - 愚人节玩笑代码

- 421 Misdirected Request - 请求被发送到错误的服务器

- 422 Unprocessable Entity - 请求格式正确但语义错误（WebDAV）

- 423 Locked - 资源被锁定（WebDAV）

- 424 Failed Dependency - 依赖操作失败（WebDAV）

- 425 Too Early - 服务器不愿冒险处理可能重放的请求

- 426 Upgrade Required - 客户端应升级协议
 
- 428 Precondition Required - 需要条件请求
 
- 429 Too Many Requests - 请求过于频繁（限速）
 
- 431 Request Header Fields Too Large - 请求头字段过大
 
- 451 Unavailable For Legal Reasons - 因法律原因不可用

5xx - 服务器错误状态码（Server Error）
表示服务器在处理请求时发生错误

- 500 Internal Server Error - 服务器内部错误
 
- 501 Not Implemented - 服务器不支持请求的功能

- 502 Bad Gateway - 网关或代理服务器收到无效响应

- 503 Service Unavailable - 服务不可用（临时过载或维护）

- 504 Gateway Timeout - 网关超时

- 505 HTTP Version Not Supported - 不支持的HTTP版本

- 506 Variant Also Negotiates - 服务器存在内部配置错误

- 507 Insufficient Storage - 存储空间不足（WebDAV）

- 508 Loop Detected - 检测到无限循环（WebDAV）

- 510 Not Extended - 需要进一步扩展请求

- 511 Network Authentication Required - 需要网络认证

这些状态码可以帮助开发者快速诊断和解决HTTP请求中的问题。在实际开发中，200、301、302、304、400、401、403、404、500、502、503等状态码最为常见。
