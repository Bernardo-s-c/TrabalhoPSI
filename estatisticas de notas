# 1. Começamos com uma lista vazia
notas = []
print("(Digite as notas de 0 a 20 ou um número negativo para encerrar)")

while True:
    entrada_texto = input("Digite uma nota: ")

    # Se começar com '-', encerramos o programa
    if entrada_texto.startswith('-'):
        break

    # Verificamos se são apenas números
    if entrada_texto.isdigit():
        entrada = int(entrada_texto)

        # NOVA REGRA: Verificar se está entre 0 e 20
        if 0 <= entrada <= 20:
            notas.append(entrada)
        else:
            print("Erro: A nota deve estar entre 0 e 20!")
    else:
        print("Erro: Por favor, digite apenas números inteiros!")

# 2. Verificamos se a lista não está vazia
if len(notas) > 0:
    nota_alta = max(notas)
    nota_baixa = min(notas)
    media = sum(notas) / len(notas)

    # 3. Exibição dos resultados
    print("\n--- Relatório Final ---")
    print(f"Notas válidas inseridas: {notas}")
    print(f"Nota mais alta: {nota_alta}")
    print(f"Nota mais baixa: {nota_baixa}")
    print(f"Média: {media}")
else:
    print("Nenhuma nota válida foi registrada.")
