import struct
import timeit
import operator


def open_file(fileName):
    try:
        with open(f'./tests/{fileName}', 'r') as f:
            lines = f.readlines()
            result = [
                [
                    int(processes.strip()) for processes in line.split(' ')
                ]
                for line in lines[0:]
            ]

            result.sort(key=operator.itemgetter(0))
            return result
    except:
        print('[Error]: File not found')
        exit()


def write_file(media_data, fileName):
    with open(f'./outputs/{fileName}', 'w') as output:
        for data in media_data:
            output.write(str(data))
