from config import conf
from {{cookiecutter.support_library}} import utilities

# data pathing setup
DATA_PATH = conf.DATA_PATH
PATHS = utilities.Paths(data_dir=DATA_PATH)