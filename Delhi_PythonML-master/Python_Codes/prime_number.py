# num = 29
# prime = False
# for i in range(2,num):
#     if num % i == 0:
#         prime = False
#         break
#     else:
#         prime = True
#
# if prime:
#     print("Number is prime")
# else:
#     print("Number is not prime")

# num = 23
#
# for i in range(2, num):
#     if (num % i) == 0:
#         print("not Prime")
#         break
# else:
#     print("prime")


min_num=int(input("Enter Min. Number : "))
max_num=int(input("Enter Max. Number : "))
for num in range (min_num, max_num):
    for i in range(2, num):
        if (num % i)==0:
            break
    else:
        print(num)
