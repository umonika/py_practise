from random import randint
num_list = []
for trk in  range(10):

    num_list.append(randint(1,10))
print('num_list',num_list)
even_odd_dict={}
for a_num in num_list:
    if a_num % 2 == 0:
        even_odd_dict[a_num] = "Even "
    else:
        even_odd_dict[a_num] = " Odd "

print("Even_Odd_Dict",even_odd_dict)
