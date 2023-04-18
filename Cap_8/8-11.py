def vali(let, min, max):
    if len(let) >= min and len(let) <= max:
        return True
    return False

let = input().upper().strip()
min = int(input())
max = int(input())
print(f"String entre {min} e {max} caracteres = {vali(let, min, max)}")