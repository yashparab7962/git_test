

#create list data type


sample=[1,2,3,4,5,6]
print(sample)


sample[1]=10

print(sample)


sample.append(10)
print(sample)


sample2=[]


sample3=[]

for x in sample:
    sample2.append(x)

print('sample2',sample2)

sample3=[x for x in sample if x%2==0]

print('Sample3',sample3)

print('Without Sort',sample)

sample.append(11)
sample.sort(reverse=True,)

print('with sort',sample)

list1=[1,2,3]
list2=[3,4,5]

print('Join List',list1+list2)

sample.clear()
print(sample)