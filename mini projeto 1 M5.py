# =============================================================================
#  MINI PROJETO 1 — Sistema de Gestão de Produtos de uma Pequena Loja
#  Estrutura: cada produto é um TUPLO | conjunto de produtos é uma LISTA
# =============================================================================
#
#  Composição do tuplo de produto:
#  (id, nome, categoria, preco, quantidade_stock, fornecedor, ativo)
#
#   [0] id          → int   — identificador único do produto
#   [1] nome        → str   — nome do produto
#   [2] categoria   → str   — categoria a que pertence (ex: "Bebidas")
#   [3] preco       → float — preço unitário em euros
#   [4] quantidade  → int   — unidades disponíveis em stock
#   [5] fornecedor  → str   — nome do fornecedor
#   [6] ativo       → bool  — True = disponível / False = descontinuado
# =============================================================================

import os  # módulo para interagir com o sistema operativo (limpar o ecrã)

# ── CÓDIGOS DE COR ANSI ───────────────────────────────────────────
# Estes códigos são sequências especiais que o terminal interpreta como cores.
# São strings que envolvem o texto que queremos colorir.
# Formato: "\033[<código>m" para iniciar e "\033[0m" para repor a cor normal.
RESET    = "\033[0m"   # repõe a formatação para o padrão do terminal
BOLD     = "\033[1m"   # texto a negrito
DIM      = "\033[2m"   # texto mais escuro / apagado
VERDE    = "\033[92m"  # verde brilhante
AZUL     = "\033[94m"  # azul claro
CIANO    = "\033[96m"  # ciano (azul-verde claro)
AMARELO  = "\033[93m"  # amarelo brilhante
VERMELHO = "\033[91m"  # vermelho brilhante
BRANCO   = "\033[97m"  # branco brilhante
CINZA    = "\033[90m"  # cinza escuro
BG_AZUL  = "\033[44m"  # fundo azul (background)

# ------------------------------------------------------------------
# DADOS INICIAIS — lista de tuplos
# Cada elemento da lista é um tuplo imutável que representa um produto.
# Esta é a "base de dados" da nossa loja enquanto o programa está a correr.
# ------------------------------------------------------------------
produtos: list = [
    # (id,  nome,                  categoria,      preco,  stock, fornecedor,          ativo )
    (1,  "Arroz Carolino 1kg",   "Alimentacao", 1.29,  150, "Distribuidor Sul",  True),
    (2,  "Azeite Extra Virgem",  "Alimentacao", 4.99,   60, "Herdade do Freixo", True),
    (3,  "Leite Gordo 1L",       "Laticinios",  0.89,  200, "Lacticoop",         True),
    (4,  "Queijo Flamengo",      "Laticinios",  3.49,   80, "Lacticoop",         True),
    (5,  "Agua das Pedras 1.5L", "Bebidas",     0.59,  300, "Unicer",            True),
    (6,  "Sumo de Laranja 1L",   "Bebidas",     1.79,  120, "Compal",            True),
    (7,  "Cerveja SB 33cl",      "Bebidas",     0.79,  250, "Unicer",            True),
    (8,  "Detergente Roupa",     "Limpeza",     5.49,   45, "Procter & Gamble",  True),
    (9,  "Lixivia 1L",           "Limpeza",     0.99,   90, "Sonasol",           True),
    (10, "Pao de Forma",         "Padaria",     1.19,   70, "Bimbo",             True),
    (11, "Bolachas Maria",       "Snacks",      0.89,  110, "Nacional",          True),
    (12, "Batatas Fritas 200g",  "Snacks",      1.59,   85, "Lay's",             True),
    (13, "Shampoo 400ml",        "Higiene",     3.29,   55, "Pantene",           False), # produto descontinuado
    (14, "Pasta de Dentes",      "Higiene",     2.19,   75, "Colgate",           True),
]


# =============================================================================
# FUNÇÕES UTILITÁRIAS DE APRESENTAÇÃO
# Funções auxiliares para formatar e mostrar informação no terminal.
# =============================================================================

def limpar_ecra() -> None:
    """Limpa o terminal para manter o ecrã organizado.
    'cls' é o comando do Windows, 'clear' é o do Mac/Linux.
    os.name == 'nt' verifica se o sistema é Windows."""
    os.system("cls" if os.name == "nt" else "clear")


def pausa() -> None:
    """Pausa o programa e espera que o utilizador pressione ENTER.
    Usado depois de mostrar resultados, para o utilizador ter tempo de ler."""
    print(f"\n  {CINZA}{'─' * 50}{RESET}")
    input(f"  {DIM}Pressiona ENTER para continuar...{RESET} ")


