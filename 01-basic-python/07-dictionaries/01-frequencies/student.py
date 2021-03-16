def frequencies(xs):
    tel = {}

    for x in xs:
        if x in tel:
            tel[x] += 1
        else:
            tel[x] = 1
            
    return tel