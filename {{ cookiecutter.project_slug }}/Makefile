ansible_config := ./vagrant/ansible.cfg
up:
	vagrant up --provider virtualbox
	ssh-keygen -f "$(HOME)/.ssh/known_hosts" -R "[127.0.0.1]:2222"

	export ANSIBLE_CONFIG=$(ansible_config); \
		ansible-playbook ./dot-files/playbooks/terminal-playbook.yml --connection local --ask-become-pass

down:
	vagrant destroy -f
restart:
	make down && make up
