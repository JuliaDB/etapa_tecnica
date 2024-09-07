print('-=' * 12)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 12)

a = 0
b = 1

def pertence_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b

    return False

def main():
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        if pertence_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    main()
