def findDoubles(w):

    for i in range(0, len(w) - 1):
        if w[i] == w[i + 1]:
            return True
    return False

print (findDoubles("jedi"))
