#2. Receba ano de nascimento e ano atual. Calcule idade e semanas.

#Entrada
AnoNascimento = int(input("Digite seu ano de nascimento: "))
AnoAtual = int(input("Digite o ano atual: "))

#Processamento
Idade = AnoAtual - AnoNascimento
IdadeEmSemanas = Idade * 12 * 4


#Saida
print(f"Sua idade é: {Idade}")
print(f"Sua idade em semanas é: {IdadeEmSemanas}")