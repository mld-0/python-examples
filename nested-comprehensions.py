
#   Convert 'Dict[str,Dict[str,List]]' -> 'Dict[str,Dict[str,len(List)]]'
d = { "a": { "x": [1, 2, 3], "y": [4, 5] }, "b": { "z": [6, 7, 8, 9], "w": [0], } }
print(d)
r1 = {k1: {k2: len(v2) for k2, v2 in v1.items()} for k1, v1 in d.items()}
r2 = {k1: {k2: len(d[k1][k2]) for k2 in d[k1]} for k1 in d}
assert r1 == r2
print(r1)

