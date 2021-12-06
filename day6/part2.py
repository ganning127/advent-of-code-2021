f = [0]*9
for m in open("input.txt").read().split(","):
    f[int(m)] += 1
for d in range(80):
    f = f[1:]+f[:1]  # put the first element at the end of the list
    f[6] += f[8]


print(sum(f))


print(f[:1])
# sum everything into groups
