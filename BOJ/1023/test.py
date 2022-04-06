
num = 4
unit = "01"
ret = [unit]
for i in range(num - 1):
    tmp_l = set()
    for j in ret:
        for k in range(3):
            tmp_s = list(unit)
            tmp_s.insert(k, j)
            tmp_l.add("".join(tmp_s))
    tmp_l = list(tmp_l)
    ret = tmp_l
res = []
for i in ret:
    res.append(int(i, 2))
res.sort()
print(res)