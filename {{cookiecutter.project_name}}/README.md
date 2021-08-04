# {{cookiecutter.project_name}}

{{cookiecutter.description}}

**((Delete Everything between #######################))**
**#########################################################**
## Requirements

 * ArcGIS Pro 2.7 (soft requirement)
 * [Conda (Anaconda or miniconda)](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
 * [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0

## Install Cookiecutter lib
### Open Source Project
- open anaconda prompt as admin
    ``` cmd
    > conda install -c conda-forge cookiecutter
    ```
### ESRI Project
- open anaconda prompt for Arcgis Pro (Start / Arcgis / Python Command Prompt)
    ``` cmd
    > conda install -c conda-forge cookiecutter
    ```

### To start a new project, run:
- Open anaconda prompt and change directory (choose anaconda prompt according to project type)
    ``` cmd
    > cd path/to/local/install
    
     ex: --> cd C:\github\projects
    ```
    ``` cmd
    > cookiecutter https://github.com/renaissanceplanning/renplan-esri-cookiecutter
    ```
  - follow the prompts 
- Update README by removing CookieCutter install and setup instructions
- Push the newly created repo up to github
        
**((Delete Everything between #######################))**
**#########################################################**


## Next

1 - Clone this repo.

2 - Create an environment with the requirements. Assumes the project originator has spent time currating the environment
appropriately. There are default libraries in each project type `.yml` that will at least get you started.

  - if setting up an open source project
    ``` cmd
    > make env
    ```
  - if setting up an ESRI project
    ``` cmd
    > make env_arc
    ```

3 - Explore - If you are more into Python, a good place to start is `jupyter lab` from the root of the project, and 
look in the `./notebooks` directory. If GIS is more your schtick, open the project `./arcgis/{{cookiecutter.project_name}}.aprx`.

## Using Make - common commands

Based on the pattern provided in the Cookiecutter Data Science template by Driven Data this template streamlines a 
number of commands using the make command pattern.

- `make env` - builds the Conda environment with all the name and dependencies from `environment_dev.yml` and installs the local project package `{{cookiecutter.support_library}}` using the command `python -m pip install -e ./src/src/{{cookiecutter.support_library}}` so you can easily test against the package as you are developing it.


- `make env_clone` - designed for environments using the default Conda instance installed with ArcGIS Pro. It is similar to `make env`, except this command clones the `arcgispro-py3` environment. Otherwise, it still installs the packages listed in `environment_dev.yml` and installs the local package using `pip` as described above.


- `make docs` - builds Sphinx docs based on files in `./docsrc/source` and places them in `./docs`. This enables easy publishing in the master branch in GitHub.


- `make test` - activates the environment created by the `make env` or `make env_clone` and runs all the tests in the `./testing` directory using PyTest. Alternately, if you prefer to use [TOX](https://tox.readthedocs.io) for testing (my preference), there is a `tox.ini` file included as well. The dependencies (`tox` and `tox-conda`) for using TOX are included in the default requirements. By default, the TOX file creates an environment from the `environment.yml` file using much fewer dependencies than the `*_dev.yml` files.


4 - What else?

### Optional Folders to Utilize
    1 - conda-build (used for generating a conda package from your src folder)

    2 - conda-recip (folder intended to hold the code to build the conda package)

    3 - docs/docsrc (folders to generate the project level documentation from code docstrings and project RST)


### Project Organization
_______________________
```
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data`
    ├── make.bat           <- Windows batch file with commands like `make data`
    ├── setup.py           <- Setup script for the library ({{ cookiecutter.support_library }})
    ├── .env               <- Any environment variables here - created as part of project creation, 
    │                         but NOT syncronized with git repo for project.                
    ├── README.md          <- The top-level README for developers using this project.
    ├── arcgis             <- Root location for ArcGIS Pro project created as part of
    │   │                     data science project creation.
    │   ├── {{ cookiecutter.project_name }}.aprx <- ArcGIS Pro project.    
    │   └── {{ cookiecutter.project_name }}.tbx  <- ArcGIS Pro toolbox associated with the project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks. Naming convention is a 2 digits (for ordering),
    │   │                     descriptive name. e.g.: 01_exploratory_analysis.ipynb
    │   └── notebook_template.ipynb
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    ├── environment.yml    <- Requirements file for reproducing the analysis execution environment.
    │                         This includes far fewer dependencies and does not include arcpy.
    ├── environment_dev.yml<- Requirements file for reproducing the analysis deveopment environment.
    │                         This includes arcpy and everything needed to generate Sphinx docs.
    └── src                <- Source code for use in this project - all scripts, modules and code.
        └── {{ cookiecutter.support_library }} <- Library containing the bulk of code used in this 
                                                  project. 
```

<p><small>Project based on the <a target="_blank" href="https://github.com/Esri/cookiecutter-spatial-data-science">cookiecutter 
spatial data science project template</a>. This template, in turn, is simply an extension and light modification of the 
<a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data 
science project template</a>. cookiecutterdatascience</small></p>
