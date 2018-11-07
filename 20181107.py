stuff='Hello\nWorld!'
stuff
print(stuff)
fhand=open('mbox.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])
fhand=open('mbox.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
