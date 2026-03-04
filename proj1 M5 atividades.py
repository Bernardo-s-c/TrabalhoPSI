# ============================================================
#  atividades.py  –  Gestão de Atividades do Evento
#  Estruturas usadas: Listas, Tuplos e Sets
# ============================================================

# Cada atividade é um TUPLO:
# (id, nome, sala, hora_inicio, hora_fim, max_vagas)

atividades = []   # LISTA de tuplos de atividades

# SET de pares (id_participante, id_atividade) – inscrições únicas
inscricoes = set()


def _proximo_id():
    if not atividades:
        return 1
    return max(a[0] for a in atividades) + 1


# ── Criar ────────────────────────────────────────────────────

def adicionar_atividade(nome, sala, hora_inicio, hora_fim, max_vagas=30):
    """Cria tuplo de atividade e adiciona à lista."""
    nova = (_proximo_id(), nome.strip().title(),
            sala.strip().upper(), hora_inicio, hora_fim, int(max_vagas))
    atividades.append(nova)
    print(f"  ✔  Atividade '{nova[1]}' criada com ID {nova[0]}.")
    return nova


# ── Ler ──────────────────────────────────────────────────────

def listar_atividades():
    if not atividades:
        print("  ⚠  Nenhuma atividade registada.")
        return
    print(f"\n  {'ID':<5} {'Nome':<28} {'Sala':<8} {'Início':<8} {'Fim':<8} {'Vagas':<6} {'Inscritos'}")
    print("  " + "-" * 72)
    for a in atividades:
        inscritos = _contar_inscritos(a[0])
        vagas_livres = a[5] - inscritos
        print(f"  {a[0]:<5} {a[1]:<28} {a[2]:<8} {a[3]:<8} {a[4]:<8} {a[5]:<6} {inscritos} ({vagas_livres} livres)")
    print()


def buscar_atividade(aid):
    for a in atividades:
        if a[0] == aid:
            return a
    return None


# ── Inscrições (SET) ─────────────────────────────────────────

def inscrever(id_participante, id_atividade):
    """Inscreve participante numa atividade usando um SET."""
    par = (id_participante, id_atividade)

    atividade = buscar_atividade(id_atividade)
    if not atividade:
        print(f"  ✘  Atividade ID {id_atividade} não existe.")
        return False

    if par in inscricoes:
        print(f"  ⚠  Participante {id_participante} já está inscrito nesta atividade.")
        return False

    if _contar_inscritos(id_atividade) >= atividade[5]:
        print(f"  ✘  Atividade '{atividade[1]}' sem vagas disponíveis.")
        return False

    inscricoes.add(par)
    print(f"  ✔  Participante {id_participante} inscrito em '{atividade[1]}'.")
    return True


def cancelar_inscricao(id_participante, id_atividade):
    """Remove inscrição do SET."""
    par = (id_participante, id_atividade)
    if par in inscricoes:
        inscricoes.discard(par)
        print(f"  ✔  Inscrição cancelada.")
        return True
    print(f"  ⚠  Inscrição não encontrada.")
    return False


def atividades_do_participante(id_participante):
    """Devolve SET com IDs das atividades do participante."""
    return {aid for (pid, aid) in inscricoes if pid == id_participante}


def participantes_da_atividade(id_atividade):
    """Devolve SET com IDs dos participantes numa atividade."""
    return {pid for (pid, aid) in inscricoes if aid == id_atividade}


def _contar_inscritos(id_atividade):
    return len(participantes_da_atividade(id_atividade))


# ── Operações de Conjuntos ───────────────────────────────────

def participantes_em_ambas(aid1, aid2):
    """SET intersection – participantes inscritos em DUAS atividades."""
    return participantes_da_atividade(aid1) & participantes_da_atividade(aid2)


def participantes_em_alguma(aid1, aid2):
    """SET union – participantes em PELO MENOS UMA das atividades."""
    return participantes_da_atividade(aid1) | participantes_da_atividade(aid2)


def participantes_so_em(aid1, aid2):
    """SET difference – participantes APENAS na primeira atividade."""
    return participantes_da_atividade(aid1) - participantes_da_atividade(aid2)
