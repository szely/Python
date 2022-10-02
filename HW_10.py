# Реализуйте алгоритм перемешивания списка.

my_list_1 = [1,2,3,3,9,434,234,123]
my_list_2 = [3,4,5,8,6,2,3,3,3,123]
new_list = my_list_1+my_list_2
new_list = list(set(new_list))
print(new_list)