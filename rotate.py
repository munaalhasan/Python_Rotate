from itertools import zip_longest
lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(line.rstrip())
        
cols=zip_longest(*lines ,fillvalue= ' ')

text='\n'.join(map(''.join,cols))

myf= open("my-output-ascii.txt","w+")
myf.write(text)
