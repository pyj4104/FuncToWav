from extended_int import int_inf

def heaviside(x: int, start: int, end: int = int_inf):
    if x >= start and x <= end:
        return 1
    else:
        return 0
