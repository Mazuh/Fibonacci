import csv
from timeit import timeit

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
        rec = timeit('fib.f_recursive({})'.format(n), setup='import fib')
        it = timeit('fib.f_iterative({})'.format(n), setup='import fib')
        exp = timeit('fib.f_explicit({})'.format(n), setup='import fib')
        print(' OK')
        writer.writerow([n, rec, it, exp])
