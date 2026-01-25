# --- CORES PARA O VISUAL (Podes mudar se quiseres) ---
VERDE = '\033[92m'  # Cor do título da tua imagem
AZUL = '\033[94m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'
# Criamos a lista que vai guardar os nomes (sem ficheiros externos)
nomes = []
while True:
    # Cabeçalho com o visual de "caixa" que gostaste
    print(f"\n{VERDE}╔════════════════════════════════════════╗")
    print(f"║      SISTEMA DE GESTÃO DE NOMES        ║")
    print(f"╚════════════════════════════════════════╝{RESET}")
    # Menu de Opções
    print(f"0. {AZUL}Adicionar Nome{RESET}")
    print(f"1. {AZUL}Remover Nome{RESET}")
    print(f"2. {AZUL}Listar Todos{RESET}")
    print(f"3. {AZUL}Procurar Nome{RESET}")
    print(f"4. {AZUL}Editar Nome{RESET}")
    print(f"5. {AZUL}Ordenar Lista{RESET}")
    print(f"6. {VERMELHO}Sair{RESET}")
    print(f"{VERDE}──────────────────────────────────────────{RESET}")
    opcao = input("O que deseja fazer? ")
    # --- 1. ADICIONAR ---
    if opcao == '0':
        novo = input("Escreva o nome para adicionar: ")
        nomes.append(novo)
        print(f"{VERDE}✔ {novo} foi guardado!{RESET}")
    # --- 2. REMOVER ---
    elif opcao == '1':
        remover = input("Qual nome quer apagar? ")
        if remover in nomes:
            nomes.remove(remover)
            print(f"{VERMELHO}✘ Nome removido.{RESET}")
        else:
            print(f"{AMARELO}⚠ Esse nome não está na lista.{RESET}")
    # --- 3. LISTAR ---
    elif opcao == '2':
        print(f"\n{AZUL}--- NOMES NA LISTA ---{RESET}")
        if len(nomes) == 0:
            print("Lista vazia.")
        else:
            # Mostra cada nome um por um
            for n in nomes:
                print(f"• {n}")
    # --- 4. PROCURAR ---
    elif opcao == '3':
        busca = input("Quem estás a procurar? ")
        if busca in nomes:
            print(f"{VERDE}★ Encontrado: {busca} está na lista!{RESET}")
        else:
            print(f"{VERMELHO}Não encontrado.{RESET}")
    # --- 5. EDITAR (Cena extra) ---
    elif opcao == '4':
        nome_antigo = input("Nome que queres mudar: ")
        if nome_antigo in nomes:
            novo_nome = input("Escreve o novo nome: ")
            # Encontra a posição do antigo e substitui pelo novo
            posicao = nomes.index(nome_antigo)
            nomes[posicao] = novo_nome
            print(f"{VERDE}✔ Atualizado com sucesso!{RESET}")
        else:
            print(f"{AMARELO}Esse nome não existe.{RESET}")
    # --- 6. ORDENAR (Cena extra) ---
    elif opcao == '5':
        nomes.sort()  # Organiza de A a Z
        print(f"{AZUL}↕ Lista organizada por ordem alfabética.{RESET}")
    # --- 0. SAIR ---
    elif opcao == '6':
        print(f"{AMARELO}A sair do programa...{RESET}")
        break
    # SE DIGITAR OPÇÃO ERRADA
    else:
        print(f"{VERMELHO}Opção inválida!{RESET}")
