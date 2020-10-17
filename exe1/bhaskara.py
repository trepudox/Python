#                                a² + bx + c = 0
#                                -b +- (b**2 - 4*a*c)
def bhask(a, b, c):
    raiz = (b ** 2) - (4 * a * c)
    x1 = (-b + raiz) / 2
    x2 = (-b - raiz) / 2
    return x1, x2

aa = input('Digite o valor de a: ')
bb = input('Digite o valor de b: ')
cc = input('Digite o valor de c: ')
a = 0
b = 0
c = 0

if (aa or bb or cc).startswith('-'):
    a = aa.replace('-', '')
    b = bb.replace('-', '')
    c = cc.replace('-', '')
    if not (a or b or c).isnumeric():
        print('\nPor favor digite valores válidos.')
    else:
        a = int(a)
        b = int(b)
        c = int(c)
else:
    if not (aa or bb or cc).isnumeric():
        print('\nPor favor digite valores válidos.')
    else:
        a = int(aa)
        b = int(bb)
        c = int(cc)

if not (a or c or b):
    pass
else:
    if (aa or bb or cc).startswith('-'):
        if aa.startswith('-'):
            a = - a
        if bb.startswith('-'):
            b = - b
        if cc.startswith('-'):
            c = - c
        print()
        print(bhask(a, b ,c))
    else:
        print()
        print(bhask(a, b, c))

