import numpy as np
import cv2

def convert(csv):
    file = open(csv, "r")
    
    for line in file:
        line = line.split(',')
        label = line[0]

        # Initialize digit as 28 x 28 which is the shape of an mnist sample
        w, h = (28, 28)
        digit = [[0 for x in range(w)] for y in range(h)]

        r, c = (0, 0)
        # Take the unrolled 784 vector and structure it as a matrix.
        for i in range(1, 784):

            if i % 28 == 0:
                r = r + 1
                c = 0
            else:
                c = c + 1
            digit[r][c] = int(line[i])

        digit = np.asarray(digit, dtype = np.uint8)
        cv2.imshow("mnist digit", digit)
        cv2.waitKey(1)
        #print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in digit]))

        


convert("mnist_test.csv")