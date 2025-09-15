# Algorithm Explanation:
# Problem: Given a circular array 'code' and an integer k, replace each element with the sum of the next k elements (if k > 0) or previous k elements (if k < 0). If k == 0, replace all elements with 0.
# Approach:
# 1. If k == 0, return an array of zeros with the same length as code.
# 2. If k > 0:
#    - For each index i, create a rotated version of code starting at i.
#    - Sum the next k elements (positions 1 to k in the rotated list) and assign to decrypted_code[i].
# 3. If k < 0:
#    - For each index i, create a rotated version of code starting at i.
#    - Sum the previous k elements (using negative indexing) and assign to decrypted_code[i].
# 4. Return the decrypted_code array.

def decrypt(code, k):
    decrypted_code=[None]*len(code)
    if k == 0:
        return [0 for _ in code]
    elif k>0:
        for i in range(0,len(code)):
            list1=code[i:]+code[:i]
            print(list1)
            decrypted_code[i]=sum(list1[1:1+k])
        return decrypted_code
    elif k<0:
        for i in range(0,len(code)):
            list1=code[i:]+code[:i]
            print(list1)
            print(list1[-1:k-1:-1])
            decrypted_code[i]=sum(list1[-1:k-1:-1])
    return decrypted_code
        

code = [10,5,7,7,3,2,10,3,6,9,1,6]
k = -4
print(decrypt(code,k))
print("output:-[12,5,6,13]")