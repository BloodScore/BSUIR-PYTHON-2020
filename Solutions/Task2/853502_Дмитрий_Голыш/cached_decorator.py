def cached(func):
    prev_args = {}

    def wrapper(*args, **kwargs):
        print(f'Summing {*args, *kwargs.values()} ...')
        nonlocal prev_args

        temp_list = list(args)
        for value in kwargs.values():
            temp_list.append(value)
        args = tuple(sorted(temp_list))

        if args not in prev_args.keys():
            prev_args.setdefault(args, func(*args))
            print('Completed!')
        else:
            print('Already counted!')

        return prev_args[args]

    return wrapper


@cached
def sum_func(*args):
    s = 0

    for i in args:
        s += i

    return s

