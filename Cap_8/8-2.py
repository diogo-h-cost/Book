def multiplo(n1, n2):
    if n1 / 2 == n2 or n1 == n2:
        return True
    return False

n1 = int(input())
n2 = int(input())
print(f"multiplo({n1}, {n2}) == {multiplo(n1, n2)}")