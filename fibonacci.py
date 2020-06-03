#!/usr/bin/env python3
import argparse
import logging
import time
import threading
import random

'''
Global Variables
'''
DEBUG = False
VERBOSE = False

MESSAGE_TYPE = {
        'debug': 'debug',
        'info': 'info',
        'warning': 'warning',
        'critical': 'critical'
        }

'''
Classes and Functions
'''
def log(message, message_type=MESSAGE_TYPE['info']):
    '''
    Logs messages to the user and the logger
    '''
    global VERBOSE
    global DEBUG
    global MESSAGE_TYPE
    if VERBOSE: 
        print (message)
    elif DEBUG or message_type == MESSAGE_TYPE['debug']:
        print (message)
        logging.debug(message)
    elif message_type == MESSAGE_TYPE['info']:
        logging.info(message)
    elif message_type == MESSAGE_TYPE['warning']:
        logging.warning(message)
    elif message_type == MESSAGE_TYPE['critical']:
        logging.critical(message)
    return


def fibonacci(function_id, max_index=10):
    data = [0 for x in range(max_index)]
    data[0] = 1
    data[1] = 1
    i = 0
    j = 1
    for value in range(2, max_index):
        log('Fibonacci function {} calculating...'.format(function_id))
        data[value] = data[i] + data[j]
        i += 1
        j += 1
    log('Fibonacci {} is done it\'s sequence of {} fibonacci numbers\n{}'.format(function_id, max_index, data))
    return

'''
Main runner
'''
def get_args():
    '''
    Gets the arguments for the user

    Returns the arguments from the user in a Key,Value Namespace.
    '''
    description = '''
    Python Threading Tutorial 

    Please see the README for more details.

    Created by Spencer Pollock (spencer@spollock.ca)
    '''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-n', '--number-of-runs', dest='numberofruns', type=int, default=2, help='Number of times to run the fibonacci sequence')

    parser.add_argument('--verbose', action='store_true', help='Run the program in verbose mode')
    parser.add_argument('--debug', action='store_true', help='Run the program in debug mode')
    return parser.parse_args()

def main(args):
    global DEBUG
    global VERBOSE
    global MESSAGE_TYPE
    DEBUG = args.debug
    VERBOSE = args.verbose
    if (DEBUG):
        log('Debug mode is {}'.format(DEBUG), MESSAGE_TYPE['info'])
    if (VERBOSE):
        log('Verbose mode is {}'.format(VERBOSE), MESSAGE_TYPE['info'])
    start_time = time.time()
    for i in range(0, args.numberofruns):
        fibonacci(i, random.randint(1500,2000))
    log('All fibonacci functions complete', MESSAGE_TYPE['info'])
    log('Took {} time to run {} Fibonacci functions'.format(time.time() - start_time, args.numberofruns))
    return 0

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s = %(message)s', filename='fibonacci.log', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
    main(get_args())
    logging.shutdown()
