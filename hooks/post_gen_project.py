import os
import shutil


def remove(filepath: str) -> None:
    """Function to remove a folder.

    Args:
        filepath (str): Path to folder to remove.
    Returns:
        None
    """
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


available_oses = ['debian']
selected_os = {{cookiecutter.os}}


for item in os.listdir(selected_os):
    shutil.move(item, '.')

for current_os in available_oses:
    remove(current_os)