def cabecalho_sistema(subtitulo: str = "") -> None:
    """Mostra o cabeçalho principal do sistema com fundo azul.
    O parâmetro subtitulo é opcional — se fornecido, aparece por baixo do cabeçalho.
    O valor padrão é uma string vazia, o que significa que não mostra subtítulo."""
    limpar_ecra()
    print(f"\n  {AZUL}{'═' * 58}{RESET}")
    # Texto centrado dentro de um bloco com fundo azul (BG_AZUL)
    print(f"  {BG_AZUL}{BOLD}{BRANCO}{'':3}{'SISTEMA DE GESTAO DE LOJA':^52}{'':3}{RESET}")
    print(f"  {BG_AZUL}{BOLD}{BRANCO}{'':3}{'Mini Projeto 1  --  Tuplos & Listas':^52}{'':3}{RESET}")
    print(f"  {AZUL}{'═' * 58}{RESET}")
    if subtitulo:  # só mostra o subtítulo se não for uma string vazia
        print(f"\n  {BOLD}{CIANO}▸ {subtitulo.upper()}{RESET}")


def cabecalho_tabela() -> None:
    """Mostra a linha de cabeçalho da tabela de produtos com os nomes das colunas.
    Usa formatação de strings para alinhar cada coluna."""
    print(f"\n  {CINZA}{'─' * 72}{RESET}")
    # :<4 = alinhar à esquerda com largura 4 | :>7 = alinhar à direita com largura 7
    print(f"  {BOLD}{CIANO}{'ID':<4} {'Nome':<25} {'Categoria':<14} {'Preco':>7} {'Stock':>6}  {'Estado'}{RESET}")
    print(f"  {CINZA}{'─' * 72}{RESET}")


def imprimir_produto(p: tuple) -> None:
    """Mostra uma linha formatada com os dados de um produto (tuplo).
    - Produtos ativos aparecem com ● verde, inativos com ○ vermelho.
    - Stock abaixo de 50 unidades aparece a amarelo como alerta visual.
    O parâmetro p é um tuplo com a estrutura definida no cabeçalho do ficheiro."""

    # Define a cor e símbolo do estado consoante p[6] (ativo/inativo)
    estado = f"{VERDE}● Ativo  {RESET}" if p[6] else f"{VERMELHO}○ Inativo{RESET}"

    # Stock a amarelo se for baixo, a branco se estiver ok
    stock_cor = AMARELO if p[4] < 50 else BRANCO

    # Imprime todos os campos do tuplo com alinhamento e cores
    print(f"  {CINZA}{p[0]:<4}{RESET} {BRANCO}{p[1]:<25}{RESET} {DIM}{p[2]:<14}{RESET} "
          f"{VERDE}{p[3]:>6.2f}E{RESET} {stock_cor}{p[4]:>6}{RESET}  {estado}")


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro do utilizador com validação.
    Fica em loop até o utilizador introduzir um valor válido.
    O try/except captura o erro quando se tenta converter texto em inteiro."""
    while True:
        try:
            return int(input(mensagem))  # tenta converter o input para inteiro
        except ValueError:
            # ValueError acontece quando o input não é um número (ex: "abc")
            print(f"  {VERMELHO}Introduz um numero inteiro valido.{RESET}")


def ler_float(mensagem: str) -> float:
    """Lê um número decimal do utilizador com validação.
    Aceita tanto ponto como vírgula como separador decimal (ex: 1.99 ou 1,99)."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))  # substitui vírgula por ponto
        except ValueError:
            print(f"  {VERMELHO}Introduz um numero valido (ex: 1.99).{RESET}")


def ler_id_valido(lista: list, mensagem: str) -> int:
    """Lê um ID e verifica se existe na lista de produtos.
    Retorna 0 se o utilizador quiser cancelar.
    Usa list comprehension para extrair todos os IDs existentes."""
    ids = [p[0] for p in lista]  # lista de todos os IDs existentes
    while True:
        pid = ler_int(mensagem)
        if pid == 0:
            return 0  # 0 significa cancelar
        if pid in ids:
            return pid  # ID válido, retorna
        print(f"  {VERMELHO}ID {pid} nao existe. Tenta outro.{RESET}")


# =============================================================================
# OPERAÇÕES SOBRE PRODUTOS
# Funções que manipulam a lista de produtos.
# NOTA IMPORTANTE: os tuplos são IMUTÁVEIS — não se pode alterar um campo
# diretamente. Para "atualizar", criamos um novo tuplo com os valores alterados
# e substituímos o antigo na lista.
# =============================================================================

