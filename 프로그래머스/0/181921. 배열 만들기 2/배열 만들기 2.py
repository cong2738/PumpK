def solution(l, r):
    ret = []
    def f(lim, val):
        if lim == 0:
            ret.append(val)
            return

        f(lim - 1, val * 10 + 5)
        f(lim - 1, val * 10)

    f(6, 0)

    return list(i for i in ret if l <= i <= r)[::-1] or [-1]
