def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

a = int(input())
b = int(input())

if a < b:
    a, b = b, a

print(f"M.D.C de {a} e {b} = {mdc(a, b)}")