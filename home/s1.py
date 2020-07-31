key = 123
data = {'a': '1', 'b': '2', 123:'3'}
if key in data:
    s = data[key]
    print(s)
else:
    print(0)