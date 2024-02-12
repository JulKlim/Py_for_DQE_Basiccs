# the list of random numbers from 0 to 1000
list_of_numbers = [428, 674, 152, 385, 571, 98, 482, 728, 845, 239, 761, 340, 845, 589, 426, 218, 743, 553, 830, 41,
                   762, 432, 970, 608, 2, 105, 561, 124, 46, 319, 654, 828, 829, 526, 663, 359, 520, 127, 166, 890,
                   998, 911, 932, 0, 212, 732, 300, 468, 594, 10, 972, 235, 565, 20, 380, 207, 977, 321, 396, 361,
                   874, 446, 989, 89, 843, 587, 891, 318, 5, 380, 242, 427, 566, 430, 376, 593, 727, 897, 903, 657,
                   593, 984, 237, 917, 332, 898, 620, 702, 974, 606, 313, 501, 788, 727, 38, 926, 527, 104, 843, 511, 152]

# the loop for iterating over the list of numbers by their index
for i in range(len(list_of_numbers)-1):
    # the loop for iteration over the list of numbers to check if each of the number is bigger or smaller its neighbour
    for j in range (len(list_of_numbers)-1):
        # checking if the number is bigger then the next number
        if list_of_numbers[j]>list_of_numbers[j+1]:
            # if the number is bigger then the next number they exchange their places in the list
            list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1],list_of_numbers[j]

# creating variables with inital value 0 for sums of even and odd numbers as well as for theit total count in the list
sum_of_even = sum_of_odd = count_of_even_numbers = count_of_odd_numbers = 0

# the loop for iterating each number in the sorted list of numbers
for k in (list_of_numbers):
    # checking if the number is even
    if k%2==0:
        # adding the even number to the sum of even numbers
        sum_of_even+=k
        # adding + 1 to the total count of even numbers
        count_of_even_numbers = count_of_even_numbers + 1
    # the logic which will take place for the odd numbers
    else:
        # adding the odd number to the sum of odd numbers
        sum_of_odd+=k
        # adding + 1 to the total count of odd numbers
        count_of_odd_numbers = count_of_odd_numbers + 1
# creating variable for average for even numbers
average_for_even_numbers = sum_of_even/count_of_even_numbers
# creating variable for avarage for odd numbers
average_for_odd_numbers = sum_of_odd/count_of_odd_numbers

# printing the average numbers of both even and odd numbers
print("Average for even numbers = ", average_for_even_numbers, "Average for odd numbers = ", average_for_odd_numbers)
