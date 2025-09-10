my_list = [993, 22, 911, 2, 11, 13, 52, 124, 4, 1,
           "beer", "potato", "pc", "dog", "nigga",
           "freak", "fashion", "amy", "mirrors", "drive"]
int_list = []
str_list = []
for x in my_list:
    if type(x) == int:
        int_list.append(x)
    else:
        str_list.append(x)
int_list.sort()
str_list.sort()
sorted_list = int_list.copy()
sorted_list.extend(str_list)
even_list = [x for x in int_list if x % 2 == 0]
upper_str_list = [x.upper() for x in str_list]
print("main list:", my_list)
print("sort list:", sorted_list)
print("number list:", even_list)
print("up list:", upper_str_list)