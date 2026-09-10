# Conversor de Bases Numéricas

Um programa feito com Python para realizar conversões entre diferentes sistemas de numeração:
- Binário (base 2)
- Octal (base 8)
- Decimal (base 10)
- Hexadecimal (base 16)
  
##  Sobre o projeto
O usuário informa:

1. O número que deseja converter;
2. A base em que o número está;
3. A base para a qual deseja converter.
Depois disso, o programa realiza a conversão e apresenta o resultado no proprio terminal.

##  Bases disponíveis

 Base  Sistema Símbolos 
-------------------------
| 2 | Binário | 0 e 1 |
| 8 | Octal | 0 até 7 |
| 10 | Decimal | 0 até 9 |
| 16 | Hexadecimal | 0 até 9 e A até F |

##  Como funciona

O programa realiza a conversão em duas etapas principais.

### 1. Converter para decimal

Primeiro, o programa verifica a base de origem.
Se o número já estiver na base 10, ele não precisa ser convertido.
Caso a base não seja decimal então cada algarismo é multiplicado pela base elevada à sua posição.