def _proximo_id(lista: list) -> int:
    """Calcula o próximo ID disponível, pegando no maior ID existente e somando 1.
    O underscore no início (_proximo_id) é uma convenção que indica que esta
    função é auxiliar/interna — não foi pensada para ser chamada diretamente."""
    return max(p[0] for p in lista) + 1 if lista else 1  # se lista vazia, começa em 1


def adicionar_produto(lista, nome, categoria, preco, quantidade, fornecedor, ativo=True):
    """Cria um novo tuplo com os dados fornecidos e adiciona-o à lista.
    O ID é gerado automaticamente pela função _proximo_id.
    O parâmetro ativo tem valor padrão True (produto ativo por defeito)."""
    novo = (_proximo_id(lista), nome, categoria, preco, quantidade, fornecedor, ativo)
    lista.append(novo)  # append adiciona o novo tuplo no final da lista
    return lista


def remover_produto(lista, produto_id):
    """Remove um produto da lista filtrando pelo ID.
    Usa list comprehension para criar uma nova lista SEM o produto a remover.
    Não modifica a lista original — cria e retorna uma nova."""
    return [p for p in lista if p[0] != produto_id]  # mantém todos exceto o que tem o ID a remover


def atualizar_preco(lista, produto_id, novo_preco):
    """Atualiza o preço de um produto.
    Como os tuplos são imutáveis, percorremos a lista e para o produto com o ID
    pretendido criamos um novo tuplo com o novo preço na posição [3].
    Para todos os outros, mantemos o tuplo original."""
    return [
        (p[0], p[1], p[2], novo_preco, p[4], p[5], p[6])  # novo tuplo com preço atualizado
        if p[0] == produto_id
        else p  # tuplo original para os outros produtos
        for p in lista
    ]


def atualizar_stock(lista, produto_id, quantidade):
    """Atualiza o stock de um produto somando a quantidade (pode ser negativa para saídas).
    max(0, ...) garante que o stock nunca fica negativo."""
    return [
        (p[0], p[1], p[2], p[3], max(0, p[4] + quantidade), p[5], p[6])  # soma a quantidade ao stock atual
        if p[0] == produto_id
        else p
        for p in lista
    ]


def alternar_estado(lista, produto_id):
    """Inverte o estado ativo/inativo de um produto (toggle).
    'not p[6]' inverte o booleano: True torna-se False e vice-versa."""
    return [
        (p[0], p[1], p[2], p[3], p[4], p[5], not p[6])  # inverte o campo ativo [6]
        if p[0] == produto_id
        else p
        for p in lista
    ]


def exportar_csv(lista, ficheiro="produtos_loja.csv"):
    """Guarda todos os produtos num ficheiro CSV (valores separados por vírgulas).
    O try/except trata possíveis erros ao escrever no disco (ex: permissões).
    O parâmetro ficheiro tem um valor padrão caso o utilizador não especifique."""
    try:
        # "w" = modo escrita | encoding="utf-8" para suportar caracteres especiais
        with open(ficheiro, "w", encoding="utf-8") as f:
            f.write("id,nome,categoria,preco,quantidade,fornecedor,ativo\n")  # linha de cabeçalho
            for p in lista:
                # escreve cada tuplo como uma linha CSV
                f.write(f"{p[0]},{p[1]},{p[2]},{p[3]},{p[4]},{p[5]},{p[6]}\n")
        print(f"\n  {VERDE}Ficheiro '{ficheiro}' exportado! ({len(lista)} produtos){RESET}")
    except IOError as e:
        print(f"\n  {VERMELHO}Erro ao exportar: {e}{RESET}")


# =============================================================================
# MENUS INTERATIVOS
# Cada função de menu mostra as opções, lê a escolha do utilizador
# e chama as funções de operação correspondentes.
# =============================================================================

