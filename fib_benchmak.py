import csv
from timeit import timeit

prefix = 'import fib; '
with open('./fibonacci_benchmark.csv', 'w') as reportfile:
    writer = csv.writer(reportfile)
    writer.writerow([
        'n_arg',
        'recursive_seconds',
        'iterative_seconds',
        'explicit_seconds'
    ])
    for n in range(1, 40):
        print('n={}...'.format(n), end='')
        rec = timeit('{}fib.f_recursive({})'.format(prefix, n))
        it = timeit('{}fib.f_iterative({})'.format(prefix, n))
        exp = timeit('{}fib.f_explicit({})'.format(prefix, n))
        print(' OK')
        writer.writerow([n, rec, it, exp])
