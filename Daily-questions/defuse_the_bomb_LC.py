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