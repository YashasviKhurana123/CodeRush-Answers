def sum_triplet(l):
    # Write your code here
    triplets = []
    
    # Sort the list for easier processing
    l.sort()

    # Find all unique triplets where the sum of two equals the third
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = l[i], l[j], l[k]
                if a + b == c or a + c == b or b + c == a:
                    triplet = [a, b, c]
                    triplet.sort()  # Sort the triplet to avoid duplicates
                    if triplet not in triplets:
                        triplets.append(triplet)

    # Print the 2D array (list of lists) in the desired format
    print(triplets)