import struct
import operator
from in_out import open_file, write_file


def rr_scheduling(quantum, file):
    # Read the file and sort the processes by arrival time
    processes = open_file(file)
    original_processes = open_file(file)

    # Initialize the variables
    n = len(processes)  # Number of processes
    executed_process = []  # List to keep track of executed processes
    current_time = 0  # Initialize the current time to 0
    # Initialize an empty list to keep track of completed processes
    completed_processes = []
    start_time = []  # List to keep track of start time of each process
    exit_time = []  # List to keep track of exit time of each process
    ready_queue = []  # List to keep track of processes in the ready queue
    response_time = [] * n  # List to keep track of response time of each process

    for process in processes:
        # Add the 0 in the end element of each process
        process.append(0)

    while 1:
        normal_queue = []
        temp = []
        for i in range(n):
            if processes[i][0] <= current_time and processes[i][2] == 0:
                present = 0
                if len(ready_queue) != 0:
                    for k in range(len(ready_queue)):
                        if processes[i][0] == ready_queue[k][0]:
                            present = 1
                # The above loop checks if the process is already present in the ready queue
                if present == 0:
                    temp.extend(processes[i])
                    ready_queue.append(temp)
                    temp = []
                # The above loop adds the process to the ready queue if it is not already present in it
                if len(ready_queue) != 0 and len(executed_process) != 0:
                    for k in range(len(ready_queue)):
                        if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                            ready_queue.insert(
                                (len(ready_queue) - 1), ready_queue.pop(k))
                # The above loop makes sure that the recently executed process is appended at the end of ready queue
            elif processes[i][2] == 0:
                temp.extend(processes[i])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        if len(ready_queue) != 0:
            if ready_queue[0][1] > quantum:
                start_time.append(current_time)
                current_time += quantum
                exit_time.append(current_time)
                executed_process.append(ready_queue[0][0])
                for j in range(len(processes)):
                    if processes[j][0] == ready_queue[0][0]:
                        break
                processes[j][1] -= quantum
                ready_queue.pop(0)
            elif ready_queue[0][1] <= quantum:
                start_time.append(current_time)
                current_time += ready_queue[0][1]
                exit_time.append(current_time)
                executed_process.append(ready_queue[0][0])
                for j in range(n):
                    if processes[j][0] == ready_queue[0][0]:
                        break
                processes[j][1] = 0
                processes[j][2] = 1
                processes[j].append(current_time)
                ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if current_time < normal_queue[0][0]:
                    current_time = normal_queue[0][0]
                if normal_queue[0][1] > quantum:
                    start_time.append(current_time)
                    current_time += quantum
                    exit_time.append(current_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(n):
                        if processes[j][0] == normal_queue[0][0]:
                            break
                    processes[j][1] -= quantum
                elif normal_queue[0][1] <= quantum:
                    start_time.append(current_time)
                    current_time += normal_queue[0][1]
                    exit_time.append(current_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(n):
                        if processes[j][0] == normal_queue[0][0]:
                            break
                    processes[j][1] = 0
                    processes[j][2] = 1
                    processes[j].append(current_time)

    # Calculate average turnaround times
    total_turnaround_time = 0
    for i in range(n):
        turnaround_time = processes[i][3] - processes[i][0]
        total_turnaround_time += turnaround_time
        processes[i].append(turnaround_time)
    avg_turnaround_time = round(total_turnaround_time / n, 1)

    # Calculate average waiting time
    total_waiting_time = 0
    for i in range(n):
        waiting_time = processes[i][4] - original_processes[i][1]
        total_waiting_time += waiting_time
        processes[i].append(waiting_time)
    avg_waiting_time = round(total_waiting_time / n, 1)

    # Print the output
    print('Average turnaround time: ', avg_turnaround_time)
    print('Average waiting time: ', avg_waiting_time)
