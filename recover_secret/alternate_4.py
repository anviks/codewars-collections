def recover_secret(a):
    out = list(zip(*a))
    h = [j for j in (set(out[0]) - set(out[1] + out[2]))]
    for i in a:
        if i[0] in h:
            i[:2], i[2] = i[1:], ''

    return h[0] + recover_secret(a) if h else str()
