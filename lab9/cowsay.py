from python_shell import Shell

command = Shell.cowsay('-l')

l = []
for i in command.output:
    l.append(i.decode('utf-8').split())

print(l[1:])
m = []
for i in l[1:]:
    for j in i:
        m.append(j)

print(m)
c = []
for i in m:
    c.append(Shell.cowsay('-f', i, 'HI').output)
with open('example.txt', 'w+') as f:
    k = -1
    for i in c:
        k +=1
        print(m[k], file=f)
        for j in i:
            print(j.decode('utf-8'), file=f, end='')


