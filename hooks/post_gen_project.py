import os
import shutil
import subprocess


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


available_oses = ['ubuntu', 'debian']
selected_os = '{{cookiecutter.os}}'.split('/')[0]


for item in os.listdir(selected_os):
    shutil.move(os.path.join(selected_os, item), '.')

for current_os in available_oses:
    remove(current_os)


subprocess.call(['git', 'init'])
subprocess.call(['git', 'submodule', 'add', 'https://github.com/jandvanegas/dot-files.git'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'chore: Initial commit'])