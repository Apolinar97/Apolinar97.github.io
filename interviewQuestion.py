
def countManipulations(s1, s2):
     
    count = 0
 
    # store the count of character
    c_count = [0] * 26
     
    for i in range(26):
        c_count[i] = 0
 
    for i in range(len(A)):
        c_count[ord(A[i]) -
                   ord('a')] += 1
 
    for i in range(len(B)):
        c_count[ord(B[i]) - ord('a')] -= 1
         
    for i in range(26):
        if c_count[i] != 0:
            count += abs(c_count[i])
         
 
    return count