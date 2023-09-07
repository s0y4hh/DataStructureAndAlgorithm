import time

#A sample function whose time taken to be measured
def fun():
    count1 = 0
    count2 = 0
    count3 = 0
    n = 100 #value to be changed
    for i in range(0, n):
        j = 1
        while j<n:
            count1 += 1
            count2 += 1
            count3 += 1
            print(count1, end = '')
            print(" ", end = '')
            print(count2, end = '')
            print(" ", end = '')
            print(count3, end = '')
            print("\n", end = '')

            j*=2

    for i in range(0, n):
        count1 += 1
        count2 += 1
        count3 += 1
        print(count1, end = '')
        print(" ", end = '')
        print(count2, end = '')
        print(" ", end = '')
        print(count3, end = '')
        print("\n", end = '')

            
# get the start time
st = time.time()

# main program
fun()

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')