import random

palavras = ["arthur", "mouse", "sao paulo", "cadeira", "carro", "ze raimundo", "computador", "php", "javascript"]
palavraEscolhida = random.choice(palavras)

LetraEscolhida = ["_"] * len(palavraEscolhida)
Quantidadeerros = len(palavraEscolhida) - 1 
MeusErros= 0

print("A palavras sorteada tem " + str(len(palavraEscolhida))+ " letras")



while "_" in LetraEscolhida and MeusErros < Quantidadeerros:
    print("Palavra" + " ".join(LetraEscolhida))
    LetraInformada = input("INFORME A LETRA: ")
    if LetraInformada in palavraEscolhida:
        for i  in range/len(palavraEscolhida):
            if palavraEscolhida[i] == LetraInformada:
                LetraEscolhida[i] = LetraInformada
else:
    MeusErros +=1
    print("ERRRRRRRROU...")