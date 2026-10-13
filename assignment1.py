#Fibinacci Series
lim=int(input("Enter the limit:"))
first_num=0
sec_num=1
result=0
i = 1
# print(first_num)
# print(sec_num)
while i<lim+1: #or i<lim-1 (if firstnum & 2ndnum prints seperately)
    result=first_num+sec_num
    print(first_num) 
    first_num=sec_num
    sec_num=result
    i+=1

    




    