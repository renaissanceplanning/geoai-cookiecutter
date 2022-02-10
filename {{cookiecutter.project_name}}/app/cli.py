import os
from config import conf
from {{cookiecutter.support_library}} import utilities
import click

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# data pathing setup
DATA_PATH = os.getenv("DATA_PATH")  # the .env file will have this defined
PATHS = utilities.Paths(data_dir=DATA_PATH)


@click.group()
def main():
    # commands with the @main.command() decorator will be added to the main group
    pass

@main.command()
@click.option('--arg_a', default=None, help='func_1')
@click.argument('arg_b', default=None, nargs=1)
def func_1(arg_a, arg_b):
    click.echo(f"example function that takes {arg_a} and {arg_b}")


if __name__ == "__main__":
    ''' add any necessary logic up front here '''
    main()
