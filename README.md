# Renaissance Planning Project CookieCutter Repo

** developed and based on: [GeoAI-Cookiecutter Project Homepage](https://esri.github.io/geoai-cookiecutter)

The repo strives to streamline and promote use of best practices for interal coding projects 
through a logical, reasonably standardized, and flexible project structure.

Use of the Renaissance Planning Project CookieCutter Repo grew out of a need streamline project bootstrapping, 
encourage consistency, increase repeatability, encourage documentation, and encourage best practices.

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
- Push the newly created repo up to github

## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.

