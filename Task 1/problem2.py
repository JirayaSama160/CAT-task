num = input()
conv = lambda x: [str(9-int(x)), x][x < '5']
ans = int(''.join(list(map(conv, num))))
print(ans)