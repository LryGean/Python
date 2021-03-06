# 1.服务器渲染：在服务器那边直接把数据和html整合在一起，同一返回给浏览器
# 在页面源代码中能看到数据。 例如：在百度里搜索周杰伦
# 2.客户端渲染：
#   第一次请求只要一个html骨架，第二次浏览器执行脚本进行第二次请求拿到数据，进行数据展示
#   特点：在页面源代码中，看不到数据

# 熟悉使用浏览器抓包工具


# HTTP协议

# 请求头中的一些重要内容（爬虫需要）：
# 1.User-Agent:请求载体的身份标识（用啥发送的请求）  **************
# 2.Referer:防盗链（这次请求是从哪各页面来的？反爬会用到）
# 3.cookie:本地字符串数据信息（用户登录信息，反爬会用到）

# 响应头中一些重要的内容：
# 1.cookie:本地字符串数据信息（用户登录信息，反爬会用到）
# 2.各种神奇的莫名其妙的字符串（这个需要经验了，一般都是token字样，防止各种攻击和反爬）


# 请求方式：
#   GET:显示提交
#   POST:隐示提交