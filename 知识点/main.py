#python文件有两种使用方法
"""
1、直接作为脚本执行
2、import到其他的python脚本中被调用执行，也就是作为模块被导入执行
"""
#理解__name__=="__main__"
"""
假如你叫小明.py,在你朋友眼中，你是小明（__main__=="小明"）
在你自己眼中，你是你自己（__name__=="__main__"）
"""
"""
当.py文件被直接运行时，if__name__=="_main_"之下的代码块将被运行
当.py文件以模块形式被导入时，if__name__=="__main__"之下的代码块不被运行
"""
#原理
"""
param.py中执行print(__name__)
输出__main__
在calculate.py中执行
输出param
__name__=="__main__"条件为假，所以无法执行后面的代码
