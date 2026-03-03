print("P\tQ\tP AND Q\tP OR Q\tNOT P")
print("-" * 30)

# Caso 1
p, q = True, True
print(f"{p}\t{q}\t{p and q}\t{p or q}\t{not p}")

# Caso 2  
p, q = True, False
print(f"{p}\t{q}\t{p and q}\t{p or q}\t{not p}")

# Caso 3
p, q = False, True
print(f"{p}\t{q}\t{p and q}\t{p or q}\t{not p}")

# Caso 4
p, q = False, False
print(f"{p}\t{q}\t{p and q}\t{p or q}\t{not p}")


