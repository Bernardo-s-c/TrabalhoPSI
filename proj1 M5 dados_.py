# ============================================================
#  dados_demo.py  –  Dados de Demonstração
#  Popula o sistema com dados iniciais para testar
# ============================================================

import participantes as p
import atividades as a


def carregar_dados_demo():
    print("\n  ⏳  A carregar dados de demonstração...")

    # ── Participantes (Tuplos guardados em Lista) ────────────
    p.adicionar_participante("Ana Rodrigues",    "10A", 10, "aluno")
    p.adicionar_participante("Bruno Ferreira",   "10A", 10, "aluno")
    p.adicionar_participante("Carla Mendes",     "11B", 11, "aluno")
    p.adicionar_participante("David Sousa",      "11B", 11, "aluno")
    p.adicionar_participante("Eva Lopes",        "12C", 12, "aluno")
    p.adicionar_participante("Filipe Costa",     "12C", 12, "aluno")
    p.adicionar_participante("Graça Oliveira",   "PROF", 0, "professor")
    p.adicionar_participante("Hugo Martins",     "PROF", 0, "professor")
    p.adicionar_participante("Inês Carvalho",    "EXT",  0, "convidado")
    p.adicionar_participante("João Pinto",       "10A", 10, "aluno")

    # ── Atividades (Tuplos guardados em Lista) ───────────────
    a.adicionar_atividade("Workshop de Robótica",   "A101", "09:00", "10:30", 20)
    a.adicionar_atividade("Teatro Escolar",         "AULA", "10:00", "11:30", 50)
    a.adicionar_atividade("Debate de Ciências",     "B205", "11:00", "12:00", 25)
    a.adicionar_atividade("Exposição de Arte",      "HALL", "09:00", "17:00", 100)
    a.adicionar_atividade("Palestra de Matemática", "C301", "14:00", "15:30", 30)

    # ── Inscrições (Pares guardados em Set) ──────────────────
    #  Workshop de Robótica (ID 1)
    for pid in [1, 2, 3, 5, 7, 10]:
        a.inscrever(pid, 1)

    #  Teatro Escolar (ID 2)
    for pid in [1, 4, 5, 6, 8, 9, 10]:
        a.inscrever(pid, 2)

    #  Debate de Ciências (ID 3)
    for pid in [2, 3, 6, 7]:
        a.inscrever(pid, 3)

    #  Exposição de Arte (ID 4)
    for pid in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        a.inscrever(pid, 4)

    #  Palestra de Matemática (ID 5)
    for pid in [3, 4, 7, 8, 9]:
        a.inscrever(pid, 5)

    print("  ✅  Dados de demonstração carregados com sucesso!\n")
