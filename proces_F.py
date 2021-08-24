from data_dict import data
import time
import tracemalloc
import multiprocessing
import csv


def single_function(DATA):
    header = list(data[0].keys())
    with open('dataProc.csv', 'w', encoding='UTF8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(DATA)
    file.close()


def pool_handler():
    p = multiprocessing.Process(target=single_function(data))
    p.start()
    p.join()


if __name__ == '__main__':
    tracemalloc.start()
    start = time.time()
    pool_handler()
    print('Current %d,Peak %d' % tracemalloc.get_traced_memory())
    print('All done {}'.format(time.time()-start))
