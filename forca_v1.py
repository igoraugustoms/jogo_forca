# -*- coding: utf-8 -*-

#Jogo da forca
#Curso de orientação a objetos

#importando bibliotecas

import random

tabuleiro = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']#lista de posição do tabuleiro


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []#lista para letras erradas
        self.guessed_letters = []#lista para letras certas

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters: #checo se letra está na palavra e se ela já nao foi dita antes
            self.guessed_letters.append(letter)#se isso acontecer, eu adiciono na lista de certas
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)#adiciono na lista de erradas
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6) #jogo acaba se o cara vence ou se foram as 6 tentativas

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True#se não tem _ na palavra, sinal que acertou tudo. Retorna true
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        oculto = ''
        for letter in self.word:
            if letter not in self.guessed_letters:#se para cada letra na palavra, e ela nao está na lista, eu escondo
                oculto += '_'
            else:
                oculto += letter#se nao, recebe o valor da propria letra
        return oculto

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(tabuleiro[len(self.missed_letters)])#printo o tabuleiro. A posição depende do numero de erros
        print('\nPalavra: ' + self.hide_word())#printo a palavra com os devidos itens ocultos
        print('\nPalavras erradas: ',)
        for letter in self.missed_letters:
            print(letter,)#Para cada letra errada, eu printo
        print()
        print('Letras corretas: ',)
        for letter in self.guessed_letters:
            print(letter,)#de forma análoga, para cada letra certa, eu printo
        print()

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        letter_input = str(input('\nDigite uma letra: '))
        game.guess(letter_input)


    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)



# Executa o programa
if __name__ == "__main__":
    main()