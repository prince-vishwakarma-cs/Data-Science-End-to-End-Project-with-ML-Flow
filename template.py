import os  # Importing the os module to interact with the operating system for file and directory management.
from pathlib import (
    Path,
)  # Importing Path from pathlib to handle file paths in a more object-oriented way.
import logging  # Importing logging to record messages that indicate the progress of the script.

# Configuring the logging settings to display messages in a specific format with a timestamp.
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(message)s")

# Setting up the project name which will be used in file paths.
project_name = "ml_project"

# Defining a list of file paths for directories and files that will be created in the project structure.
list_of_files = [
    "./github/workflows/.gitkeep",  # .gitkeep is used to keep an empty folder in Git.
    f"src/{project_name}/__init__.py",  # __init__.py files mark directories as Python packages.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",  # Common utility functions can be placed here.
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  # Configuration handling functions or classes.
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",  # Classes or methods defining entities used in configuration.
    f"src/{project_name}/constants/__init__.py",  # Constants or static configurations.
    "config/config.yaml",  # YAML configuration file for setting up project-specific settings.
    "dvc.yaml",  # DVC configuration file for data versioning.
    "params.yaml",  # Parameter file, often used for hyperparameters or project configurations.
    "schema.yaml",  # Schema definition for dataset structure.
    "main.py",  # Main script that may serve as an entry point for the project.
    "app.py",  # API entry point or web application.
    "Dockerfile",  # Dockerfile for containerizing the project.
    "requirements.txt",  # Lists project dependencies for easy installation.
    "setup.py",  # Setup script to install the package.
    "research/trials.ipynb",  # Jupyter notebook for experimentation and trials.
    "templates/index.html",  # HTML template, likely for the app frontend.
]

# Iterating over each file path in the list_of_files to create the necessary files and directories.
for filepath in list_of_files:
    filepath = Path(
        filepath
    )  # Converting the file path into a Path object for easier path handling.
    filedir, filename = os.path.split(
        filepath
    )  # Splitting into directory (filedir) and file name (filename).

    # Checking if the directory part of the path is not empty.
    if filedir != "":
        # Creating the directory (and parent directories if needed). If the directory already exists, do nothing.
        os.makedirs(filedir, exist_ok=True)
        # Logging that the directory creation is in progress.
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file doesn't exist or if it exists but is empty.
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        # Creating an empty file by opening it in write mode.
        with open(filepath, "w") as f:
            pass  # Using pass here to avoid writing anything into the file (just creates an empty file).
        # Logging that the empty file creation is complete.
        logging.info(f"Creating empty file: {filepath}")

    else:
        # Logging that the file already exists and has content, so no action is needed.
        logging.info(f"{filename} already exists")
