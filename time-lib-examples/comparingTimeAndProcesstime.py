import time
from time import process_time as my_timer
from time import time as actual_time
import random

input("press enter to start")

start_process_time = my_timer()
start_time = actual_time()
input("press enter to stop")
result = 1
for i in range(1, 100000):
    if(i==50000):
        time.sleep(5)
    result *= i
end_process_time = my_timer()
end_time = actual_time()

print("process started at " + time.strftime("%X",time.localtime(start_process_time)))
print("actually started at " + time.strftime("%X",time.localtime(start_time)))
print("process ended at " + time.strftime("%X",time.localtime(end_process_time)))
print("actually ended at " + time.strftime("%X",time.localtime(end_time)))

print("computer process time was {} seconds".format(end_process_time - start_process_time ))
print("actual time taken was {} seconds".format(end_time - start_time ))