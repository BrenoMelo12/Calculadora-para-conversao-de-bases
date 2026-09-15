# Conversor de Bases

## Sobre o projeto

A estrutura utiliza:

- **Python** para a lógica da conversão;
- **Flask** para criar o servidor web;
- **HTML** para a interface;
- **CSS** para a aparência.

O código Python original foi adaptado para funcionar por meio de um formulário web.

## Estrutura

```text
conversor_bases_python_frontend/
│
├── app.py
├── requisitos.txt
│
├── HTML/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md
```

## Como executar

### 1. Instalar o Flask

No terminal:

```bash
pip install -r requisitos.txt
```

### 2. Entrar na pasta do projeto

```bash
cd conversor_bases_python_frontend
```

### 3. Executar

```bash
python app.py
```

O terminal mostrará um endereço local, normalmente:

```text
http://127.0.0.1:5000
```

Abra esse endereço no navegador.

## Como o projeto funciona

O navegador envia:

```text
Número
Base de origem
Base de destino
```

para o Python.

O Python executa:

```text
1. Validação do número
        ↓
2. Conversão da origem para decimal
        ↓
3. Conversão do decimal para a base de destino
        ↓
4. Envio do resultado para o HTML
```

## Bases disponíveis

| Base | Nome |
|---:|---|
| 2 | Binário |
| 8 | Octal |
| 10 | Decimal |
| 16 | Hexadecimal |

## Exemplo

Entrada:

```text
Número: 1010
Origem: 2
Destino: 10
```

O Python calcula:

```text
1 × 2³ = 8
0 × 2² = 0
1 × 2¹ = 2
0 × 2⁰ = 0

8 + 0 + 2 + 0 = 10
```

Resultado:

```text
10
```

## Observação

O Flask é necessário somente para conectar o navegador ao Python. A matemática da conversão continua sendo executada pelo Python.
