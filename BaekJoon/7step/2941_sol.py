texts = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
for text in texts:
    a = a.replace(text, '*')
print(len(a))