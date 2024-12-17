import sys


def rot(A, i):
    B = 0
    for i in range(i):
        B = (A % 8) ^ 3
        C = A // 2**B
        B = B ^ C ^ 5
        A = A // 8
    return B % 8


PROG = [2, 4, 1, 3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]

if len(sys.argv) > 1:
    print([rot(int(sys.argv[1]), i + 1) for i in range(16)])
    print(PROG)
else:
    for i, v in enumerate(PROG):
        x = 0
        f = 0
        while True:
            if rot(x, i + 1) == v:
                print(x, end=" ")
                if f > 63:
                    print()
                    break
                f += 1
            x += 1


# 4 + 8*x


# 8
# 64
# 8**3
