import operator
from in_out import open_file, write_file
from Process import Process


def fcfs_scheduling(file):
    # Read the file and sort the processes by arrival time
    processes = open_file(file)
    # Set current time to the arrival time of the first process
    current_time = processes[0][0]
    # Create a list of Process objects to add arrival time and burst time to each process
    processes = [Process(arrival_time, burst_time)
                 for arrival_time, burst_time in processes]

    # Iterate over processes
    for process in processes:
        # If the process has not arrived yet, wait until it arrives
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        # Set the start time of the process to the current time
        process.start_time = current_time
        # Set the end time of the process to the current time + burst time
        process.end_time = current_time + process.burst_time
        # Set the current time to the end time of the process
        current_time = process.end_time
        # Calculate the waiting time of the process
        process.waiting_time = process.start_time - process.arrival_time
        # Calculate the turnaround time of the process
        process.turnaround_time = process.end_time - process.arrival_time

    # Calculate the average waiting time
    avg_waiting_time = round(
        sum([process.waiting_time for process in processes]) / len(processes), 1)
    # Calculate the average turnaround time
    avg_turnaround_time = round(
        sum([process.turnaround_time for process in processes]) / len(processes), 1)
    # Calculate the average response time
    avg_response_time = round(sum(
        [process.start_time - process.arrival_time for process in processes]) / len(processes), 1)

    # Print the average waiting time and average turnaround time and average response time
    print(f'Average waiting time: {avg_waiting_time}')
    print(f'Average turnaround time: {avg_turnaround_time}')
    print(f'Average response time: {avg_response_time}')

    # Return the average waiting time and average turnaround time
    return avg_waiting_time, avg_turnaround_time
