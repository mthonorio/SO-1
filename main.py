import sys
from rr import rr_scheduling
from fcfs import fcfs_scheduling
from sjf import sjf_scheduling


def parse_args(argV):
    if len(argV) < 1:
        return 'Not enough arguments', None
    if argV[0] == '-rr':
        if len(argV) > 4:
            return 'Not enough arguments', None
        if not argV[1].isdigit():
            return 'Q must be a number', None
        return None, {'op': argV[0], 'Q': int(argV[1]), 'input_file': argV[2]}
    else:
        return None, {'op': argV[0], 'input_file': argV[1]}


if __name__ == '__main__':
    argV = sys.argv[1:]
    print(parse_args(argV))
    error, args = parse_args(argV)
    if error:
        print(f'[ERROR]: {error}')
        exit()
    else:
        if (args['op'] == '-rr'):
            rr_scheduling(args['Q'], args['input_file'])
        elif (args['op'] == '-fcfs'):
            fcfs_scheduling(args['input_file'])
        elif (args['op'] == '-sjf'):
            sjf_scheduling(args['input_file'])
