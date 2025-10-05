from collections import defaultdict, Counter

def overlap(a, b, min_length=3):
    """
    Longitud del solapamiento máximo entre el final de 'a' y el inicio de 'b'.
    """
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def build_overlap_graph(reads, k=3):
    """
    Grafo dirigido de solapamientos: edge a->b con peso = overlap(a,b).
    """
    G = defaultdict(dict)
    for i, a in enumerate(reads):
        for j, b in enumerate(reads):
            if i == j:
                continue
            olen = overlap(a, b, min_length=k)
            if olen > 0:
                G[a][b] = olen
    return G

def greedy_layout(G):
    """
    Layout aproximado:
    - Mantiene a lo sumo 1 arista saliente y 1 entrante por nodo (tipo camino).
    - Elige siempre la arista saliente de mayor peso que no forme ciclo.
    - Empieza desde un nodo con indegree 0 si existe.
    """
    out_choice = {}
    indeg = Counter()
    # ordenar candidatos por peso (mayor primero)
    edges = []
    for u in G:
        for v, w in G[u].items():
            edges.append((w, u, v))
    edges.sort(reverse=True)

    parent = {}
    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    # seleccionar aristas evitando ciclos y manteniendo grado <=1
    in_choice = {}
    nodes = set(G.keys()) | {v for u in G for v in G[u]}
    for w, u, v in edges:
        if u in out_choice or v in in_choice:
            continue
        # evitar ciclo: si unir u->v crea un ciclo, saltar
        if find(u) == find(v):
            continue
        out_choice[u] = (v, w)
        in_choice[v] = (u, w)
        union(u, v)
        indeg[v] += 1

    # encontrar inicio (nodo sin entrante) y construir camino
    starts = [n for n in nodes if n not in in_choice]
    start = starts[0] if starts else next(iter(nodes))
    order = [start]
    while order[-1] in out_choice:
        order.append(out_choice[order[-1]][0])

    return order  # lista de lecturas en orden

def consensus_from_layout(order, k=3):
    """
    Genera consenso concatenando lecturas según solapamiento estimado.
    (Versión simple: usa el solapamiento máximo local entre consecutivas).
    """
    if not order:
        return ""
    consensus = order[0]
    for i in range(1, len(order)):
        a, b = consensus, order[i]
        # buscar mejor solapamiento entre 'consensus' y 'b'
        maxo = overlap(a, b, min_length=k)
        consensus = a + b[maxo:]
    return consensus

# ----- Ejemplo de uso didáctico -----
if __name__ == "__main__":
    reads = [
        "ATTAC",
        "TACGA",
        "CGAAT",
        "GAATT"
    ]

    k = 2  # umbral de solapamiento mínimo (para ejemplo)
    G = build_overlap_graph(reads, k=k)
    layout = greedy_layout(G)
    cons = consensus_from_layout(layout, k=k)

    print("Orden (layout) de lecturas:")
    for r in layout:
        print(" -", r)
    print("\nConsenso:", cons)
