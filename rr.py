import struct
import timeit
import operator
from in_out import open_file, write_file

def rr_scheduling(quantum, file):
    # Read the file and sort the processes by arrival time
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

    print("Gantt Chart:")
    print("-----------")

    # Print header row
    for p in execution_order:
        print(f"| P{p} ", end="")
    print("|")

    # Print separator
    print("+", end="")
    for i in range(len(execution_order)):
        print("----+", end="")
    print("")

    # Print timeline
    current_time = 0
    for i, p in enumerate(execution_order):
        # Print time interval
        if i == 0:
            print(f"0    {current_time + 1}    ", end="")
        else:
            print(f"{current_time}    {current_time + 1}    ", end="")
        
        # Print process ID
        if i == len(execution_order) - 1:
            print(f"P{p} |")
        else:
            print(f"P{p} ", end="")
        
        # Update current time
        current_time += 1
    return execution_order
