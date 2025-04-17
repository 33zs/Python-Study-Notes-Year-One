#format 用法
#1 无参数
print('{}{}'.format('hello','world'))
#2 有参数索引
print('{0}{1}'.format('hello','world'))
#3 有参数索引
print('{1}{0}{1}'.format('hello','world'))
#4 有参数key
print('id:{id},name:{name}'.format(id='001',name='hello'))
#5  列表为参数
list=['001','hello']
print('id:{List[0]},name:{List[1]}'.format(List=list))
print('id:{0[0]},name:{0[1]}'.format(list))
#6 字典为参数
dict={'id':'001','name':'hello'}
print(dict)
print(f'id:{id},name:{name}'.format(**dict))
#7 类为参数
class value():
    id='001'
    name='hello'
print(f'id:{Value.id},name{Value.name}'.format(Value=value))
#8 *args,**kwargs为参数
args=[',','.']
kwargs={'id':'001','name':'hello'}
print('id:{id}{}name:{name}{}'.format(*args,**kwargs))
