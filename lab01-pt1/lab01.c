// Specifications

// 1. Read n as a user input (maybe from a command line or as a data stream);
// 2. Create a zero n x n square matrix M. Assigned a randomized non-zero value (1-1000) to grid points divisible by 10 such (0,0), (0,10), (20,0), (10,10) ... You can use a fucntion for this but the running time of this will not be considered in the "time_elapsed";
// 3. Take note of the system "time_before";
// 4. Call your function "terrain_inter(M)";
// 5. Take note of the system time "time_after";
// 6. Obtain the elapsed "time_elapsed" = "time_after" - "time_before"
// 7. Output the "time_elapsed"
// 8. (Optional) You can outout the resulting matrix.

// For example, for computing the matrix of a 100x100 square matrix M:
// $ lab03 < 100
// $ time elapsed: 10.2345 seconds

// Tasks:

// 1. Lets create a matrix first and print it - DONE
// 2. Get the time of the machine to store it - DONE
// 3. Figure out how to calculate the points sequentially from 00 to end

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// #define RAND_MAX 1000

int getTimeNow()
{
    time_t now = time(0);
    return now;
}

float float_rand(float min, float max)
{
    float scale = rand() / (float) RAND_MAX; /* [0, 1.0] */
    return min + scale * ( max - min );      /* [min, max] */
}


int main() 
{
    int input;
    int row, col;
    int time_before, time_after;

    // time_before = getTimeNow();
    // printf("\t%ls\n", &time_before);

    // Get User Input
    printf("Enter a number: ");
    scanf("%d", &input);
    if (input % 10 != 0)
    {
        printf("Invalid input!");
        return -1;
    }
    printf("Input accepted!\n");

    // Generate Matrix via a 1d array sequence
	float* matxptr = malloc((input * input) * sizeof(float));

	/* Putting 1 to 12 in the 1D array in a sequence */
	for (int i = 0; i < input * input; i++)
    {
        if ((i+1)%10 == 0)
        {
            matxptr[i] = float_rand(0, 1000);
            // matxptr[i] = i+1;
        } else matxptr[i] = 0;
        
    }

	/* Accessing the array values as if it was a 2D array */
	for (int i = 0; i < input; i++) {
		for (int j = 0; j < input; j++)
			printf("%f ", matxptr[i * input + j]);
            // printf("(%d %d) ", i, j);
		printf("\n");
	}

    for (int i = 0; i < input; i++) {
		for (int j = 0; j < input; j++)
			printf("%f ", matxptr[i * input + j]);
            // printf("(%d %d) ", i, j);
		printf("\n");
	}

	free(matxptr);
    time_after = getTimeNow();
    printf("\t%ls\n", &time_after);

	return 0;
    // int **matx = createMatrix(input);
    // time_before = getTimeNow();
    // printf("%ls", &time_before);
}


// Referrences:
// https://stackoverflow.com/questions/14166350/how-to-display-a-matrix-in-c
// https://stackoverflow.com/questions/5141960/get-the-current-time-in-c
// https://beginnersbook.com/2014/01/2d-arrays-in-c-example/
// https://www.geeksforgeeks.org/dynamically-allocate-2d-array-c/