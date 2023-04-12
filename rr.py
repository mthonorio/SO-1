import struct
import timeit
from tqdm import tqdm
import operator

def open_file(fileName):
    try:
        with open(f'./tests/{fileName}', 'r') as f:
            lines=f.readlines()
            result = [
                [
                    int(processes.strip()) for processes in line.split(' ')
                ]
                for line in lines[0:]
            ]

            return result
    except:
        print('[Error]: File not found')
        exit()

def write_file(media_data, fileName):
    with open(f'./outputs/{fileName}', 'w') as output:
        for data in media_data:
            output.write(str(data))

# def quickSort(list, compare_fn):
#   if not list:
#       return list
#   pivot = list[0]
#   lesser = quickSort([x for x in list[1:] if compare_fn(x, pivot)], compare_fn)
#   greater = quickSort([x for x in list[1:] if not compare_fn(x, pivot)], compare_fn)
#   return lesser + [pivot] + greater
# print(quickSort(product_list, lambda x,y: x[0] < y[0]))

def rr_schedule(quantum, file):

    data = open_file(file) 
    data.sort(key=operator.itemgetter(0))
    print(data)

    n = len(data) # Number of processes
    queue = [] # Initialize an empty queue
    current_time = 0 # Initialize the current time to 0
    completed_processes = [] # Initialize an empty list to keep track of completed processes

    begin_time = timeit.default_timer()
    while len(completed_processes) < n: # Loop until all processes have completed execution
        for i, process in enumerate(data):
            # Check if a process has arrived and add it to the queue
            if process[0] <= current_time and i not in [p[0] for p in queue] and i not in [p[0] for p in completed_processes]:
                queue.append((i, process[0]))

        if not queue: # If the queue is empty, increment the current time and continue the loop
            current_time += 1
            continue

        # Get the first process in the queue and execute it for the quantum
        current_process = queue.pop(0)
        process_idx = current_process[0]
        process_time_left = current_process[1]

        if process_time_left > quantum:
            current_time += quantum
            process_time_left -= quantum
            queue.append((process_idx, process_time_left)) # Add the process back to the queue if it hasn't completed execution
        else:
            current_time += process_time_left
            completed_processes.append((process_idx, current_time)) # Add the process to the list of completed processes

    end_time = timeit.default_timer()

    # Sort the list of completed processes by the order in which they were completed
    completed_processes.sort(key=lambda x: x[1])
    # Create a list of tuples representing the order in which the processes were executed
    execution_order = [(process_idx, completion_time) for process_idx, completion_time in completed_processes]

    print(f'RR algorithm time: {end_time - begin_time} seconds')
    write_file(execution_order, file)
    return execution_order

def round_robin(processes, quantum):
    """
    Simulates the Round Robin scheduling algorithm for CPU scheduling.

    Args:
    processes (list): A list of dictionaries representing the processes to be scheduled. Each dictionary should
                      have the following keys: 'arrival_time' (int), 'burst_time' (int).
    quantum (int): The time quantum for the Round Robin algorithm.

    Returns:
    A list of tuples representing the order in which the processes were executed. Each tuple should have two elements:
    the index of the process in the original list (int) and the time at which it completed execution (int).
    """
    
    

    
