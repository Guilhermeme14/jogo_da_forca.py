
import random

palavra1 = 'python'
palavra2 = 'exceto'
palavra3 = 'mister'
palavra4 = 'script'

lista = [palavra1, palavra2, palavra3, palavra4]

palavra = random.choice(lista)
letra_acertada = ''
repeticoes = 0

while True:
    letra_digitada = input('Digite uma letra: ')
        
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_digitada in palavra:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'
    print('Palavra: ', palavra_formada)  

    repeticoes +=1    
    
    if repeticoes >= 15:
        print('Bonequinho morreu, tente novamente')
        break

    if palavra_formada == palavra:
        print('Parabéns você conseguiu salvar a pessoa')
        print('A palavra era: ', palavra)
        print('Tentativas: ', repeticoes)
        break

