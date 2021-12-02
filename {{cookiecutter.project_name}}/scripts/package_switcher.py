# TODO: setup this script to checkout the correct branch and create a new project branch
import git
from pathlib import Path
from check_package_deps import Environment

PROJECT_DIR = Path(__file__).parent.parent
PACKAGES_DIR = PROJECT_DIR.parent / 'packages'

# assumes all branches of our packages will be branches off of whatever is provided here
INITIAL_BRANCH = {{cookiecutter.package_base_branches}}
PROJECT_NAME = {{cookiecutter.project_name}}
ENVIRONMENT_YML = Path(PROJECT_DIR, 'environment.yml')

environment = Environment(ENVIRONMENT_YML)
# identify local packages in the environment


"""
1) check to see if the repo is already local
2) if not, clone it
3) if it is, set branch to (DEV_INIT)
4) pull the latest changes
6) create a new branch from the package with the project name as the branch [dev-init-project-name]
"""