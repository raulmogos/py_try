

def BinaryGap(n):
    maxZeros = 0
    zeros = 0
    ones = 0
    didPassFirstOne = False
    while n!=0:
        if n%2 == 0:
            if didPassFirstOne:
                zeros += 1
        else:
            ones += 1
            if not didPassFirstOne:
                didPassFirstOne = True
            else:
                # get max
                if zeros > maxZeros:
                    maxZeros = zeros
                zeros = 0
        n = int(n//2)
    return 0 if ones == 1 else maxZeros + 1

r = BinaryGap(343)
print(r)
