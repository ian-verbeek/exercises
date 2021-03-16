def slug(n):
    x = n.split()
    y = 1
    z = ''
    while y < len(x):
        z += f'{x[y]}-'
        y += 1
    return (z + x[0]).lower()

### solution

# def slug(n):
#     x = n.split()
#     firstn = x[0]
#     lastn = x[1:]
#    
#     return '-'.join(y.lower() for y in lastn + [firstn])