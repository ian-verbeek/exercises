def median(ns):
    numbers = sorted(ns)
    i = len(ns) // 2
    
    if len(ns) % 2 == 0:
        return (numbers[i - 1] + numbers[i]) / 2
    else:
        return numbers[i]