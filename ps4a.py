# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def swap_letters(sequence, index_1, index_2):
    """
    Swaps the letters at the indices 1 and 2 and returns the new string.
    Assumes that index 2 - index 1 is 1.
    """
    string_list = list(sequence)
    string_list[index_1], string_list[index_2] = string_list[index_2], string_list[index_1]
    return ''.join(string_list)

print swap_letters('abcd', 1, 0)

def get_permutations(sequence, index_of_start, index_of_end, list_of_permutations):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if index_of_start == index_of_end:
        list_of_permutations.append(sequence)
        print list_of_permutations
    else:
        for i in xrange(len(sequence)):
            print 'calling swap_letters with start, i', index_of_start, i
            sequence = swap_letters(sequence, index_of_start, i)
            print 'sequence after swap', sequence
            get_permutations(sequence, index_of_start + 1, index_of_end, list_of_permutations)
            print 'sequence after recursice call', sequence
            swap_letters(sequence, index_of_start, i)
            print 'sequence after backtrack', sequence
            
        


list_of_permutations = []  
print get_permutations('abcd', 0, 2, list_of_permutations)

##def get_permutations_lists((list_of_permutations, list_of_rests)):
    
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(list_of_string, start, end):
    if start == end:
        print toString(list_of_string)
    else:
        for i in xrange(start, end + 1):
            list_of_string[start], list_of_string[i] = list_of_string[i], list_of_string[start]
            permute(list_of_string, start + 1, end)
            list_of_string[start], list_of_string[i] = list_of_string[i], list_of_string[start] # backtrack
 
# Driver program to test the above function
string = "ABC"
n = len(string)
list_of_string = list(string)
permute(list_of_string, 0, n-1)

