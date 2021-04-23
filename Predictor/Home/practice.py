# a = 'mayur'
# print(a,'is my name')
# delete : remove,pop clear is not possible in string
# fetcing is possible
# change is not possible

# a = 'mayur is my name is is is sis sis is '
# b=a.rstrip()
# print(a.rstrip())
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.split(' '))
# print(a.split('is'))
# # print(a.replace('is','are',10))
# lst=['1','2','3']
# lst1 = '@'.join(lst)
# print(lst1)
#types of operators
#arithmatic operator--->+,-,*%,/\
#assignment operator
#relational operator
#unary operator
# print(2+3)
# A=2
# print(type(A))
# print(float(A))
# print(int(5%3))
# a=1*5/(2+3)(BODMAS:- B = [],{},(),O=X^2,ROOT OF 2,D OR M : DIVIDE OR MULTIPLICATION,A OR S:- ADD OR SUBSTRACT)
# p

#relational operator :- >,<,>=,<=,==,!=
#Logical operator : And,Or and  not
# a=3
# b=4
# if a>b:
#     print()
### list
# lst = [1,2,3,[1,4,5],(10,2,3),'nandan',{11,2,13}]
# lst[4]=list(lst[4])
# lst[4][1]=20
# print(lst)
# print(lst)#list is mutable
# lst[4]=list(lst[4])
# lst[4][1]=20
# print(lst)
# lst.append(103)
# print(lst)
# b=(1,2,3)
# lst.append(b)
# print(lst)
# lst.extend([5,6,7,4])
# print(lst)
# lst.remove(5)
# print(lst)
# del lst
# lst.reverse()
# print(lst)
# c[1]=20
# print(c)
# d=tuple(c)
# print(d)
# print(lst)
# # indexing in list
# print(lst[0])
#indexing starts from 0 f to n-1 left to right and -1 to -n from right to left
#we can change value of list cause list is mutable
# method of list is
#1st is indexing
# print(lst[1])
# a = lst[1]
# print(a)
# by using slicing we get multiple element or items at one time
# for reverse order you want to write list
# b= lst[::-1]
# print(b)
# lst = [1,2,3,4]
# b= tuple(lst)
# print(b)
# tup = (1,2,3,4,'my')
# print(tup[1])
# print(type(tup))
# tup1 = list(tup)
# print(tup1)
# tup1[1]=3
# print(tup1)
# print(tuple(tup1))
# t=tup1.count(3)
# print(t)
#dictionary
# dic = {1:'mayur',2:'ronak','mayur':[1,2,3],4:{5:6,6:7}}
# dic['mayur']='keval'
# dic[5]={1,2}
# print(dic)
# print(dic.keys())
# print(dic.values())
# print(dic.items())
a=[1,2,3,4]
b=[5,4,3,2]
c=dict(zip(a,b))
print(c)
# dic = dict({1:2,2:3})
# print(dic)
# dic1 = dict([(1,'mayur'),(2,'ram')])
# print(dic1)