from collections import defaultdict, Counter
import networkx as nx

def kmers(seq, k):
    for i in range(len(seq) - k + 1):
        yield seq[i:i+k]

def build_debruijn(reads, k=3):
    """
    Grafo de de Bruijn:
    - Nodos: (k-1)-mers
    - Aristas dirigidas: k-mers (u -> v) donde u = prefijo y v = sufijo
    Devuelve (G, in_deg, out_deg) como dicts simples para uso didáctico.
    """
    G = defaultdict(list)
    in_deg = Counter()
    out_deg = Counter()
    for read in reads:
        for kmer in kmers(read, k):
            u = kmer[:-1]
            v = kmer[1:]
            G[u].append(v)
            out_deg[u] += 1
            in_deg[v] += 1
            # asegurar presencia de nodos aislados
            _ = G[v]
    return G, in_deg, out_deg

def find_eulerian_path(G, in_deg, out_deg):
    """
    Hierholzer simplificado para encontrar camino euleriano si existe.
    """
    # determinar nodo de inicio
    start = None
    for v in set(list(G.keys()) + [w for vs in G.values() for w in vs]):
        outd = out_deg[v]
        ind = in_deg[v]
        if outd == ind + 1:
            start = v
            break
    if start is None:
        # caer alfabéticamente o cualquiera con aristas
        start = next((v for v in G if G[v]), next(iter(G)))
    # copiar estructura para consumir aristas
    adj = {u: list(vs) for u, vs in G.items()}
    path, stack = [], [start]
    while stack:
        v = stack[-1]
        if adj.get(v):
            u = adj[v].pop()
            stack.append(u)
        else:
            path.append(stack.pop())
    path.reverse()
    return path  # secuencia de nodos (k-1)-mers

def contig_from_path(path):
    """
    Reconstruye contig a partir de la lista de (k-1)-mers.
    """
    if not path:
        return ""
    contig = path[0]
    for node in path[1:]:
        contig += node[-1]
    return contig

if __name__ == "__main__":
    # Ejemplo de juguete
    reads = ["ATTAC", "TACGA", "CGAAT", "GAATT"]
    k = 3  # k-mers de longitud 3 -> nodos de longitud 2
    G, in_deg, out_deg = build_debruijn(reads, k=k)
    path = find_eulerian_path(G, in_deg, out_deg)
    contig = contig_from_path(path)
    print("Camino euleriano (nodos):", " -> ".join(path))
    print("Contig reconstruido:", contig)
