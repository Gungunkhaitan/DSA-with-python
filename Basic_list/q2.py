list1=[1,4,2.5,'a','b',6,3,6.6]
new_list=[]
for i in list1:
    if type(i) is int:
        new_list.append(i)
for i in new_list:
      print(i,end=', ') 
print("\n")