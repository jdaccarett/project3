import time

#this file will run all testcases needed.

#import prims implementation
from tps_mst_prims import mst_prims

#import hungarian implementation
from hungarian import hungarian

print("\n")

#tsp_example_1.txt
start = time.clock()
mst_prims('tsp_example_1.txt')
elapsed_time = (time.clock() - start)
print('Running Algo tps_mst_prims:')
print("File: tsp_example_1.txt: ")
print("Time: ", elapsed_time)

print("\n__________________________\n")

#tsp_example_2.txt
start = time.clock()
mst_prims('tsp_example_2.txt')
elapsed_time = (time.clock() - start)
print('Running Algo tps_mst_prims:')
print("File: tsp_example_2.txt: ")
print("Time: ", elapsed_time)

print("\n__________________________\n")

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

print("\n__________________________\n")

#Test-Input-3.txt
start = time.clock()
mst_prims('test-input-3.txt')
elapsed_time = (time.clock() - start)
print('Running Algo tps_mst_prims:')
print("File: test-input-3.txt: ")
print("Time: ", elapsed_time)
print("\n__________________________\n")

#Test-Input-4.txt
start = time.clock()
hungarian('test-input-4')
elapsed_time = (time.clock() - start)
print('Running Algo Hungarian:')
print("File: test-input-4: ")
print("Time: ", elapsed_time)
print("\n__________________________\n")

#Test-Input-5.txt
start = time.clock()
fast('test-input-5')
elapsed_time = (time.clock() - start)
print('Running Algo Fast:')
print("File: test-input-5: ")
print("Time: ", elapsed_time)
print("\n__________________________\n")

#Test-Input-6.txt
start = time.clock()
fast('test-input-6')
elapsed_time = (time.clock() - start)
print('Running Algo Fast:')
print("File: test-input-6: ")
print("Time: ", elapsed_time)
print("\n__________________________\n")

#Test-Input-7.txt
start = time.clock()
fast('test-input-7')
elapsed_time = (time.clock() - start)
print('Running Algo Fast:')
print("File: test-input-7: ")
print("Time: ", elapsed_time)
print("\n__________________________\n")


