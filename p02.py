pop_a = 100
pop_b = 200
taxa_a = 1.3
taxa_b = 1.15
cont_anos = 0

while pop_a <= pop_b:

    pop_a = pop_a * taxa_a
    pop_b = pop_b * taxa_b
    cont_anos += 1
    if (cont_anos == 1):
        print(f"{cont_anos} ano se passou")
    else:
        print(f"{cont_anos} anos se passaram")
    print(f"População A atual: {pop_a:.2f}")
    print(f"População B atual: {pop_b:.2f}")
    print("=====")

if(cont_anos == 1):
    print(f"Foi necessário {cont_anos} ano até a população A se igualar ou passar a população B")
else:
    if(pop_a == pop_b):
        print(f"Foram necessários {cont_anos} anos até a população A se igualar a população B")
    else:
        print(f"Foram necessários {cont_anos} anos até a população A({int(pop_a)}) passar a população B({int(pop_b)})")