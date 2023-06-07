with open("in", "w") as f:
    for i in range(100000):
        f.write(str(i + 1)+"\n")
f.close()