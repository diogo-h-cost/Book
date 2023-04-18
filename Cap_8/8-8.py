def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    return (a * b) / mdc(a, b)

a = int(input())
b = int(input())
if a < b:
    a, b = b, a

print(f"M.M.C de {a} e {b} = {mmc(a, b):.0f}")