## Because sometimes it just doesn't work...
Please note that these are the failures modes discovered during testing and are by no means exclusive to the failures that may arise during use. Please open a pull request with the issues and issue description so it can be added to the troubleshooting documentation. https://github.com/hentronnumerouno/miniprintbox/pulls
### Failure Modes:

#### No image in Octoprint or Obico?
- Cause 1:
    - Not all browsers support Avahi for network resolution of .local domains
- Fix 1:
    - Change browser to Firefox
- Cause 2: 
    - Check to see if miniprintbox.local is resolvable on the local network.
- Fix 2:
    - Open a terminal or windows command prompt and ping miniprintbox.local.

#### Octoprint reset to defaults?
- Cause 1:
    - Can occur when the "rebuild-octoprint.sh" script is run outside of the ansible-playbook
- Fix 1: 
    - Find running containers using `docker ps` or `sudo docker ps` depending on privileges.
    - Stop the Octoprint docker container with `docker stop octoprint_octoprint_1`
    - Delete the running Ocotoprint container with `docker rm octoprint_octoprint_1`
    - Delete the 3rd octoprint folder that will be created in this path:
    `user@test-os:~/Documents/miniprintbox/install/octoprint/octoprint/octoprint`
    - Change the current directory to `wherever_you_cloned_the_repo/miniprintbox/install/octoprint`
    - Rebuild the container `docker-compose up -d --force-recreate`
- Cause 2:
    - Breaking change from Octoprint update
- Fix 2: 
    - Confirm that the docker image used for Octoprint is `octoprint/octoprint@sha256:f50ab403cec9979562b0a9da31167d36d653dad1b9271589603e44caf42517f0`.