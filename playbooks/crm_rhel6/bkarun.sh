#!/bin/bash
export ANSIBLE_HOST_KEY_CHECKING=False
cd /opt/ansible/playbooks/crm_rhel6/
echo [web] > /opt/ansible/playbooks/crm_rhel6/vhosts
echo $1 >> /opt/ansible/playbooks/crm_rhel6/vhosts
echo [db] >> /opt/ansible/playbooks/crm_rhel6/vhosts
echo $2 >> /opt/ansible/playbooks/crm_rhel6/vhosts

echo webip: $1 > /opt/ansible/playbooks/crm_rhel6/group_vars/web
echo dbip: $2 >> /opt/ansible/playbooks/crm_rhel6/group_vars/web
echo logo: $4 >> /opt/ansible/playbooks/crm_rhel6/group_vars/web


echo webip: $1 > /opt/ansible/playbooks/crm_rhel6/group_vars/db
echo dbip: $2 >> /opt/ansible/playbooks/crm_rhel6/group_vars/db
echo sname: $3 >> /opt/ansible/playbooks/crm_rhel6/group_vars/db
echo logo: $4 >> /opt/ansible/playbooks/crm_rhel6/group_vars/db
#
ansible-playbook -i /opt/ansible/playbooks/crm_rhel6/vhosts  /opt/ansible/playbooks/crm_rhel6/site.yml
echo OUT_URL:http://$1/scrm