def menu_listar(lista):
    """Menu para listar produtos com 3 filtros: todos, ativos ou descontinuados.
    Usa list comprehension para filtrar a lista conforme a opção escolhida."""
    cabecalho_sistema("Listar Produtos")

    # Mostra as opções disponíveis
    print(f"\n  {CINZA}[{RESET}{BOLD}{CIANO}1{RESET}{CINZA}]{RESET}  Todos os produtos")
    print(f"  {CINZA}[{RESET}{BOLD}{CIANO}2{RESET}{CINZA}]{RESET}  Apenas ativos")
    print(f"  {CINZA}[{RESET}{BOLD}{CIANO}3{RESET}{CINZA}]{RESET}  Apenas descontinuados")
    print(f"  {CINZA}[{RESET}{BOLD}{VERMELHO}0{RESET}{CINZA}]{RESET}  Voltar")

    opcao = input(f"\n  {BOLD}{CIANO}>{RESET} ").strip()  # .strip() remove espaços extra

    if opcao == "1":
        # Mostra todos os produtos sem filtro
        cabecalho_tabela()
        for p in lista:
            imprimir_produto(p)
        print(f"\n  {DIM}Total: {len(lista)} produto(s){RESET}")

    elif opcao == "2":
        # Filtra apenas produtos com p[6] == True (ativos)
        ativos = [p for p in lista if p[6]]
        cabecalho_tabela()
        for p in ativos:
            imprimir_produto(p)
        print(f"\n  {DIM}Total: {len(ativos)} produto(s) ativo(s){RESET}")

    elif opcao == "3":
        # Filtra apenas produtos com p[6] == False (inativos/descontinuados)
        inativos = [p for p in lista if not p[6]]
        cabecalho_tabela()
        if inativos:
            for p in inativos:
                imprimir_produto(p)
        else:
            print(f"\n  {VERDE}Nenhum produto descontinuado.{RESET}")
        print(f"\n  {DIM}Total: {len(inativos)} produto(s){RESET}")

    elif opcao != "0":
        print(f"  {VERMELHO}Opcao invalida.{RESET}")

    # Só pausa se o utilizador não escolheu voltar (opção 0)
    if opcao != "0":
        pausa()


def menu_adicionar(lista):
    """Menu para adicionar um novo produto à lista.
    Pede todos os dados ao utilizador, valida e cria o novo tuplo."""
    cabecalho_sistema("Adicionar Produto")

    # Lê o nome e valida que não está vazio
    nome = input(f"\n  {CIANO}Nome do produto  :{RESET} ").strip()
    if not nome:
        print(f"  {VERMELHO}Nome nao pode estar vazio.{RESET}")
        pausa()
        return lista  # retorna a lista sem alterações

    categoria  = input(f"  {CIANO}Categoria        :{RESET} ").strip()
    preco      = ler_float(f"  {CIANO}Preco (E)        :{RESET} ")
    quantidade = ler_int(f"  {CIANO}Quantidade stock :{RESET} ")
    fornecedor = input(f"  {CIANO}Fornecedor       :{RESET} ").strip()
    ativo_str  = input(f"  {CIANO}Ativo? (s/n)     :{RESET} ").strip().lower()
    ativo      = ativo_str != "n"  # True se não respondeu "n"

    # Adiciona o produto e guarda a lista atualizada
    lista = adicionar_produto(lista, nome, categoria, preco, quantidade, fornecedor, ativo)
    novo  = lista[-1]  # o último elemento é o que acabamos de adicionar

    print(f"\n  {VERDE}Produto adicionado com ID {novo[0]}!{RESET}")
    cabecalho_tabela()
    imprimir_produto(novo)
    pausa()
    return lista  # devolve a lista com o novo produto


def menu_remover(lista):
    """Menu para remover um produto pelo seu ID.
    Pede confirmação antes de remover para evitar acidentes."""
    cabecalho_sistema("Remover Produto")

    # Mostra todos os produtos para o utilizador ver os IDs disponíveis
    cabecalho_tabela()
    for p in lista:
        imprimir_produto(p)

    print()
    pid = ler_id_valido(lista, f"  {CIANO}ID a remover {CINZA}(0 para cancelar){CIANO}:{RESET} ")
    if pid == 0:
        return lista  # utilizador cancelou

    # Encontra o produto com esse ID usando next() — retorna o primeiro que encontrar
    produto = next(p for p in lista if p[0] == pid)

    # Pede confirmação antes de remover
    conf = input(f"\n  {AMARELO}Tens a certeza que queres remover '{produto[1]}'? (s/n):{RESET} ").strip().lower()

    if conf == "s":
        lista = remover_produto(lista, pid)
        print(f"\n  {VERDE}'{produto[1]}' removido com sucesso.{RESET}")
    else:
        print(f"  {CINZA}Remocao cancelada.{RESET}")

    pausa()
    return lista


