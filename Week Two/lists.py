my_List = []
my_List.append(10)
my_List.append(20)
my_List.append(30)
my_List.append(40)
my_List.insert(1, 15)
other_list = [50, 60, 70]
my_List.extend(other_list)
my_List.remove(40)
my_List.sort()
print(my_List.index(30))
print(my_List)