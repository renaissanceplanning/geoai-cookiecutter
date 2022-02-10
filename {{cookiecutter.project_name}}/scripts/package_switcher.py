"""
1) check to see if the repo is already local
2) if not, clone it
3) if it is, set branch to (DEV_INIT)
4) pull the latest changes
6) create a new branch from the package with the project name as the branch [dev-init-project-name]
"""
from git.repo import Repo
from pathlib import Path
from check_package_deps import Environment

RP_GITHUB_URL = "https://github.com/renaissanceplanning"
PROJECT_DIR = Path(__file__).parent.parent
PACKAGES_DIR = PROJECT_DIR.parent / 'packages'

# assumes all branches of our packages will be branches off of whatever is provided here
DEFAULT_BRANCH = "DEV_INIT"
BASE_BRANCH = {{cookiecutter.package_base_branch}}
PROJECT_NAME = {{cookiecutter.project_name}}
ENVIRONMENT_YML = Path(PROJECT_DIR, 'environment.yml')

environment = Environment(ENVIRONMENT_YML)


def locate_local_package(package_name):
    """
    Given a package name, check it it exists in the packages directory
    """
    pkg_path = Path(PACKAGES_DIR, package_name)
    if pkg_path.exists():
        return pkg_path


def check_branch(package_path, branch_name):
    """
    Given a package path and a branch name, check if the branch exists in the package
    """
    repo = Repo(package_path)
    if branch_name in repo.branches:
        return True
    return False


def main():
    # identify local packages in the environment and clone if they don't exist
    for package in environment.local_packages:
        pkg_path = locate_local_package(package)
        prj_repo_name = f"{DEFAULT_BRANCH}-{PROJECT_NAME}"
        # if package is local, switch to base branch "dev-init"
        if pkg_path:
            # switch branch to dev_init
            repo = Repo(pkg_path)
            if repo.active_branch.name != BASE_BRANCH:
                repo.git.checkout(BASE_BRANCH)
                repo.git.pull()
        # otherwise clone the package from github
        else:
            print(f'Cloning {package}')
            repo = Repo.clone_from(url=f'{RP_GITHUB_URL}/{package}', to_path=str(pkg_path), branch=BASE_BRANCH)

        # check if the project branch exists, if not create it
        if not check_branch(pkg_path, prj_repo_name):
            repo.create_head(prj_repo_name)
        # check out the project branch and push up to github
        repo.git.checkout(prj_repo_name)
        repo.git.push()


if __name__ == "__main__":
    main()