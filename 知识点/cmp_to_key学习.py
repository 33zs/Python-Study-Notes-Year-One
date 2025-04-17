"""
在Python中，cmp_to_key是一个函数，它用于将一个比较函数（接受两个参数并返回一个整数值）转换为一个关键字函数（接受单个参数并返回一个可排序的键）。它通常用于排序算法中，例如sorted()和list.sort()函数。

在Python 2中，list.sort()和sorted()函数接受一个cmp参数，用于指定比较函数。
但在Python 3中，cmp参数已被移除。相反，这些函数现在接受一个key参数，该参数指定一个用于从每个元素中提取排序键的函数。因此，如果您有一个比较函数并且希望将其用作key参数，则可以使用cmp_to_key函数。
"""
"""
返回1代表相反
返回-1代表保持
"""
#cmp_to_key函数接受一个比较函数作为参数，并返回一个关键字函数。例如，假设有一个比较函数：

def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

#您可以使用cmp_to_key函数将其转换为关键字函数：


from functools import cmp_to_key

key_func = cmp_to_key(compare)

#现在，您可以将key_func作为sorted()和list.sort()函数的key参数使用。例如，假设有一个列表：


my_list = [5, 1, 3, 2, 4]
#1
sorted_list = sorted(my_list, key=key_func)

#2
my_list.sort(key=key_func)

#有优先级的比较
#before
listC=[[3,3,"AAAA"],[4,4,"aa11"],[3,3,"aaa"],[3,3,"111bb"],[4,1,"aa"]]
#after
# listC=[[3,3,"aaa"],[3,3,"AAAA"],[3,3,"111bb"],[4,1,"aa"],[4,4,"aa11"]]
from functools import cmp_to_key
def cmp(x,y):
    if x[0]!=y[0]:
        return x[0]-y[0]
    elif x[1]!=y[1]:
        return x[1]-y[1]    #若结果为负数，则保持不变，按照降序排序，若结果为正数，则相反，还是按照降序排序
    elif x[2]>y[2]:          #表示以x>y的顺序升序排序
        return -1
    else:
        return 1
listCS=sorted(listC,key=cmp_to_key(cmp))
print(listCS)

#运用类的方法
class node:
    def __init__(self,val1,val2,val3):
        self.val1=val1
        self.val2=val2
        self.val3=val3
    def __lt__(self, other):
        if self.val1!=other.val1:
            return self.val1<other.val1
        elif self.val2!=other.val2:
            return self.val2<other.val2
        elif self.val3>other.val3:
            return True
        else:
            return False
    def __repr__(self):
        return "["+str(self.val1)+","+str(self.val2)+","+self.val3+"]"
listC=[]
nodeA=node(3,3, 'AAAA')
listC.append(nodeA)
nodeA=node(4, 4, 'aa11')
listC.append(nodeA)
nodeA=node(3, 3, 'aaa')
listC.append(nodeA)
nodeA=node(3, 3, '111bb')
listC.append(nodeA)
nodeA=node(4, 1, 'aa')
listC.append(nodeA)
listCS=sorted(listC) print(listCS)