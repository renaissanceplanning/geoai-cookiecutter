import os
from config import conf
from {{cookiecutter.support_library}} import utilities

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# data pathing setup
DATA_PATH = os.getenv("DATA_PATH")  # the .env file will have this defined
PATHS = utilities.Paths(data_dir=DATA_PATH)


def func_runs():
    # define func queues within a method
    pass


def run(args):
    if args.overwrite:
        overwrite = True
    if args.argument:
        func_runs()


def main():
    # call func queues within main using an ArgParse methodology
    # todo: add more utility to this, making the download script executable
    import argparse
    parser = argparse.ArgumentParser(prog="{{cookiecutter.project_name}}",
                                     description="{{cookiecutter.description}}")
    parser.add_argument("-x", "--overwrite",    dest="overwrite",   action="store_false")
    parser.add_argument("-a", "--argument",     dest="argument",    action="store_false")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    ''' add any necessary logic up front here '''
    main()
