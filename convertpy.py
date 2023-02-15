import clipboard


filename = 'index_gen3.py'


with open(filename, 'r') as f:
    code = f.read()

code = code.replace('\\', '\\\\')

clipboard.copy(code)
print (code)


















