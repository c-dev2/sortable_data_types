# Creating a feature for sortoables arrays repository.
# The intended feature will be merging 2 sorted arrays of integers.


def merge_arrays(A,B):
    
    results = []
    sortA = sorted(A)
    sortB = sorted(B)
    
    #Declaring 2 pointers
    i, j = 0, 0
    
    #Merging begins using a while for appending to being by comparing values.
    while i < len(sortA) and j < len(sortB):
        
        #compare each iteration values from both arrays to see the biggger value.
        if sortA[i] < sortB[j]:
            results.append(sortA[i])
            i += 1
        
        else:
            results.append(sortB[j])
            j += 1
    
    #Append remaining elements of each array.
    while i < len(sortA):
        results.append(sortA[i])
        i += 1
        
    while j < len(sortB):
        results.append(sortB[j])
        j += 1
        
    
    return results

    
