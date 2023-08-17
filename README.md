# Vagrant Templates

Templates to set up vagrant for different os and distributions.

## Using the repository
- Install [ansible](https://www.ansible.com/)
```bash
pipx install --include-deps ansible
```
- Install [cruft](https://pypi.org/project/cruft/)
```bash
pipx install cruft
```
- Instantiate and select options

```bash
❯ cruft create https://github.com/jandvanegas/vagrant-templates
project_name [Vagrant Templates]: My project     
project_slug [my_project]: 
author [Anonymous]: Me
Select os:
1 - ubuntu
Choose from 1 [1]: 
```