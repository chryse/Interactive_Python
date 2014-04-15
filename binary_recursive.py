import random

range_num = 100
list_num = []
for i in range(0, range_num+1):
    list_num.append(i)
    
secret_num = random.randint(0, 100)
max_num = list_num[len(list_num)-1]
min_num = list_num[0] 

#print list_num
print "secret number is ", secret_num

def binary_search(list_num, secret_num, min_num, max_num):
    # test if array is
    if max_num < min_num:
    # set is empty, so return value showing not found
        return "KEY_NOT_FOUND"
    
    else:
        # calculate midpoint to cut set in half
        mid_num = (max_num + min_num) // 2
        
        print "middle numbler is ", mid_num
        
        # three-way comparison
        if mid_num > secret_num:
            # key is in lower subset
            return binary_search(list_num, secret_num, min_num, mid_num-1);
        elif (list_num[mid_num] < secret_num):
            # key is in upper subset
            return binary_search(list_num, secret_num, mid_num+1, max_num);
        else:
            # key has been found
            print "found number is ", mid_num
            return mid_num;

    
print binary_search(list_num, secret_num, min_num, max_num)
