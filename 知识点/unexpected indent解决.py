#异常
"""
unexpected indent/unindent does not match any outer indentation level
"""
#1、代码前后缩进量不一致
class abc():
    """error"""
     def __init__(self):
         pass
"""
def前面有红色小波浪线，说明出现了缩进错误
"""
#2 代码前后缩进符号不一致
"""
用tab缩进和用空格键混合缩进可能出错
"""