def magic_number(n):

    sum=0
    while n>0:
        sum+=n%10
        n//=10
    if sum>9:
        return magic_number(sum)
    else:
        if sum==1:
            return 1
        else:
            return 0

n=int(input())
print(magic_number(n))