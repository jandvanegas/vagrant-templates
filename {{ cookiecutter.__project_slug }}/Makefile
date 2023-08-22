current_folder := $(notdir $(CURDIR))
ansible_config := ./vagrant/ansible.cfg
up:
	vagrant up --provider virtualbox
	ssh-keygen -f "$(HOME)/.ssh/known_hosts" -R "[127.0.0.1]:2222"

my-env: up
	export ANSIBLE_CONFIG=$(ansible_config); \
		ansible-playbook ./vagrant/my-playbook.yml

down:
	vagrant destroy -f

restart:
	make down && make up

ssh-config:
	vagrant ssh-config --host $(current_folder) >> ~/.ssh/config
