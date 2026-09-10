print("======================================")
print("        CONVERSOR DE BASES")
print("======================================")
print("2  - Binário")
print("8  - Octal")
print("10 - Decimal")
print("16 - Hexadecimal")

numero = input("\nDigite o número: ").upper()
base_origem = int(input("Digite a base de origem: "))
base_destino = int(input("Digite a base de destino: "))


# ==========================================
# 1. CONVERTER PARA DECIMAL
# ==========================================

if base_origem == 10:

    decimal = int(numero)

    print("\nO número já está em decimal.")

else:

    decimal = 0

    print("\n--- Convertendo para decimal ---")

    for i in range(len(numero)):

        digito = numero[i]

        if digito.isdigit():
            valor = int(digito)
        else:
            valor = ord(digito) - ord('A') + 10

        posicao = len(numero) - 1 - i

        calculo = valor * (base_origem ** posicao)

        print(
            valor, "×", base_origem, "^", posicao,
            "=", calculo
        )

        decimal = decimal + calculo

    print("Resultado decimal:", decimal)


# ==========================================
# 2. CONVERTER DECIMAL PARA A NOVA BASE
# ==========================================

if base_destino == 10:

    resultado = str(decimal)

else:

    simbolos = "0123456789ABCDEF"
    resultado = ""

    print("\n--- Convertendo decimal para a nova base ---")

    while decimal > 0:

        quociente = decimal // base_destino
        resto = decimal % base_destino

        print(
            decimal, "÷", base_destino,
            "=", quociente,
            "resto", resto
        )

        resultado = simbolos[resto] + resultado

        decimal = quociente


# ==========================================
# 3. RESULTADO FINAL
# ==========================================

print("\n")
print("======================================")
print("           RESULTADO FINAL")
print("======================================")
print(f"Número original : {numero}")
print(f"Base de origem  : {base_origem}")
print(f"Base de destino : {base_destino}")
print("--------------------------------------")
print(f"Resultado       : {resultado}")
print("======================================")