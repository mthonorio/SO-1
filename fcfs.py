import operator
from in_out import open_file, write_file


def fcfs_scheduling(file):
    # Read the file and sort the processes by arrival time
    processes = open_file(file)
    # Set current time to the arrival time of the first process
    current_time = processes[0][0]

    # Initialize variables
    n = len(processes)
    start_times = []
    exit_times = []
    return_times = []
    waiting_times = []

    # Iterate over processes
    for i in range(n):
        # If the process has not arrived yet, wait until it arrives
        if processes[i][0] > current_time:
            current_time = processes[i][0]
        # Set the start time of the process to the current time
        start_times.append(current_time)
        # Set the end time of the process to the current time + burst time
        end_time = current_time + processes[i][1]
        exit_times.append(end_time)
        # Set the current time to the end time of the process
        current_time = end_time
        # Calculate the waiting time of the process
        waiting_time = start_times[i] - processes[i][0]
        waiting_times.append(waiting_time)
        # Calculate the turnaround time of the process
        return_time = end_time - processes[i][0]
        return_times.append(return_time)

    # Calculate and print the average return time
    print(
        f'Average return time: {round(sum(return_times) / len(processes), 1)}')

    # Calculate and print the average waiting time
    print(
        f'Average turnaround time: {round(sum(waiting_times) / len(processes), 1)}')

    # Calculate and print the average waiting time
    print(
        f'Average waiting time: {round(sum(waiting_times) / len(processes), 1)}')
