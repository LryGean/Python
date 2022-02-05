# 匹配模式（re的第三个模式参数）
import re
language = 'PythonC#\nJavaPHP'

# 小写无法匹配
# r = re.findall('c#',language)

# 多个模式用 | 隔开
# re.I：忽略大小写匹配
# r = re.findall('c#.{1}',language,re.I)
# 结果：[]

# re.S：表示可以包含\n的匹配 
r = re.findall('c#.{1}',language,re.I | re.S)

print(r)