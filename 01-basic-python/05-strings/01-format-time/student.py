def format_time(h, m ,s):       
    return str(h).rjust(2, "0") + ":" + str(m).rjust(2, "0") + ":" + str(s).rjust(2, "0")

# solution :
# def format_time(h, m, s):
#    def format(x):
#        return str(x).rjust(2, '0')
#
#    h = format(h)
#    m = format(m)
#    s = format(s)
#
#    return f"{h}:{m}:{s}"