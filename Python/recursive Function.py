#recursive function
def power(a,b):

    if b==1:
        return a

    return a*power(a,b-1)

res = power(3,3)
print(res)