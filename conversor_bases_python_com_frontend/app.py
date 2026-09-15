"""
CONVERSOR DE BASES — APLICAÇÃO WEB EM PYTHON

Frontend:
    HTML + CSS

Backend:
    Python + Flask

A lógica de conversão permanece em Python.
O navegador apenas envia os dados e exibe o resultado.
"""

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='HTML', static_folder='CSS', static_url_path='/CSS')


# =========================================================
# CONVERTER QUALQUER BASE PARA DECIMAL
# =========================================================
def para_decimal(numero, base):
    """
    Converte um número da base informada para decimal.

    Exemplo:
        1010 na base 2 -> 10 na base 10

    Cada dígito é multiplicado pela base elevada
    à posição correspondente.
    """
    simbolos = "0123456789ABCDEF"
    numero = numero.upper()
    decimal = 0
    passos = []

    for i, digito in enumerate(numero):
        valor = simbolos.index(digito)
        posicao = len(numero) - 1 - i
        calculo = valor * (base ** posicao)

        decimal += calculo

        passos.append(
            f"{valor} × {base}^{posicao} = {calculo}"
        )

    return decimal, passos


# =========================================================
# CONVERTER DECIMAL PARA OUTRA BASE
# =========================================================
def de_decimal(decimal, base):
    """
    Converte um número decimal para a base escolhida.

    O método utiliza divisões sucessivas:
    divide o número pela base e guarda os restos.
    Os restos são lidos de trás para frente.
    """
    simbolos = "0123456789ABCDEF"
    resultado = ""
    passos = []

    if decimal == 0:
        return "0", ["O valor decimal é 0."]

    while decimal > 0:
        quociente = decimal // base
        resto = decimal % base

        passos.append(
            f"{decimal} ÷ {base} = {quociente}, resto {resto}"
        )

        resultado = simbolos[resto] + resultado
        decimal = quociente

    return resultado, passos


# =========================================================
# VALIDAR NÚMERO
# =========================================================
def numero_valido(numero, base):
    """
    Verifica se todos os caracteres pertencem à base escolhida.
    """
    simbolos = "0123456789ABCDEF"
    numero = numero.upper()

    if not numero:
        return False

    for digito in numero:
        if digito not in simbolos:
            return False

        if simbolos.index(digito) >= base:
            return False

    return True


# =========================================================
# NOME DAS BASES
# =========================================================
def nome_base(base):
    """Retorna o nome da base para mostrar na interface."""
    nomes = {
        2: "Binário",
        8: "Octal",
        10: "Decimal",
        16: "Hexadecimal"
    }

    return nomes[base]


# =========================================================
# ROTA PRINCIPAL
# =========================================================
@app.route("/", methods=["GET", "POST"])
def index():
    """
    Exibe a página e processa as conversões.

    GET:
        Apenas mostra o formulário.

    POST:
        Recebe número, base de origem e base de destino,
        realiza a conversão em Python e envia os dados
        de volta para o HTML.
    """

    dados = None
    erro = None

    if request.method == "POST":
        numero = request.form.get("numero", "").strip().upper()

        try:
            base_origem = int(request.form.get("base_origem"))
            base_destino = int(request.form.get("base_destino"))

            bases_permitidas = [2, 8, 10, 16]

            if base_origem not in bases_permitidas:
                raise ValueError("Base de origem inválida.")

            if base_destino not in bases_permitidas:
                raise ValueError("Base de destino inválida.")

            if not numero_valido(numero, base_origem):
                raise ValueError(
                    f'O número "{numero}" não é válido para a base '
                    f"{base_origem}."
                )

            # Primeira etapa: origem -> decimal.
            decimal, passos_decimal = para_decimal(
                numero, base_origem
            )

            # Segunda etapa: decimal -> destino.
            if base_destino == 10:
                resultado = str(decimal)
                passos_destino = []
            else:
                resultado, passos_destino = de_decimal(
                    decimal, base_destino
                )

            dados = {
                "numero": numero,
                "base_origem": base_origem,
                "nome_origem": nome_base(base_origem),
                "base_destino": base_destino,
                "nome_destino": nome_base(base_destino),
                "decimal": decimal,
                "resultado": resultado,
                "passos_decimal": passos_decimal,
                "passos_destino": passos_destino
            }

        except (ValueError, TypeError):
            erro = "Digite um número válido e selecione bases permitidas."

    return render_template(
        "index.html",
        dados=dados,
        erro=erro
    )


# =========================================================
# INICIAR SERVIDOR
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)
