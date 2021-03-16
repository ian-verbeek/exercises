def countdown(n):
    if n == 1:
        return "1"
    else:
        return f'{n}, {countdown(n-1)}'

### solution:

# def countdown(n):
#     return ", ".join( str(k) for k in range(n, 0, -1) )
