# ============================================================
#  main.py  –  Ponto de Entrada do Sistema
#
#  🏫  Sistema de Gestão de Participantes num Evento Escolar
#
#  Estruturas de dados utilizadas:
#    ✅  LISTAS    – armazenam participantes e atividades
#    ✅  TUPLOS    – representam cada participante/atividade
#    ✅  SETS      – gerem inscrições e operações de conjuntos
#
#  Ficheiros do projeto:
#    main.py        – arranque e menu de boas-vindas
#    participantes.py – lógica de participantes
#    atividades.py  – lógica de atividades e inscrições
#    relatorios.py  – relatórios e estatísticas
#    menus.py       – interface de utilizador (menus)
#    dados_.py      – dados de exemplo para testar
# ============================================================

import menus
import dados_


def boas_vindas():
    print()
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║                                                      ║")
    print("  ║   🏫  EVENTO ESCOLAR  –  SISTEMA DE GESTÃO           ║")
    print("  ║                                                      ║")
    print("  ║   Estruturas usadas:                                 ║")
    print("  ║     📋 Listas   → guardar participantes/atividades   ║")
    print("  ║     📦 Tuplos   → representar cada registo           ║")
    print("  ║     🔵 Sets     → inscrições únicas e conjuntos      ║")
    print("  ║                                                      ║")
    print("  ╚══════════════════════════════════════════════════════╝")


def perguntar_demo():
    print("\n  Deseja carregar dados de demonstração? (s/n) ", end="")
    resposta = input().strip().lower()
    return resposta in ("s", "sim", "y", "yes", "")


# ── Arranque ─────────────────────────────────────────────────

if __name__ == "__main__":
    boas_vindas()

    if perguntar_demo():
        dados_.carregar_dados_demo()

    menus.menu_principal()
