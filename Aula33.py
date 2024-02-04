"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int (input('Informe a hora:'))

if horario <= 11 :
    print('Bom dia!')
elif horario <= 17 :
    print('Boa tarde!')
elif horario <= 23 :
    print('Boa noite!')    
else :
    print('Não conheço essa hora!')    
    