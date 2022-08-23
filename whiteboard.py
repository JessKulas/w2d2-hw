#Given an array of integers.

#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

#If the input is an empty array or is null, return an empty array.

#Example
#For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


#def count_positives_sum_negatives(arr):
   # if len(arr) == 0:
      #  return[]
    #positive_count = sum([1 for i in arr if i > 0])
    #negative_sum = sum([i for i in arr if i < 0])
    #return[positive_count, negative_sum]



list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

def count_positives_sum_negatives(numbers):

    pos_count = 0
    
    neg_sum = 0

    for numpos in numbers:
        if numpos > 0:
            pos_count += 1

        else:
            neg_sum += numpos
    
    return [pos_count, neg_sum]

    print(count_positives_sum_negatives)




