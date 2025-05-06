op = input("Escolha a operação (+, -, *, /): ")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida.")

input("Pressione Enter para sair...")
