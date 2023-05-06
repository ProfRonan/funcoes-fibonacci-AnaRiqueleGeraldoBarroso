def fibonacci(num):
    if num < 0:
        raise ValueError("n tem que ser maior do que zero")
    primeiro_termo = 0
    segundo_termo = 1
    contador = 3
    print(f"{primeiro_termo} - {segundo_termo}", end=" ")
    while contador <= num:
        terceiro_termo = primeiro_termo + segundo_termo
        print(f" - {terceiro_termo}", end=" ")
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
        contador += 1

num = int(input("Digite um número: "))
fibonacci(num)