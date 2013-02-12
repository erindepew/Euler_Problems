__author__ = 'Erin Depew'

'''
Euler Problem #1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

def mult_of_num ( range , num ):
    '''
    (int, int) -> list of ints

    return a list of all the multiples of num given the range of range

    '''

    count = 0
    list = []

    while (count < range):
        if (count % num == 0):
            list.append(count)
        count = count + 1

    return list

def sum_lists (list1, list2):
    '''
    (list, list) -> int

    takes two lists, removes duplicate numbers and returns the sum of the two lists

    '''

    sum_list = []

    merge_list = list1 + list2;
    sum_list = list(set(merge_list));
    return sum(sum_list)


five_list = mult_of_num(1000, 5)

three_list = mult_of_num(1000,3)

print sum_lists(five_list , three_list)





