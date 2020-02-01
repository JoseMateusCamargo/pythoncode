
#solution -> Count Even Odd - Python
#https://practice.geeksforgeeks.org/problems/count-even-odd-python/1


""" This is a function problem.You only need to complete the function given below """
#User function Template for python3
# Function to count even and odd
# c_e : variable to store even count
# c_o : variable to store odd count
def count_even_odd(n, arr):
   
    pair = list()
    
    # start code
    c_e=len([x for x in arr if x%2==0])
    c_o=len([x for x in arr if x%2!=0])
    # finish code
    
    pair.append(c_e)
    pair.append(c_o)
    return pair
    
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array
        size_array = int(input())
        
        # array elements input
        array = input().split()
        # print (array)
        arr = list()
        for i in array:
            arr.append(int(i))
            
        # print (arr)
        
        # calling function to count even odd
        a = count_even_odd(size_array, arr)
        print (a[0], a[1])
        testcases -= 1
 
if __name__ == '__main__':
    main()
