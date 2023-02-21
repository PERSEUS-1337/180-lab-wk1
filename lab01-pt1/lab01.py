# Specifications
'''
1. Read n as a user input (maybe from a command line or as a data stream);
2. Create a zero n x n square matrix M. Assigned a randomized non-zero value (1-1000) to grid points divisible by 10 such (0,0), (0,10), (20,0), (10,10) ... You can use a fucntion for this but the running time of this will not be considered in the "time_elapsed";
3. Take note of the system "time_before";
4. Call your function "terrain_inter(M)";
5. Take note of the system time "time_after";
6. Obtain the elapsed "time_elapsed" = "time_after" - "time_before"
7. Output the "time_elapsed"
8. (Optional) You can outout the resulting matrix.

For example, for computing the matrix of a 100x100 square matrix M:
$ lab03 < 100
$ time elapsed: 10.2345 seconds
'''

print("Enter a number: ")
n = int(input())
print(n)

def createMatrix(size):
    