def is_increasing(ns):
    i = 1
    while i < len(ns):
        if ns[i] < ns[i - 1]:
            return False
        i += 1
    return True

# solution:
#def is_increasing(xs):
#    for (x, y) in zip(xs, xs[1:]):
#        if x > y:
#            return False
#    return True