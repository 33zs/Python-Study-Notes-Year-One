#n的阶乘
def factorial(n): #base case
    if n==0 or n==1:
        return 1
#recursive call else:
    return n * factorial(n - 1)
print(factorial(4))

#计算列表元素的和
def practical9_ex1(nums):
    #base case, directly solavable
    if len(nums) == 1:
        return nums[0]
    else:
        #recursive call
        return nums[0] + practical9_ex1(nums[1:])
#test
l = [10,20,30,40,50]
print(practical9_ex1(l))

#斐波那契数
def practical9_ex2(n):
    #sequence
    #base case, directly solavable
    if n == 1 or n == 2:
        return 1
    else:
        #recursive call
        return (practical9_ex2(n - 1) + (practical9_ex2(n - 2)))
#test
n = 10
print(practical9_ex2(n))

#加和每个数位上的数字
#1
def practical9_ex3(n):
    #base case, directly solavable
    if n == 0:
        return 0
    else:
        #recursive call
        #here we remove bases etc. and get the whole integers added
        return n % 10 + practical9_ex3(int(n / 10))
#test
n = 912
print(practical9_ex3(n))

#2
def r(n):
    b=str(n)
    if len(str(n))==1:
        return n
    return int(b[0])+int(r((str(n))[1:]))
print(r(18))

#算a的b次方
def practical9_ex4(a,b):
    #base cases
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    #end of base cases
    else:
        #recursive call
        return a * practical9_ex4(a,b - 1)
#test
c=3
d=3 print(practical9_ex4(c,d))