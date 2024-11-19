def plus_one(digits):
    string_num=int(''.join(map(str,digits)))+1
    return [int(i) for i in str(string_num)]
    
digits=[9]
print(plus_one(digits))