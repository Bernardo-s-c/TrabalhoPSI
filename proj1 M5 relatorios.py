# ============================================================
#  relatorios.py  –  Relatórios e Estatísticas
#  Estruturas usadas: Listas, Tuplos e Sets
# ============================================================

import participantes as p
import atividades as a


def _linha(char="─", largura=60):
    print("  " + char * largura)


def cabecalho(titulo):
    print()
    _linha("═")
    print(f"  {'📋  ' + titulo}")
    _linha("═")


# ── Relatório Geral ──────────────────────────────────────────

def relatorio_geral():
    cabecalho("RELATÓRIO GERAL DO EVENTO")

    total = p.total_participantes()
    tipos = p.tipos_existentes()   # SET

    print(f"\n  👥  Total de participantes : {total}")
    print(f"  🏷   Tipos presentes        : {', '.join(tipos) if tipos else 'nenhum'}")
    print(f"  🎯  Total de atividades    : {len(a.atividades)}")
    print(f"  📝  Total de inscrições    : {len(a.inscricoes)}")

    # Contagem por tipo usando list comprehension
    for tipo in sorted(tipos):
        conta = len([x for x in p.participantes if x[4] == tipo])
        print(f"       • {tipo.capitalize():<15}: {conta}")
    print()


# ── Relatório por Atividade ──────────────────────────────────

def relatorio_atividade(id_atividade):
    ativ = a.buscar_atividade(id_atividade)
    if not ativ:
        print(f"  ✘  Atividade {id_atividade} não encontrada.")
        return

    cabecalho(f"ATIVIDADE: {ativ[1]}")
    print(f"\n  🏫  Sala      : {ativ[2]}")
    print(f"  🕐  Horário   : {ativ[3]} – {ativ[4]}")
    print(f"  👥  Max vagas : {ativ[5]}")

    ids_inscritos = a.participantes_da_atividade(id_atividade)   # SET
    print(f"  ✅  Inscritos : {len(ids_inscritos)}")
    print(f"  🆓  Livres    : {ativ[5] - len(ids_inscritos)}\n")

    if ids_inscritos:
        print(f"  {'ID':<6} {'Nome':<25} {'Turma':<8} {'Tipo'}")
        _linha()
        for pid in sorted(ids_inscritos):
            part = p.buscar_por_id(pid)
            if part:
                print(f"  {part[0]:<6} {part[1]:<25} {part[2]:<8} {part[4]}")
    print()


# ── Relatório por Participante ───────────────────────────────

def relatorio_participante(id_participante):
    part = p.buscar_por_id(id_participante)
    if not part:
        print(f"  ✘  Participante {id_participante} não encontrado.")
        return

    cabecalho(f"PARTICIPANTE: {part[1]}")
    print(f"\n  🆔  ID     : {part[0]}")
    print(f"  📛  Nome   : {part[1]}")
    print(f"  🏫  Turma  : {part[2]}  (Ano {part[3]})")
    print(f"  🏷   Tipo   : {part[4].capitalize()}\n")

    ids_ativ = a.atividades_do_participante(id_participante)   # SET
    print(f"  Atividades inscritas: {len(ids_ativ)}")
    if ids_ativ:
        _linha()
        for aid in sorted(ids_ativ):
            ativ = a.buscar_atividade(aid)
            if ativ:
                print(f"  🎯 [{ativ[0]}] {ativ[1]}  –  Sala {ativ[2]}  ({ativ[3]}-{ativ[4]})")
    print()


# ── Relatório de Operações de Conjuntos ──────────────────────

def relatorio_conjuntos(aid1, aid2):
    a1 = a.buscar_atividade(aid1)
    a2 = a.buscar_atividade(aid2)
    if not a1 or not a2:
        print("  ✘  Uma das atividades não existe.")
        return

    cabecalho(f"ANÁLISE DE CONJUNTOS: {a1[1]} vs {a2[1]}")

    ambas = a.participantes_em_ambas(aid1, aid2)
    alguma = a.participantes_em_alguma(aid1, aid2)
    so_a1 = a.participantes_so_em(aid1, aid2)
    so_a2 = a.participantes_so_em(aid2, aid1)

    print(f"\n  🔵  Apenas em '{a1[1]}' (A-B)  : {len(so_a1)} participante(s)  {so_a1}")
    print(f"  🟢  Apenas em '{a2[1]}' (B-A)  : {len(so_a2)} participante(s)  {so_a2}")
    print(f"  🔴  Em AMBAS (A∩B)             : {len(ambas)} participante(s)  {ambas}")
    print(f"  🟡  Em ALGUMA (A∪B)            : {len(alguma)} participante(s)  {alguma}")
    print()
