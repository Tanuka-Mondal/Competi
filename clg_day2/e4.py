def change_list(list11):
    list10.append(20)
    list11.append(30)
    print("list inside function: ",list10)

list10 = [10,30,40,50]
list11 = [11,31,41,51]

change_list(list11)
print("list outside function = ",list11)
