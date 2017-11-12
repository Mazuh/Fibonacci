import csv
from timeit import timeit

prefix = 'import fib; '
with open('./report.csv', 'w') as reportfile:
  writer = csv.writer(reportfile)
  writer.writerow([
    'n_arg',
    'recursive_time',
    'iterative_time',
    'explicit_time'
  ])
  for n in range(1, 40):
    print('n=', n, '...', end='')
    rec = timeit('{}fib.f_recursive({})'.format(prefix, n))
    it = timeit('{}fib.f_iterative({})'.format(prefix, n))
    exp = timeit('{}fib.f_explicit({})'.format(prefix, n))
    print(' OK')
    writer.writerow([n, rec, it, exp])
