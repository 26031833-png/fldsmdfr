calif = [8.5, 7.0, 9.2, 6.5, 8.0]
print(max(calif))
print(min(calif))
print(sum(calif))
prom = sum(calif) / len(calif)
calif.sort()
calif.sort(reverse=True)
top3 = calif[:3]
aprobados = [c for c in calif if c >= 6]