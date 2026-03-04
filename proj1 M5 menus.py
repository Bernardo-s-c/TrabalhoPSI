# ============================================================
#  menus.py  –  Interface de Menus do Sistema
# ============================================================

import participantes as p
import atividades as a
import relatorios as r


def _cabecalho_sistema():
    print("\n" + "═" * 62)
    print("   🏫  SISTEMA DE GESTÃO DE PARTICIPANTES – EVENTO ESCOLAR")
    print("═" * 62)


def _input_int(msg, minimo=1):
    while True:
        valor = input(msg).strip()
        if valor.isdigit() and int(valor) >= minimo:
            return int(valor)
        print("  ⚠  Por favor insira um número válido.")


def _pausar():
    input("\n  ↩  Prima ENTER para continuar...")


# ══════════════════════════════════════════════════════════════
#  MENU PARTICIPANTES
# ══════════════════════════════════════════════════════════════

def menu_participantes():
    while True:
        print("\n  ┌─────────────────────────────────┐")
        print("  │     👥  PARTICIPANTES           │")
        print("  ├─────────────────────────────────┤")
        print("  │  1. Adicionar participante      │")
        print("  │  2. Listar todos                │")
        print("  │  3. Procurar por nome           │")
        print("  │  4. Listar por tipo             │")
        print("  │  5. Remover participante        │")
        print("  │  6. Ver ficha de participante   │")
        print("  │  0. Voltar                      │")
        print("  └─────────────────────────────────┘")

        opcao = input("  Opção: ").strip()

        if opcao == "1":
            print("\n  ── Novo Participante ──")
            nome = input("  Nome           : ").strip()
            turma = input("  Turma          : ").strip()
            ano = _input_int("  Ano escolar    : ")
            print("  Tipo: 1-Aluno  2-Professor  3-Convidado")
            t = input("  Tipo [1]: ").strip()
            tipos_map = {"1": "aluno", "2": "professor", "3": "convidado"}
            tipo = tipos_map.get(t, "aluno")
            p.adicionar_participante(nome, turma, ano, tipo)

        elif opcao == "2":
            p.listar_todos()

        elif opcao == "3":
            nome = input("  Nome a procurar: ").strip()
            resultados = p.buscar_por_nome(nome)
            if resultados:
                for part in resultados:
                    print(f"  [{part[0]}] {part[1]}  –  {part[2]}  ({part[4]})")
            else:
                print("  ⚠  Nenhum resultado.")

        elif opcao == "4":
            print("  Tipos: aluno | professor | convidado")
            tipo = input("  Tipo: ").strip()
            p.listar_por_tipo(tipo)

        elif opcao == "5":
            pid = _input_int("  ID a remover: ")
            p.remover_participante(pid)

        elif opcao == "6":
            pid = _input_int("  ID do participante: ")
            r.relatorio_participante(pid)

        elif opcao == "0":
            break
        else:
            print("  ⚠  Opção inválida.")

        _pausar()


# ══════════════════════════════════════════════════════════════
#  MENU ATIVIDADES
# ══════════════════════════════════════════════════════════════

def menu_atividades():
    while True:
        print("\n  ┌─────────────────────────────────┐")
        print("  │     🎯  ATIVIDADES              │")
        print("  ├─────────────────────────────────┤")
        print("  │  1. Adicionar atividade         │")
        print("  │  2. Listar atividades           │")
        print("  │  3. Inscrever participante      │")
        print("  │  4. Cancelar inscrição          │")
        print("  │  5. Ver participantes atividade │")
        print("  │  6. Análise de conjuntos        │")
        print("  │  0. Voltar                      │")
        print("  └─────────────────────────────────┘")

        opcao = input("  Opção: ").strip()

        if opcao == "1":
            print("\n  ── Nova Atividade ──")
            nome = input("  Nome            : ").strip()
            sala = input("  Sala            : ").strip()
            inicio = input("  Hora início     : ").strip()
            fim = input("  Hora fim        : ").strip()
            vagas = _input_int("  Nº máx. vagas  : ")
            a.adicionar_atividade(nome, sala, inicio, fim, vagas)

        elif opcao == "2":
            a.listar_atividades()

        elif opcao == "3":
            pid = _input_int("  ID participante : ")
            aid = _input_int("  ID atividade    : ")
            a.inscrever(pid, aid)

        elif opcao == "4":
            pid = _input_int("  ID participante : ")
            aid = _input_int("  ID atividade    : ")
            a.cancelar_inscricao(pid, aid)

        elif opcao == "5":
            aid = _input_int("  ID atividade    : ")
            r.relatorio_atividade(aid)

        elif opcao == "6":
            print("  Comparar duas atividades (operações de conjuntos)")
            aid1 = _input_int("  ID atividade A  : ")
            aid2 = _input_int("  ID atividade B  : ")
            r.relatorio_conjuntos(aid1, aid2)

        elif opcao == "0":
            break
        else:
            print("  ⚠  Opção inválida.")

        _pausar()


# ══════════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════

def menu_principal():
    _cabecalho_sistema()
    while True:
        print("\n  ┌─────────────────────────────────┐")
        print("  │        📋  MENU PRINCIPAL       │")
        print("  ├─────────────────────────────────┤")
        print("  │  1. 👥  Gerir Participantes     │")
        print("  │  2. 🎯  Gerir Atividades        │")
        print("  │  3. 📊  Relatório Geral         │")
        print("  │  0. 🚪  Sair                    │")
        print("  └─────────────────────────────────┘")

        opcao = input("  Opção: ").strip()

        if opcao == "1":
            menu_participantes()
        elif opcao == "2":
            menu_atividades()
        elif opcao == "3":
            r.relatorio_geral()
            _pausar()
        elif opcao == "0":
            print("\n  👋  Até breve!\n")
            break
        else:
            print("  ⚠  Opção inválida.")
