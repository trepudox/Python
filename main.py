string = [1, 2, 3, 4, 5, 6456, 12324, 7543]

print('teste')
print('alteração na main')

for x in string:
    print(chr(x))
    if x > 1000:
        print(1001)
        for y in range(1, 1002):
            print(y)

        break
