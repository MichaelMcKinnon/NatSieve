from timeit import default_timer

# def bens_loop(lst):
#     replicate = False
    
#     for a in range(0, len(lst)):
#         for  b in range(a+1, len(lst)):
#             if lst[a] == lst[b]:
#                 replicate = True
#                 break
#     return replicate

#count natural numbers trhat don't have duplicate digits
max_num = 10000000000
#max_num = 100000000
max_num = 10000000
cnt = 0
i = 0
time_start = default_timer()

while i < max_num:
    lst = [x for x in str(i)]    #convert integer into list of integers
    if len(set(lst)) == len(lst): #check that the list of integers is unique
        cnt += 1
    else:
        #print(i)
        next
    i+=1
time_delta = default_timer() - time_start
print(cnt,time_delta)

# #Do it again with Ben's collision loop
# cnt = 0
# i = 0
# time_start = default_timer()

# while i < max_num:
#     lst = [x for x in str(i)]    #convert integer into list of integers
#     if not bens_loop(lst): #check that the list of integers is unique
#         cnt += 1
#     i+=1
# time_delta = default_timer() - time_start
# print(cnt,time_delta)