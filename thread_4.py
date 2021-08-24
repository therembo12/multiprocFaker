from data_dict import count
from data_dict import data
import time
import tracemalloc
import threading
import csv


def single_function(data):
    header = ['name', 'login', 'password', 'address']
    with open('dataThread.csv', 'w', encoding='UTF8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerow(data)
    file.close()


if __name__ == '__main__':
    tracemalloc.start()
    start = time.time()

    threads = []
    for item in range(count+1):
        thread = threading.Thread(
            target=single_function, args=(item,))
    threads.append(thread)
    thread.start()
    for thread in threads:
        thread.join()

    print('Current %d,Peak %d' % tracemalloc.get_traced_memory())
    print('All done {}'.format(time.time()-start))
