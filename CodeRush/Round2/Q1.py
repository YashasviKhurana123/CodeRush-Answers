def treasure_burying(ncr):
    # Write your code here
    for i in range(int(ncr[0])):
        for j in range(int(ncr[0])):
            if (i,j) == ((ord(ncr[1])-97),int(ncr[2])-1):
                print("|X|", end='')
            else:
                print("|_|", end='')
        print()