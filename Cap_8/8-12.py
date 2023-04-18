def verif(let, lis):
    for i in lis:
        if i == let:
            return True
    return False

let = input().lower()

lis = []
for i in range(5):
    lis.append(input(f"Palavra {i+1} = "))

print(f"-> {let} <- esta na lista {lis} == {verif(let, lis)}")