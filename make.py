from pathlib import Path
import subprocess

PROJECT_DIR = Path(__file__).parent.absolute()
SCRIPTS_DIR = Path(PROJECT_DIR, "scripts")
PACKAGE_DEPS_SCRIPT = Path(SCRIPTS_DIR, "{{cookiecutter.project_name}}/check_package_deps.py")

PROJECT_NAME = {{cookiecutter.project_name}}
SUPPORT_LIBRARY = {{cookiecutter.support_library}}
ENV_NAME = {{cookiecutter.conda_environment_name}}
ENV_NAME_ARC = {{cookiecutter.conda_arc_environment_name}}


# commands
setup_conda = ["conda", "install", "-c", "conda-forge", "mamba", "yaml", "-y"]
compile_env = ["python", PACKAGE_DEPS_SCRIPT]
build_env = ["mamba", "env", "create", "-f", "build_environment.yml"]
build_env_arc = ["mamba", "env", "create", "-f", "environment_arc.yml"]
env_activate = ["conda", "activate", ENV_NAME]
env_activate_arc = ["conda", "activate", ENV_NAME_ARC]
env_deactivate = ["conda", "deactivate"]
install_local = ["python", "-m", "pip", "install", "-e"]
remove_env = ["mamba", "env", "remove", "--name", ENV_NAME]
remove_env_arc = ["mamba", "env", "remove", "--name", ENV_NAME_ARC]


# make functions
def _command_runner(commands=None):
    try:
        for command in commands:
            subprocess.check_output(args=command,)
    except subprocess.CalledProcessError as e:
        print(e.output)


def make_env(commands=[setup_conda, compile_env, build_env, install_local, env_activate]):
    """Build the local environment from the environment file"""
    if commands is None:
        pass
    else:
        _command_runner(commands=commands)


def make_arc_env(commands=[setup_conda, build_env_arc, install_local, env_activate]):
    """Build the local environment from the environment file for arcpy"""
    if commands is None:
        pass
    else:
        _command_runner(commands=commands)


def drop_env(commands=[env_deactivate, remove_env]):
    """Remove the environment"""
    if commands is None:
        pass
    else:
        _command_runner(commands=commands)


def drop_arc_env(commands=[env_deactivate, remove_env_arc]):
    """Remove the environment for arc"""
    if commands is None:
        pass
    else:
        _command_runner(commands=commands)


def switch_branches():
    """switch local packages to project branch"""
    pass


def setup_user():
    pass
