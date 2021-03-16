def contains_duplicates(xs):
    i = 0
    while i < len(xs):
        y = 0
        while y < len(xs):
            if i == y:
                y += 1
            if y < len(xs):
                if xs[i] == xs[y]:
                    return True
            y += 1
        i += 1
    
    return False
            