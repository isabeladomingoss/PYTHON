texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS: #.upper() transforma letra em letra maiuscula
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha
    print("Executa no final do laço")