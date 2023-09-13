import random  as rd
import os

print(" Bem vindo ao jogo da Forca!!")

def jogo():
  os.system("cls")
  chances_restantes = 6
  letras_erradas = []
  letras_certas = []
  lista_de_palavras = ['CARRO', 'MOTO', 'NAVIO', 'AVIAO', 'METRO', 'CELULAR']
  palavra = rd.choice(lista_de_palavras)
  palavra_atualizada = []
  for i in palavra:
   palavra_atualizada.append(" _ ")
   status =''
  j= 0

  while status != 'Finalizado':
    print("\nChances Restantes: ", chances_restantes)
    print("Letras erradas: ", " ".join(letras_erradas))
    print("Advinhe a palavra abaixo:")
    print(" ".join(palavra_atualizada))
    letra = input("\nDigite uma letra: ").upper()

    if letra in palavra:
      for i in palavra:
        if i == letra:
          palavra_atualizada[j] = letra
        j+=1
    else:
      letras_erradas.append(letra)
      chances_restantes -=1
    if palavra_atualizada == list(palavra):
      print("\nVoce Ganhou!\nA palavra certa é: ", palavra)
      status = "Finalizado"
      retorno = input("\nDeseja jogar novamente ?\n1-Sim   2-Nao\n")
      if retorno == '1':
        os.system("cls")
        jogo()
      else:
        break
    if chances_restantes== 0:
     print("\nChances Esgotadas! Você Perdeu!")
     status = "Finalizado"
     retorno = input("\nDeseja jogar novamente ?\n1-Sim   2-Nao\n")
     os.system('cls') 
     if retorno == '1':
        jogo()
     else:
        break
    j=0

#Bolco Main Serve para dizer que esse script é um modulo
if __name__ =="__main__":
  jogo()