'''
CMSC 180 Lab 01 Part 01
Author: Aron Resty Ramillano | 2020-01721
Section: T3L
'''

# Specifications
'''
1. Read n as a user input (maybe from a command line or as a data stream);
2. Create a zero n x n square matrix M. Assigned a randomized non-zero value (1-1000) to grid points divisible by 10 such (0,0), (0,10), (20,0), (10,10) ... You can use a fucntion for this but the running time of this will not be considered in the "time_elapsed";
3. Take note of the system "time_before";
4. Call your function "terrain_inter(M)";
5. Take note of the system time "time_after";
6. Obtain the elapsed "time_elapsed" = "time_after" - "time_before"
7. Output the "time_elapsed"
8. (Optional) You can output the resulting matrix.

For example, for computing the matrix of a 100x100 square matrix M:
$ lab03 < 100
$ time elapsed: 10.2345 seconds
'''
# Resources:
# https://www.programiz.com/python-programming/matrix
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
# https://www.w3schools.com/python/ref_random_randint.asp
# https://www.geeksforgeeks.org/how-to-measure-elapsed-time-in-python/

import random
import math
import time

def row_print(matx):
    """
    It prints the matrix in a nice way
    
    :param matx: the matrix to be printed
    """
    print("Matrix:")
    for row in matx:
        print(row)


def coords_print(matx):
    """
    It prints the coordinates and values of a matrix
    
    :param matx: The matrix to be printed
    """
    print("Matrix Coordinates and Values")
    for i in range(len(matx)):
        for j in range(len(matx[0])):
            print("x: ",i,", y:", j,", val:", matx[i][j])


def create_matx(n):
    """
    It creates an n x n matrix with all zeros
    
    :param n: the number of nodes in the graph
    :return: A matrix of size n+1
    """
    print("Generating empty matrix...")
    n+=1
    matx = [[0 for i in range(n)] for j in range(n)]
    return matx


def rand_pop_matx(matx):
    """
    It populates the matrix with random elevation values at every 10th index
    
    :param matx: The matrix that will be populated with random elevation values
    """
    print("Populating Matrix with randomized elevation values...")
    for i in range(len(matx)):
        for j in range(len(matx[0])):
            if (((i)%10 == 0) and ((j)%10 == 0)):
                matx[i][j] = random.randint(1, 1000)


def terrain_inter(M):
    """
    It takes a matrix and for each point in the matrix, it calls a function that interpolates the point
    based on the surrounding points
    
    :param M: The matrix
    """
    for i in range(len(matx)):
        for j in range(len(matx[0])):
            if not (((i)%10 == 0) and ((j)%10 == 0)):
                a_w_point_inter(M,i,j)


def get_min_max(n):
    """
    It takes a number and returns the minimum and maximum numbers that are multiples of 10 and are
    within 10 of the input number
    
    :param n: The number of elements in the array
    :return: The minimum and maximum values of the range of numbers that the input number belongs to.
    """
    min = math.floor((n-1 if n > 1 else 1)/10)*10
    max = math.ceil((n if n > 0 else 1)/10)*10
    # print("Min:",min,", Max:",max)
    return min, max
       

def get_area(x,y):
    """
    The function takes in two lists of coordinates and returns the area of the four quadrants of the
    coordinate plane
    
    :param x: The x-coordinate of the center of the rectangle
    :param y: The y-coordinates of the points
    :return: The area of each of the four quadrants
    """
    min_x, max_x = get_min_max(x)
    min_y, max_y = get_min_max(y)
    area_d = abs(min_x - x) * abs(min_y - y)
    area_c = abs(max_x - x) * abs(min_y - y)
    area_b = abs(min_x - x) * abs(max_y - y)
    area_a = abs(max_x - x) * abs(max_y - y)
    
    # print("area_d:", area_d)
    # print("area_c:", area_c)
    # print("area_b:", area_b)
    # print("area_a:", area_a)
    
    # For getting the value, it is important that we start with d to follow the proper convention
    return area_d, area_c, area_b, area_a


def get_elev(matx, x1, x2, y1, y2):
    """
    It takes in a matrix, and four coordinates, and returns the elevation values at those coordinates
    
    :param matx: the matrix of elevation data
    :param x1: the x coordinate of the first point
    :param x2: the x coordinate of the second point
    :param y1: the y-coordinate of the top-left corner of the square
    :param y2: the y-coordinate of the bottom-right corner of the square
    :return: The elevation of the four points of the square.
    """
    elev_a = matx[x1][y1]
    elev_b = matx[x2][y1]
    elev_c = matx[x1][y2]
    elev_d = matx[x2][y2]
    
    # print("Elev A:,", elev_a)
    # print("Elev B:,", elev_b)
    # print("Elev C:,", elev_c)
    # print("Elev D:,", elev_d)
    
    return elev_a, elev_b, elev_c, elev_d


def a_w_point_inter(matx, x, y):
    """
    We find the area of each of the four quadrants that make up the square, then we find the elevation
    of each of the four points that make up the square, then we multiply the area of each quadrant by
    the elevation of the point that makes up that square, then we add all of those together and divide
    by the total area of the square
    
    :param matx: The matrix that we're working with
    :param x: x-coordinate of the point
    :param y: The y coordinate of the point we're interpolating
    """
    min_x, max_x = get_min_max(x)
    min_y, max_y = get_min_max(y)
    
    # Important that we start with d to get the right values
    area_d, area_c, area_b, area_a = get_area(x,y)
    elev_a, elev_b, elev_c, elev_d = get_elev(matx, min_x, max_x, min_y, max_y)
    
    elevation = ((area_a*elev_a) + (area_b*elev_b) + (area_c*elev_c) + (area_d*elev_d)) / (area_a + area_b + area_c + area_d)
    
    # print("Elevation of point(", x,",",y,") =", elevation)
    
    matx[x][y] = elevation
    
n = 1
# Get user input
while n:
    n = int(input("\nEnter a number divisible by 10: "))
    if not n%10:
        matx = create_matx(n)
        break

# Generate matrix with randomized values
rand_pop_matx(matx)

# Start the function and get the elapsed time
start = time.time()
terrain_inter(matx)
end = time.time()

choice = int(input("Do you want to print the resulting matrix? [1] if yes, [0] if no: "))
if choice == 1:
    row_print(matx)
    
print("Time Elapsed:",end - start, "seconds")