def menu_atualizar(lista):
    """Menu para atualizar dados de um produto existente.
    Oferece 4 opções: preço, entrada de stock, saída de stock e ativar/desativar."""
    cabecalho_sistema("Atualizar Produto")

    print(f"\n  {CINZA}[{RESET}{BOLD}{AMARELO}1{RESET}{CINZA}]{RESET}  Atualizar preco")
    print(f"  {CINZA}[{RESET}{BOLD}{AMARELO}2{RESET}{CINZA}]{RESET}  Entrada de stock  (+)")
    print(f"  {CINZA}[{RESET}{BOLD}{AMARELO}3{RESET}{CINZA}]{RESET}  Saida de stock    (-)")
    print(f"  {CINZA}[{RESET}{BOLD}{AMARELO}4{RESET}{CINZA}]{RESET}  Ativar / Desativar produto")
    print(f"  {CINZA}[{RESET}{BOLD}{VERMELHO}0{RESET}{CINZA}]{RESET}  Voltar")

    opcao = input(f"\n  {BOLD}{CIANO}>{RESET} ").strip()
    if opcao == "0":
        return lista
    if opcao not in ("1", "2", "3", "4"):
        print(f"  {VERMELHO}Opcao invalida.{RESET}")
        pausa()
        return lista

    # Mostra a lista para o utilizador escolher o ID
    cabecalho_tabela()
    for p in lista:
        imprimir_produto(p)

    print()
    pid = ler_id_valido(lista, f"  {CIANO}ID do produto {CINZA}(0 para cancelar){CIANO}:{RESET} ")
    if pid == 0:
        return lista

    # Encontra o produto atual para mostrar os valores antes de atualizar
    produto = next(p for p in lista if p[0] == pid)

    if opcao == "1":
        # Atualiza o preço — substitui o campo [3] do tuplo
        print(f"  {DIM}Preco atual: {produto[3]:.2f}E{RESET}")
        novo_preco = ler_float(f"  {CIANO}Novo preco (E):{RESET} ")
        lista = atualizar_preco(lista, pid, novo_preco)
        print(f"  {VERDE}Preco atualizado: {produto[3]:.2f}E → {novo_preco:.2f}E{RESET}")

    elif opcao == "2":
        # Entrada de stock — soma uma quantidade positiva ao campo [4]
        print(f"  {DIM}Stock atual: {produto[4]} unidades{RESET}")
        qtd = ler_int(f"  {CIANO}Quantidade a adicionar:{RESET} ")
        lista = atualizar_stock(lista, pid, +qtd)  # + para entrada
        print(f"  {VERDE}Stock: {produto[4]} → {produto[4] + qtd}{RESET}")

    elif opcao == "3":
        # Saída de stock — subtrai quantidade (passa negativo para atualizar_stock)
        print(f"  {DIM}Stock atual: {produto[4]} unidades{RESET}")
        qtd = ler_int(f"  {CIANO}Quantidade a remover:{RESET} ")
        novo_stock = max(0, produto[4] - qtd)  # garante que não fica negativo
        lista = atualizar_stock(lista, pid, -qtd)  # - para saída
        print(f"  {VERDE}Stock: {produto[4]} → {novo_stock}{RESET}")

    elif opcao == "4":
        # Toggle do estado ativo/inativo — inverte o booleano [6]
        novo_estado = not produto[6]
        lista = alternar_estado(lista, pid)
        cor = VERDE if novo_estado else VERMELHO
        estado_str = "ATIVO" if novo_estado else "INATIVO"
        print(f"  {cor}'{produto[1]}' esta agora: {estado_str}{RESET}")

    pausa()
    return lista


def menu_pesquisar(lista):
    """Menu de pesquisa com 4 critérios diferentes.
    Todos usam list comprehension com condições para filtrar a lista."""
    cabecalho_sistema("Pesquisar Produtos")

    print(f"\n  {CINZA}[{RESET}{BOLD}{AZUL}1{RESET}{CINZA}]{RESET}  Por nome")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}2{RESET}{CINZA}]{RESET}  Por categoria")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}3{RESET}{CINZA}]{RESET}  Por fornecedor")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}4{RESET}{CINZA}]{RESET}  Por intervalo de preco")
    print(f"  {CINZA}[{RESET}{BOLD}{VERMELHO}0{RESET}{CINZA}]{RESET}  Voltar")

    opcao = input(f"\n  {BOLD}{CIANO}>{RESET} ").strip()
    resultados = []  # lista onde vão ficar os resultados da pesquisa

    if opcao == "1":
        termo = input(f"  {CIANO}Nome (ou parte):{RESET} ").strip()
        # .lower() em ambos para pesquisa case-insensitive (ignora maiúsculas/minúsculas)
        # 'in' verifica se o termo aparece em qualquer parte do nome
        resultados = [p for p in lista if termo.lower() in p[1].lower()]

    elif opcao == "2":
        # Mostra as categorias existentes para ajudar o utilizador
        cats = sorted(set(p[2] for p in lista))  # set() remove duplicados, sorted() ordena
        print(f"  {DIM}Categorias: {', '.join(cats)}{RESET}")
        cat = input(f"  {CIANO}Categoria:{RESET} ").strip()
        # == para correspondência exata (ao contrário de 'in' que é parcial)
        resultados = [p for p in lista if p[2].lower() == cat.lower()]

    elif opcao == "3":
        forn = input(f"  {CIANO}Fornecedor (ou parte):{RESET} ").strip()
        # Pesquisa parcial no campo fornecedor [5]
        resultados = [p for p in lista if forn.lower() in p[5].lower()]

    elif opcao == "4":
        # Filtra por intervalo de preço — verifica se p[3] está entre min e max
        min_p = ler_float(f"  {CIANO}Preco minimo (E):{RESET} ")
        max_p = ler_float(f"  {CIANO}Preco maximo (E):{RESET} ")
        resultados = [p for p in lista if min_p <= p[3] <= max_p]

    else:
        if opcao != "0":
            print(f"  {VERMELHO}Opcao invalida.{RESET}")
        return  # sai da função sem fazer pausa

    # Mostra os resultados ou mensagem de "não encontrado"
    if resultados:
        cabecalho_tabela()
        for p in resultados:
            imprimir_produto(p)
        print(f"\n  {VERDE}{len(resultados)} resultado(s) encontrado(s).{RESET}")
    else:
        print(f"\n  {AMARELO}Nenhum produto encontrado.{RESET}")

    pausa()


