import itertools
import functools
list1=[1,2,3,4]
print(list(itertools.accumulate(list1,lambda a,b:a+b)))
print(functools.reduce(lambda a,b:a+b,list1))


lis = [2,1,7,3,4,3]
for i in range(len(lis)):
    for j in range(0, len(lis)-i-1):
        if(lis[j] > lis[j+1]):
            lis[j], lis[j+1] = lis[j+1], lis[j]

print(lis)