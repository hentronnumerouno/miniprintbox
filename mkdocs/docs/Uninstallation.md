Tested on Ubuntu 22.04, other versions may work as well.

!!! warning

    Always ensure that important data is backed up before executing this script.

Clone Git Repo:

``` 
git clone https://github.com/hentronnumerouno/miniprintbox.git 
```

Begin Uninstallation:

```
cd remove
./remove.sh
```
Once the uninstallation script is completed, your system should be returned to normal (note: this script is still in development so there may be some hanging packages remaining)

!!! note "Actual build time may vary depending on system specs."
    - System Type: Virtualized (Proxmox VE 7.4-16)
    - OS Version: Ubuntu 22.04 Cloud Image
    - Link Speed: 1 GB Symmetrical
    - Disk: 60 GB (bare minimum of 10 GBs needed for install)
    - CPU Cores: 6
    - Memory: 6 GB


[![Ansible Timer](images/ansible_time.png)](images/ansible_time.png)

#### Congrats, Uninstall is now complete! Your system should now be restored to the way it was before install commenced. :material-party-popper: :material-party-popper:

