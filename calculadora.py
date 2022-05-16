print("Calculadora simples")
print("\n (+) (-) (*) (/) (=) ")

n = int(input("\nNúmero: "))
result = n
maior = n
menor = n
while True:
    op= input("Operação: ")
    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "="):
        break


while op != "=":
    n = int(input("Número: "))

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    if op == "+":
        result += n
    elif op == "-":
        result -= n
    elif op == "*":
        result *= n
    elif op == "/":
        result /= n 
    print(f"\nResultado: {result}")
        
    
    while True:
        op= input("\nOperação: ")
        if (op == "+" or op == "-" or op == "*" or op == "/" or op == "="):
            break
print("\n")
print(f"Resultado: {result}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")