def menu_ordenar(lista):
    """Menu para ordenar e visualizar os produtos por diferentes critérios.
    Usa sorted() que cria uma nova lista ordenada sem modificar a original.
    O parâmetro key define o critério de ordenação usando uma função lambda."""
    cabecalho_sistema("Ordenar Produtos")

    print(f"\n  {CINZA}[{RESET}{BOLD}{AZUL}1{RESET}{CINZA}]{RESET}  Por preco (crescente)")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}2{RESET}{CINZA}]{RESET}  Por preco (decrescente)")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}3{RESET}{CINZA}]{RESET}  Por stock (crescente)")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}4{RESET}{CINZA}]{RESET}  Por stock (decrescente)")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}5{RESET}{CINZA}]{RESET}  Por nome (A → Z)")
    print(f"  {CINZA}[{RESET}{BOLD}{AZUL}6{RESET}{CINZA}]{RESET}  Por categoria (A → Z)")
    print(f"  {CINZA}[{RESET}{BOLD}{VERMELHO}0{RESET}{CINZA}]{RESET}  Voltar")

    opcao = input(f"\n  {BOLD}{CIANO}>{RESET} ").strip()
    ordenado = None  # vai guardar a lista ordenada

    # sorted(lista, key=lambda p: p[X]) ordena pelo campo X do tuplo
    # reverse=True inverte a ordem (decrescente)
    if   opcao == "1": ordenado = sorted(lista, key=lambda p: p[3])               # preço crescente
    elif opcao == "2": ordenado = sorted(lista, key=lambda p: p[3], reverse=True) # preço decrescente
    elif opcao == "3": ordenado = sorted(lista, key=lambda p: p[4])               # stock crescente
    elif opcao == "4": ordenado = sorted(lista, key=lambda p: p[4], reverse=True) # stock decrescente
    elif opcao == "5": ordenado = sorted(lista, key=lambda p: p[1])               # nome A-Z
    elif opcao == "6": ordenado = sorted(lista, key=lambda p: p[2])               # categoria A-Z
    elif opcao != "0": print(f"  {VERMELHO}Opcao invalida.{RESET}")

    # Só mostra a tabela se houve ordenação
    if ordenado:
        cabecalho_tabela()
        for p in ordenado:
            imprimir_produto(p)

    if opcao != "0":
        pausa()


