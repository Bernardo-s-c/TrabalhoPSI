import os

# --- CORES PARA O TERMINAL ---
RESET = "\033[0;0m"
NEGRITO = "\033[1m"
AZUL = "\033[94m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
CIANO = "\033[96m"

# Agora a turma é uma lista que conterá outras listas: [[nome, nota], [nome, nota]]
turma = []
NOME_FICHEIRO = "turma.txt"

# --- CARREGAR DADOS (Lógica de Listas) ---
if os.path.exists(NOME_FICHEIRO):
    with open(NOME_FICHEIRO, "r") as f:
        for linha in f:
            if "," in linha:
                partes = linha.strip().split(",")
                # Guardamos como uma lista [nome, nota]
                turma.append([partes[0], float(partes[1])])

while True:
    print(f"\n{AZUL}{'=' * 55}{RESET}")
    print(f"{AZUL}{NEGRITO}          GESTÃO DE TURMA PRO - V3.0 (LISTAS){RESET}")
    print(f"{AZUL}{'=' * 55}{RESET}")
    print(f"{AMARELO}[1]{RESET} Cadastrar Aluno")
    print(f"{AMARELO}[2]{RESET} Listar Alunos e Gráfico")
    print(f"{AMARELO}[3]{RESET} Gerir Aluno (Editar/Remover)")
    print(f"{AMARELO}[4]{RESET} Ranking (Top Notas)")
    print(f"{AMARELO}[5]{RESET} Estatísticas da Turma")
    print(f"{VERMELHO}[0]{RESET} Sair e Guardar")
    print(f"{AZUL}{'-' * 55}{RESET}")

    opcao = input(f"{NEGRITO}Escolha uma opção: {RESET}")

    if opcao == "1":
        nome = input("\nNome do aluno: ").strip().title()
        nota_str = input(f"Nota de {nome} (0-20): ")
        if nota_str.replace('.', '', 1).isdigit():
            nota = float(nota_str)
            if 0 <= nota <= 20:
                # ADICIONA UMA LISTA À LISTA PRINCIPAL
                turma.append([nome, nota])
                print(f"{VERDE}✔ {nome} adicionado!{RESET}")
            else:
                print(f"{VERMELHO}✘ Erro: Nota entre 0-20.{RESET}")
        else:
            print(f"{VERMELHO}✘ Erro: Digite um número.{RESET}")

    elif opcao == "2":
        if not turma:
            print(f"{AMARELO}Turma vazia.{RESET}")
        else:
            print(f"\n{NEGRITO}{'NOME':<15} {'NOTA':<6} {'DESEMPENHO'}{RESET}")
            print("-" * 55)
            for aluno in turma:
                # aluno[0] é o nome, aluno[1] é a nota
                blocos = "█" * int(aluno[1])
                espacos = " " * (20 - int(aluno[1]))
                cor = VERDE if aluno[1] >= 9.5 else VERMELHO
                print(f"{aluno[0]:<15} {aluno[1]:<6} {cor}[{blocos}{espacos}]{RESET}")

    elif opcao == "3":
        busca = input("\nNome para gerir: ").strip().title()
        encontrado = False
        for i, aluno in enumerate(turma):
            if aluno[0] == busca:
                encontrado = True
                print(f"\n{CIANO}Aluno: {aluno[0]} | Nota: {aluno[1]}{RESET}")
                print(f"{AMARELO}[E]{RESET} Editar | {VERMELHO}[R]{RESET} Remover | {AZUL}[S]{RESET} Sair")
                sub_op = input("Escolha: ").upper()
                if sub_op == "E":
                    nova_nota = float(input(f"Nova nota: "))
                    aluno[1] = nova_nota  # Altera o segundo elemento da sub-lista
                    print(f"{VERDE}Atualizado!{RESET}")
                elif sub_op == "R":
                    turma.pop(i)
                    print(f"{VERMELHO}Removido.{RESET}")
                break
        if not encontrado: print(f"{VERMELHO}Não encontrado.{RESET}")

    elif opcao == "4":
        if not turma:
            print(f"{VERMELHO}Sem dados.{RESET}")
        else:
            ranking = list(turma)
            n = len(ranking)
            for i in range(n):
                for j in range(0, n - i - 1):
                    # Comparamos as notas usando o índice [1]
                    if ranking[j][1] < ranking[j + 1][1]:
                        ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

            print(f"\n{AMARELO}🏆 RANKING 🏆{RESET}")
            for pos, aluno in enumerate(ranking, 1):
                icon = "🥇" if pos == 1 else "🥈" if pos == 2 else "🥉" if pos == 3 else f" {pos}º"
                print(f"{icon} - {aluno[0]}: {aluno[1]}")

    elif opcao == "5":
        if not turma:
            print(f"{VERMELHO}Vazio.{RESET}")
        else:
            soma = 0
            for a in turma: soma += a[1]
            print(f"\n{CIANO}Média: {soma / len(turma):.2f} | Total: {len(turma)}{RESET}")

    elif opcao == "0":
        with open(NOME_FICHEIRO, "w") as f:
            for aluno in turma:
                f.write(f"{aluno[0]},{aluno[1]}\n")
        print(f"\n{VERDE}Guardado. Tchau!{RESET}")
        break
