from collections import defaultdict

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

def greedy_assembly(reads, k=3, verbose=False):
    """
    Ensamblaje greedy: une iterativamente el par de lecturas con mayor solapamiento.
    """
    reads = list(reads)  # copiar para no mutar entrada
    steps = []
    while len(reads) > 1:
        max_len, best_a, best_b = -1, None, None
        for i, a in enumerate(reads):
            for j, b in enumerate(reads):
                if i == j:
                    continue
                olen = overlap(a, b, min_length=k)
                if olen > max_len:
                    max_len, best_a, best_b = olen, a, b
        if max_len <= 0:
            # Sin solapamientos significativos: concatenar arbitrariamente
            merged = reads[0] + reads[1]
            chosen = (reads[0], reads[1], 0)
            reads = [merged] + reads[2:]
        else:
            merged = best_a + best_b[max_len:]
            chosen = (best_a, best_b, max_len)
            reads.remove(best_a)
            reads.remove(best_b)
            reads.append(merged)
        steps.append((chosen, merged, list(reads)))
        if verbose:
            a, b, w = chosen
            print(f"Paso: unir '{a}' -> '{b}' (overlap={w}); nuevo: '{merged}'")
    return reads[0], steps

if __name__ == "__main__":
    reads = ["ATTAC", "TACGA", "CGAAT", "GAATT"]
    genome, steps = greedy_assembly(reads, k=2, verbose=True)
    print("\nResultado final:", genome)
