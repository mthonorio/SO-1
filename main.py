import sys
from rr import rr_scheduling
from fcfs import fcfs_scheduling
from sjf import sjf_scheduling

file_path = "tests/sjf.txt"
quantum = 2

if __name__ == '__main__':
    fcfs_scheduling(file_path)
    sjf_scheduling(file_path)
    rr_scheduling(quantum, file_path)
