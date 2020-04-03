import tempfile


def merge_sort(file):
    steps = 1

    with open(file, 'r') as f:
        length_f = count_lines(f)

    while steps <= length_f:
        input_file = open(file, 'r')
        f1 = tempfile.NamedTemporaryFile(mode='w+')
        f2 = tempfile.NamedTemporaryFile(mode='w+')

        k = 0
        temp = f1

        for line in input_file:
            temp.write(line)
            k += 1

            if k == steps:
                if temp.name == f1.name:
                    temp = f2
                else:
                    temp = f1
                k = 0

        input_file.close()

        length_f1 = count_lines(f1)
        length_f2 = count_lines(f2)

        input_file = open(file, 'w+')

        f1_iter = iter(f1)
        f2_iter = iter(f2)

        left = next(f1_iter)
        right = next(f2_iter)

        i = j = k = q = 0

        while i < length_f1 and j < length_f2:

            if int(left) < int(right):
                input_file.write(left)
                if i + 1 < length_f1:
                    left = next(f1_iter)
                i += 1
                k += 1
                if k == steps:
                    while q < steps:
                        input_file.write(right)
                        j += 1
                        q += 1
                        if j < length_f2:
                            right = next(f2_iter)
                        else:
                            break
                    k = q = 0
            else:
                input_file.write(right)
                if j + 1 < length_f2:
                    right = next(f2_iter)
                j += 1
                q += 1
                if q == steps:
                    while k < steps:
                        input_file.write(left)
                        i += 1
                        k += 1
                        if i < length_f1:
                            left = next(f1_iter)
                        else:
                            break
                    k = q = 0

        while i < length_f1:
            input_file.write(left)
            i += 1
            if i < length_f1:
                left = next(f1_iter)

        while j < length_f2:
            input_file.write(right)
            j += 1
            if j < length_f2:
                right = next(f2_iter)

        steps *= 2

        input_file.close()
        f1.close()
        f2.close()


def count_lines(file):
    lines = 0
    file.seek(0)

    for _ in file:
        lines += 1

    file.seek(0)

    return lines


def main():
    input_file = 'numbers.txt'

    merge_sort(input_file)


if __name__ == '__main__':
    main()
