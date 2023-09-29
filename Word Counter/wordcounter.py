li = ["PyThoN", "c", "OoP", "hello", "JaVa"]
with open('input.txt', 'r') as input:
    file = input.readlines()
for i in range(len(file)):
    file[i] = file[i].capitalize()
for i in li:
    str = (i + "\n").capitalize()
    print("{} -> {}".format(i, file.count(str)))