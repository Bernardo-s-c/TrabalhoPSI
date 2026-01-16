import random

# Lista global para armazenar as passwords geradas durante a execução
historico_global = []


def desenhar_interface():
    # Cores fixas em códigos ANSI para evitar erros de variáveis não definidas
    # \033[94m = Azul | \033[95m = Roxo | \033[96m = Ciano | \033[93m = Amarelo
    print(f"\033[94m╔═══════════════════════════════════════════════════════════╗")
    print(f"║\033[95m                                                           \033[94m║")
    print(f"║\033[95m          ██████╗  █████╗ ███████╗███████╗                 \033[94m║")
    print(f"║\033[95m          ██╔══██╗██╔══██╗██╔════╝██╔════╝                 \033[94m║")
    print(f"║\033[95m          ██████╔╝███████║███████╗███████╗                 \033[94m║")
    print(f"║\033[95m          ██╔═══╝ ██╔══██║╚════██║╚════██║                 \033[94m║")
    print(f"║\033[95m          ██║     ██║  ██║███████║███████║                 \033[94m║")
    print(f"║\033[95m          ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝                 \033[94m║")
    print(f"║\033[96m                   >> PASS_GEN <<                          \033[94m║")
    print(f"║\033[95m                                                           \033[94m║")
    print(f"╠═══════════════════════════════════════════════════════════╣")
    print(f"║                                                           ║")
    print(f"║\033[96m  [1] GERAR PASSWORDS FORTES                               \033[94m║")
    print(f"║\033[96m  [2] ACEDER AO HISTÓRICO DE SESSÃO                        \033[94m║")
    print(f"║\033[96m  [3] TERMINAR SESSÃO                                      \033[94m║")
    print(f"║                                                           ║")
    print(f"╚═══════════════════════════════════════════════════════════╝\033[0m")
    print(f"\033[93mCMD_PROMPT > \033[0m", end="")


def gerar_passwords():
    frase = input("\n\033[93m>> FRASE ORIGEM:\033[0m ")
    palavras = frase.split()

    if len(palavras) < 2:
        print("\033[91m!! ERRO: USA PELO MENOS 2 PALAVRAS !!\033[0m")
        input("\nENTER para continuar...")
        return

    # 1. Lógica Hardened Sigla (Iniciais + Sal)
    sigla = "".join([p[0].upper() for p in palavras])
    op1 = sigla + "#_2026"

    # 2. Lógica Super Leet (Substituição de caracteres)
    subst = {'A': '4', 'a': '4', 'E': '3', 'e': '3', 'I': '1', 'i': '1', 'O': '0', 'o': '0', 'S': '5', 's': '$'}
    op2_temp = ""
    frase_sem_espacos = "".join(palavras)
    for i, letra in enumerate(frase_sem_espacos):
        char = letra.upper() if i % 2 == 0 else letra.lower()
        op2_temp += subst.get(char, char)
    op2 = op2_temp[:12] + "!"

    # 3. Lógica Word Expansion (Duas letras por palavra)
    op3_temp = ""
    for p in palavras:
        if len(p) >= 2:
            op3_temp += p[0:2].capitalize()
        else:
            op3_temp += p[0].upper() + "x"
    op3 = op3_temp + str(len(frase)) + "?"

    # Guardar no histórico
    historico_global.append(f"V1: {op1} | V2: {op2} | V3: {op3}")

    # Mostrar resultados
    print(f"\n\033[96m--- RESULTADOS DE ALTA SEGURANÇA ---\033[0m")
    print(f"\033[94m1. Hardened Sigla: \033[0m {op1}")
    print(f"\033[94m2. Super Leet:     \033[0m {op2}")
    print(f"\033[94m3. Word Expansion: \033[0m {op3}")
    input("\nENTER para voltar ao menu...")


def ver_historico():
    print(f"\n\033[96m--- HISTÓRICO DA SESSÃO ---\033[0m")
    if not historico_global:
        print("\033[91mHistórico vazio.\033[0m")
    else:
        for item in historico_global:
            print(f"\033[94m>>\033[0m {item}")
    input("\nENTER para voltar...")


def main():
    while True:
        desenhar_interface()
        escolha = input()

        if escolha == "1":
            gerar_passwords()
        elif escolha == "2":
            ver_historico()
        elif escolha == "3":
            print("\n\033[91mSISTEMA ENCERRADO.\033[0m")
            break
        else:
            print("\n\033[91mOpção inválida!\033[0m")


if __name__ == "__main__":
    main()