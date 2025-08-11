my_list=[]
items_to_add=[10,20,30,40]
for item in items_to_add:
    my_list.append(item)
my_list.insert(1,15)
my_list.extend([50,60,70])
my_list.pop(-1)
my_list.sort()
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")

