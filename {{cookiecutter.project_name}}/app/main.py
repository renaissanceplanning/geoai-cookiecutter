from config import conf
from {{cookiecutter.support_library}} import utilities

# data pathing setup
DATA_PATH = conf.DATA_PATH
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
