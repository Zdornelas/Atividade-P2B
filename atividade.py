alturas = []
alturas_homens = []
quantidade_mulheres = 0

for i in range(15):
    altura = float(input(f"Digite a altura da pessoa{i + 1}:"))
    genero = input("Digite o Gênero (Masculino/Feminino):").strip().lower()

    alturas.append(altura)

    if genero == "masculino":
        alturas_homens.append(altura)
    elif genero == "feminino":
        quantidade_mulheres += 1
    else: print("Gênero invalido.")

    alturas.sort(reverse=True)  

    media_altura = sum(alturas_homens) / len(alturas_homens) if alturas_homens else 0
    
    print("Lista de alturas do maior para o menor:")
    for altura in alturas:
        print(altura)
    print(f"Média de altura dos homens: {media_altura}")
    print(f"Quantidade de mulheres: {quantidade_mulheres}")