HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def print_error(message=""):
    print(f'{FAIL} --> {BOLD}{message}{ENDC}')


def print_ok(message=""):
    print(f'{OKGREEN} --> {BOLD}{message}{ENDC}')


def printy(message=""):
    print(f'{OKGREEN} --> {ENDC}{BOLD}{message}{ENDC}')


def printWarning(message=""):
    print(f'\n{BOLD}{WARNING} --> {message}{ENDC}\n')
