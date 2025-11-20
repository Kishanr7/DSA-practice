def convert(s,numRows):
    if numRows == 1:
        return s
    
    i = 0
    d = 1
    
    rows = [[] for _ in range(numRows)]
    
    for char in s:
        rows[i].append(char)   
        if i == 0:
            d = 1
        elif i == numRows - 1:
            d = -1
        i += d
    
    ret = ''
    for i in range(numRows):
        ret += ''.join(rows[i])
    return ret

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"