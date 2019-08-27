# import time
# start_time = time.time()
# main()
# print("--- %s seconds ---" % (time.time() - start_time))
import random
# a = int(input("enter your no: "))
# n = 0
# for i in range (a+1):
#     n = n*10+i
# print(n)
str1 = str(input("enter your first word: "))
str2 = str(input("enter your second word: "))
if len(str1)==len(str2):
    # list1 = list(str1)
    # list2 = list(str2)
    # print(list1)
    # print(list2)
    #  my code
    # n = True
    # while n ==True:
    #     random.shuffle(list2)
    #     if list1==list2:
    #         print(" same")
    #         n = False

    # phanis code

    list1 = list(str1)
    list2 = list(str2)
    c = 0
    for i in list1:
        if i in list2:
            c+=1
            pass
        else:
            print(" not same")
            break
    if c == len(str1):
        print ("same")

    # malini's code
    
    # list1 = sorted(str1)
    # list2 = sorted(str2)
    # if list1 == list2:
    #     print("same")
    # else:
    #     print("not same")

else:
    print("both are not ")