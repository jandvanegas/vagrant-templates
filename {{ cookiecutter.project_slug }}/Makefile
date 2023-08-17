up:
	vagrant up --provider virtualbox
	ssh-keygen -f "$(HOME)/.ssh/known_hosts" -R "[127.0.0.1]:2222"
	ansible-playbook ./dot-files/terminal-playbook.yml
down:
	vagrant destroy -f
restart:
	make down && make up
