import sys
from rr import rr_schedule

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
        if len(argV) < 1:
            return 'Not enough arguments', None
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
            rr_schedule(args['Q'], args['input_file'])
        else:
            print('Not implemented yet')