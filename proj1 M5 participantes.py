# ============================================================
#  participantes.py  –  Gestão de Participantes
#  Estruturas usadas: Listas e Tuplos
# ============================================================

# Cada participante é um TUPLO imutável:
# (id, nome, turma, ano, tipo)   tipo -> "aluno" | "professor" | "convidado"

participantes = []   # LISTA global de tuplos


def _proximo_id():
    """Devolve o próximo ID disponível."""
    if not participantes:
        return 1
    return max(p[0] for p in participantes) + 1


# ── Criar ────────────────────────────────────────────────────

def adicionar_participante(nome, turma, ano, tipo="aluno"):
    """Cria um tuplo e adiciona-o à lista."""
    novo = (_proximo_id(), nome.strip().title(), turma.strip().upper(),
            int(ano), tipo.lower())
    participantes.append(novo)
    print(f"  ✔  Participante '{novo[1]}' adicionado com ID {novo[0]}.")
    return novo


# ── Ler ──────────────────────────────────────────────────────

def listar_todos():
    """Mostra todos os participantes."""
    if not participantes:
        print("  ⚠  Nenhum participante registado.")
        return
    print(f"\n  {'ID':<5} {'Nome':<25} {'Turma':<8} {'Ano':<5} {'Tipo':<12}")
    print("  " + "-" * 58)
    for p in participantes:
        print(f"  {p[0]:<5} {p[1]:<25} {p[2]:<8} {p[3]:<5} {p[4]:<12}")
    print(f"\n  Total: {len(participantes)} participante(s)\n")


def buscar_por_id(pid):
    """Devolve o tuplo do participante ou None."""
    for p in participantes:
        if p[0] == pid:
            return p
    return None


def buscar_por_nome(nome):
    """Devolve lista de tuplos cujo nome contenha a string."""
    nome = nome.lower()
    return [p for p in participantes if nome in p[1].lower()]


def listar_por_tipo(tipo):
    """Filtra participantes por tipo."""
    resultado = [p for p in participantes if p[4] == tipo.lower()]
    if not resultado:
        print(f"  ⚠  Nenhum participante do tipo '{tipo}'.")
        return []
    for p in resultado:
        print(f"  [{p[0]}] {p[1]}  –  {p[2]}  ({p[3]})")
    return resultado


# ── Remover ──────────────────────────────────────────────────

def remover_participante(pid):
    """Remove o participante com o ID indicado."""
    global participantes
    antes = len(participantes)
    participantes = [p for p in participantes if p[0] != pid]
    if len(participantes) < antes:
        print(f"  ✔  Participante ID {pid} removido.")
        return True
    print(f"  ✘  ID {pid} não encontrado.")
    return False


# ── Estatísticas ─────────────────────────────────────────────

def total_participantes():
    return len(participantes)


def tipos_existentes():
    """Devolve SET com os tipos únicos presentes."""
    return {p[4] for p in participantes}
