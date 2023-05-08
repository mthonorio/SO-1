import operator
from in_out import open_file, write_file


def sjf_scheduling(file):
    """Run the non-preemptive SJF (Shortest Job First) scheduling algorithm on a list of processes.
    Returns a list of process IDs in the order they are executed."""
    processes = open_file(file)
    # Sort the processes by their arrival time and burst time (shortest jobs first)
    sorted_processes = sorted(processes, key=lambda p: (
        p[0], p[1]))
    # Initialize variables
    n = len(processes)
    start_times = []
    exit_times = []
    turnaround_times = [0] * n
    current_time = 0

    for process in sorted_processes:
        # Add the 0 in the end element of the process
        process.append(0)

    for i in range(n):
        ready_queue = []
        temp = []
        normal_queue = []
        for j in range(len(sorted_processes)):
            if (sorted_processes[j][0] <= current_time) and (sorted_processes[j][2] == 0):
                temp.extend(sorted_processes[j])
                ready_queue.append(temp)
                temp = []
            elif sorted_processes[j][2] == 0:
                temp.extend(sorted_processes[j])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[1])
            start_times.append(current_time)
            current_time += ready_queue[0][1]
            exit_times.append(current_time)
            for k in range(len(sorted_processes)):
                if (sorted_processes[k][0] == ready_queue[0][0]) and (sorted_processes[k][1] == ready_queue[0][1]):
                    break
            sorted_processes[k][2] = 1
            sorted_processes[k].append(current_time)

        elif len(ready_queue) == 0:
            if current_time < normal_queue[0][0]:
                current_time = normal_queue[0][0]
            start_times.append(current_time)
            current_time += normal_queue[0][1]
            exit_times.append(current_time)
            for k in range(len(sorted_processes)):
                if (sorted_processes[k][0] == normal_queue[0][0]) and (sorted_processes[k][1] == normal_queue[0][1]):
                    break
            sorted_processes[k][2] = 1
            sorted_processes[k].append(current_time)

    # Calculate average waiting and turnaround times
    total_turnaround_time = 0
    for i in range(n):
        turnaround_times = sorted_processes[i][3] - sorted_processes[i][0]
        total_turnaround_time += turnaround_times
        sorted_processes[i].append(turnaround_times)

    avg_turnaround_time = round(total_turnaround_time / n, 1)

    total_waiting_time = 0
    for r in range(n):
        waiting_time = sorted_processes[r][4] - sorted_processes[r][1]
        total_waiting_time += waiting_time
        sorted_processes[r].append(waiting_time)

    avg_waiting_time = round(total_waiting_time / n, 1)

    # Print the average waiting time and average turnaround time and average return time
    print(f'SJF {avg_turnaround_time} {avg_waiting_time} {avg_waiting_time}')
