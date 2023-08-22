sudo apt update
sudo apt upgrade -y
sudo apt install ansible -y
ansible-playbook playbook.yml -i inventory.yml