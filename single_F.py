from data_dict import data
import time
import tracemalloc
import csv


def single_function(data):
    header = list(data[0].keys())
    with open('data.csv', 'w', encoding='UTF8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
    file.close()


tracemalloc.start()
start = time.time()
single_function(data)

print('Current %d,Peak %d' % tracemalloc.get_traced_memory())
print('All done {}'.format(time.time()-start))
