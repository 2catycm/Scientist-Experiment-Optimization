"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/utils.ipynb.

# %% auto 0
__all__ = ['lib_init_path', 'lib_repo_path', 'runs_path', 'runs_figs_path', 'lib_directory_path']

# %% ../nbs/utils.ipynb 3
from pathlib import Path
import inspect
import Scientist_Experiment_Optimization
lib_init_path = Path(inspect.getfile(Scientist_Experiment_Optimization))
lib_init_path
lib_repo_path = lib_init_path.parent.parent
lib_repo_path
runs_path = lib_repo_path/'runs'
runs_path.mkdir(exist_ok=True, parents=True)
runs_figs_path = runs_path/'figs'
runs_figs_path.mkdir(exist_ok=True, parents=True)

# %% ../nbs/utils.ipynb 4
lib_directory_path = lib_init_path.parent
