#a=0
#print(a)

def ACC(n):
    if n<0:
        print("Illegal")
    else:
        m=0
        for i in range(n+1):
            m=m+i
    return m

n=5
print(ACC(n))