def menu_relatorios(lista):
    """Menu com 4 tipos de relatórios e estatísticas sobre os produtos.
    Usa funções como max(), min(), sum() e dicionários para agregar dados."""
    cabecalho_sistema("Relatorios e Estatisticas")

    print(f"\n  {CINZA}[{RESET}{BOLD}{CIANO}1{RESET}{CINZA}]{RESET}  Estatisticas gerais")
    print(f"  {CINZA}[{RESET}{BOLD}{CIANO}2{RESET}{CINZA}]{RESET}  Resumo por categoria")
    print(f"  {CINZA}[{RESET}{BOLD}{CIANO}3{RESET}{CINZA}]{RESET}  Alertas de stock baixo")
    print(f"  {CINZA}[{RESET}{BOLD}{CIANO}4{RESET}{CINZA}]{RESET}  Valor total em stock")
    print(f"  {CINZA}[{RESET}{BOLD}{VERMELHO}0{RESET}{CINZA}]{RESET}  Voltar")

    opcao = input(f"\n  {BOLD}{CIANO}>{RESET} ").strip()

    if opcao == "1":
        # Estatísticas gerais — usa max/min com key para encontrar extremos
        ativos = [p for p in lista if p[6]]  # filtra só ativos para cálculos
        precos = [p[3] for p in ativos]      # lista apenas com os preços
        mais_caro   = max(lista, key=lambda p: p[3])   # produto com maior preço
        mais_barato = min(lista, key=lambda p: p[3])   # produto com menor preço
        mais_stock  = max(lista, key=lambda p: p[4])   # produto com mais stock
        menos_stock = min(ativos, key=lambda p: p[4])  # produto ativo com menos stock

        print(f"\n  {CINZA}{'─' * 50}{RESET}")
        print(f"  {DIM}Total de produtos      :{RESET} {BOLD}{BRANCO}{len(lista)}{RESET}")
        print(f"  {DIM}Produtos ativos        :{RESET} {BOLD}{VERDE}{len(ativos)}{RESET}")
        print(f"  {DIM}Descontinuados         :{RESET} {BOLD}{VERMELHO}{len(lista) - len(ativos)}{RESET}")
        # sum()/len() para calcular a média de preços
        print(f"  {DIM}Preco medio            :{RESET} {BOLD}{AMARELO}{sum(precos)/len(precos):.2f}E{RESET}")
        print(f"  {DIM}Produto mais caro      :{RESET} {mais_caro[1]} {CINZA}({mais_caro[3]:.2f}E){RESET}")
        print(f"  {DIM}Produto mais barato    :{RESET} {mais_barato[1]} {CINZA}({mais_barato[3]:.2f}E){RESET}")
        print(f"  {DIM}Mais stock             :{RESET} {mais_stock[1]} {CINZA}({mais_stock[4]} un.){RESET}")
        print(f"  {DIM}Menos stock (ativo)    :{RESET} {menos_stock[1]} {CINZA}({menos_stock[4]} un.){RESET}")
        print(f"  {CINZA}{'─' * 50}{RESET}")

    elif opcao == "2":
        # Agrupa produtos por categoria usando um dicionário
        # Estrutura: {"categoria": {"produtos": N, "stock": N, "valor": N}}
        categorias = {}
        for p in lista:
            cat = p[2]  # campo categoria do tuplo
            if cat not in categorias:
                # Inicializa a entrada para esta categoria se ainda não existir
                categorias[cat] = {"produtos": 0, "stock": 0, "valor": 0.0}
            categorias[cat]["produtos"] += 1           # conta produtos
            categorias[cat]["stock"]    += p[4]        # soma unidades
            categorias[cat]["valor"]    += p[3] * p[4] # preço × quantidade = valor em stock

        print(f"\n  {BOLD}{CIANO}{'Categoria':<15} {'Produtos':>9} {'Stock':>8} {'Valor':>12}{RESET}")
        print(f"  {CINZA}{'─' * 48}{RESET}")
        for cat, d in sorted(categorias.items()):  # sorted ordena as categorias alfabeticamente
            print(f"  {BRANCO}{cat:<15}{RESET} {d['produtos']:>9} {d['stock']:>8} {VERDE}{d['valor']:>11.2f}E{RESET}")

    elif opcao == "3":
        # Alerta de stock baixo — o utilizador define o limite mínimo
        minimo = ler_int(f"  {CIANO}Stock minimo (ex: 50):{RESET} ")
        # Filtra produtos ativos com stock abaixo do mínimo
        criticos = [p for p in lista if p[4] < minimo and p[6]]
        if criticos:
            # Ordena por stock crescente — os mais críticos aparecem primeiro
            cabecalho_tabela()
            for p in sorted(criticos, key=lambda p: p[4]):
                imprimir_produto(p)
            print(f"\n  {AMARELO}{len(criticos)} produto(s) precisam de reposicao!{RESET}")
        else:
            print(f"\n  {VERDE}Todos os produtos tem stock suficiente.{RESET}")

    elif opcao == "4":
        # Valor total = soma de (preço × stock) para todos os produtos ativos
        valor_total = sum(p[3] * p[4] for p in lista if p[6])
        print(f"\n  {BOLD}{VERDE}Valor total em armazem: {valor_total:,.2f}E{RESET}\n")
        print(f"  {BOLD}{CIANO}{'Nome':<28} {'Valor':>12}{RESET}")
        print(f"  {CINZA}{'─' * 42}{RESET}")
        # Ordena do produto com mais valor para o com menos
        for p in sorted(lista, key=lambda p: p[3] * p[4], reverse=True):
            if p[6]:  # só mostra ativos
                print(f"  {BRANCO}{p[1]:<28}{RESET} {VERDE}{p[3]*p[4]:>11.2f}E{RESET}")

    elif opcao != "0":
        print(f"  {VERMELHO}Opcao invalida.{RESET}")

    if opcao != "0":
        pausa()


