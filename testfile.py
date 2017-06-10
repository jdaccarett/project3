import time

#this file will run all testcases needed.

#import prims implementation
from tps_mst_prims import mst_prims

print("\n")
#Test-Input-1.txt
start = time.clock()
mst_prims('test-input-1.txt')
elapsed_time = (time.clock() - start)
print('Running Algo tps_mst_prims:')
print("File: test-input-1.txt: ")
print("Time: ", elapsed_time)

print("\n__________________________\n")

#Test-Input-2.txt
start = time.clock()
mst_prims('test-input-2.txt')
elapsed_time = (time.clock() - start)
print('Running Algo tps_mst_prims:')
print("File: test-input-2.txt: ")
print("Time: ", elapsed_time)


