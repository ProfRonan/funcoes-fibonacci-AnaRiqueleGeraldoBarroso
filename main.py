def fibonacci(num):
    if num < 0:
        raise ValueError("n tem que ser maior do que zero")
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    primeiro_termo = 0
    segundo_termo = 1
    contador = 3    
    while contador <= num+1:
        terceiro_termo = primeiro_termo + segundo_termo
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
        contador += 1
    return terceiro_termo
if __name__=="__main__":
    num = int(input("Digite um número: "))
    print(fibonacci(num))