# =============================================================================
# MENU PRINCIPAL
# Ponto central do programa — mostra as opções e encaminha para os submenus.
# Usa 'global produtos' para poder modificar a lista definida fora da função.
# =============================================================================

def menu_principal():
    """Função principal que controla o fluxo do programa em loop.
    Continua a mostrar o menu até o utilizador escolher sair (opção 0)."""

    global produtos  # permite modificar a variável global 'produtos' dentro desta função

    # Lista de opções do menu: (tecla, ícone, texto, cor)
    # Separar os dados da apresentação facilita adicionar ou remover opções
    opcoes = [
        ("1", "📋", "Listar produtos",            CIANO),
        ("2", "➕", "Adicionar produto",           VERDE),
        ("3", "🗑 ", "Remover produto",            VERMELHO),
        ("4", "✏ ", "Atualizar produto",           AMARELO),
        ("5", "🔍", "Pesquisar",                   AZUL),
        ("6", "🔃", "Ordenar",                     AZUL),
        ("7", "📊", "Relatorios e estatisticas",   CIANO),
        ("8", "💾", "Exportar para CSV",           VERDE),
    ]

    while True:  # loop infinito — o programa só sai quando o utilizador escolhe 0
        cabecalho_sistema()

        # Calcula as estatísticas em tempo real para mostrar na barra de estado
        ativos  = sum(1 for p in produtos if p[6])         # conta produtos ativos
        alertas = sum(1 for p in produtos if p[4] < 50 and p[6])  # conta stock baixo

        # Barra de estado — mostra resumo rápido da loja
        print(f"\n  {CINZA}{'─' * 58}{RESET}")
        print(f"  {DIM}Produtos:{RESET} {BOLD}{BRANCO}{len(produtos)}{RESET}   "
              f"{DIM}Ativos:{RESET} {BOLD}{VERDE}{ativos}{RESET}   "
              f"{DIM}Stock baixo:{RESET} {BOLD}{AMARELO if alertas else VERDE}{alertas}{RESET}")
        print(f"  {CINZA}{'─' * 58}{RESET}\n")

        # Gera as linhas do menu dinamicamente a partir da lista 'opcoes'
        for tecla, icone, texto, cor in opcoes:
            print(f"  {CINZA}[{RESET}{BOLD}{cor}{tecla}{RESET}{CINZA}]{RESET}  {icone}  {BRANCO}{texto}{RESET}")

        print(f"\n  {CINZA}{'─' * 58}{RESET}")
        print(f"  {CINZA}[{RESET}{BOLD}{VERMELHO}0{RESET}{CINZA}]{RESET}  🚪  {DIM}Sair{RESET}")
        print(f"  {CINZA}{'─' * 58}{RESET}\n")

        opcao = input(f"  {BOLD}{CIANO}>{RESET} ").strip()

        # Encaminha para a função correta conforme a opção escolhida
        # As funções que modificam a lista devolvem a lista atualizada
        if   opcao == "1": menu_listar(produtos)
        elif opcao == "2": produtos = menu_adicionar(produtos)   # atualiza a lista global
        elif opcao == "3": produtos = menu_remover(produtos)     # atualiza a lista global
        elif opcao == "4": produtos = menu_atualizar(produtos)   # atualiza a lista global
        elif opcao == "5": menu_pesquisar(produtos)
        elif opcao == "6": menu_ordenar(produtos)
        elif opcao == "7": menu_relatorios(produtos)
        elif opcao == "8":
            cabecalho_sistema("Exportar CSV")
            nome_f = input(f"\n  {CIANO}Nome do ficheiro {CINZA}(ENTER = 'produtos_loja.csv'){CIANO}:{RESET} ").strip()
            if not nome_f:
                nome_f = "produtos_loja.csv"  # nome padrão se o utilizador não escrever nada
            exportar_csv(produtos, nome_f)
            pausa()
        elif opcao == "0":
            # Sai do loop e termina o programa
            limpar_ecra()
            print(f"\n  {VERDE}{BOLD}Ate logo! 👋{RESET}\n")
            break  # interrompe o while True
        else:
            print(f"\n  {VERMELHO}Opcao invalida. Tenta novamente.{RESET}")
            pausa()


# =============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# 'if __name__ == "__main__"' garante que menu_principal() só é chamado
# quando o ficheiro é executado diretamente (não quando é importado por outro).
# =============================================================================

if __name__ == "__main__":
    menu_principal()  # inicia o programa
