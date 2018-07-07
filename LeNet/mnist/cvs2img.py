
def convert(csv):
    file = open(csv, "r")
    
    for line in file:
        line = line.split(',')
        label = line[0]

        # Initialize digit as 28 x 28 which is the shape of an mnist sample
        w, h = (28, 28)
        digit = [[0 for x in range(w)] for y in range(h)]
        #print(digit)
        
        r, c = (0, 0)
        for i in range(1, 784):
            #print(i)
            
            

            #print(str(i) + ": " + str(r) + ", " + str(c) + " = " + str(line[i]))
            #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in digit]))
            digit[r][c] = line[i]

            if i % 28 == 0:
                r = r + 1
                c = 0
            else:
                c = c + 1
            
            
        #print(label)
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in digit]))
        #return
        


convert("mnist_test.csv")