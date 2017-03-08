## Docker configuration

The RNA workbench docker container is rather large and expected to grow when further tools and workflows are contributed. So for users new to docker, we list here some tweaks that can help to work around issues when first using docker.
After successful installation of docker, it is recommended to configure some settings, dealing for example with the storage space required by containers.

The default storage for docker under Linux is "/var/lib/docker", which usually does not come with a lot of free space. To prevent docker from running out of disc space, one can easily change the default storage location to some more spacious partition.

To do so follow the steps here [Docker config](https://docs.docker.com/engine/admin/systemd/#custom-docker-daemon-options).

In short do:

1. service docker stop
2. backup /var/lib/docker and remove it
3. cd /etc/systemd/system/
4. mkdir docker.service.d
5. cd docker.service.d/
6. touch docker.conf
7. vim docker.conf
8. copy-paste and replace ${PATH_TO_NEW_STORAGE} with the new directory

  [Unit]  
  Description=Docker Application Container Engine  
  Documentation=https://docs.docker.com  
  After=network.target  
  
  [Service]  
  Type=notify  
  \# the default is not to use systemd for cgroups because the delegate issues still  
  \# exists and systemd currently does not support the cgroup feature set required  
  \# for containers run by docker

  ExecStart=  
  ExecStart=/usr/bin/dockerd --graph=${PATH_TO_NEW_STORAGE} --storage-driver=devicemapper  
  ExecReload=/bin/kill -s HUP $MAINPID  

  \# Having non-zero Limit*s causes performance problems due to accounting
oerhead  
  \# in the kernel. We recommend using cgroups to do container-local accounting.  
  LimitNOFILE=infinity  
  LimitNPROC=infinity  
  LimitCORE=infinity  

  \# Uncomment TasksMax if your systemd version supports it.  
  \# Only systemd 226 and above support this version.  
  \#TasksMax=infinity  
  TimeoutStartSec=0  

  \# set delegate yes so that systemd does not reset the cgroups of docker containers  
  Delegate=yes  
  \# kill only the docker process, not all processes in the cgroup  
  KillMode=process  

  [Install]  
  WantedBy=multi-user.target  

9. systemctl daemon-reload
10. systemctl start docker

After this docker should be able to launch the RNA workbench without problems.  
Kitematik users can follow the instructions [here](https://docs.docker.com/kitematic/userguide/#managing-volumes).

### Making docker usable without sudo

Please be aware that this comes with a risk, only take this steps if you have read [this](https://docs.docker.com/engine/installation/linux/linux-postinstall/) and fully understand what you are doing.  
1. sudo groupadd docker && sudo gpasswd -a ${USER} docker && sudo systemctl restart docker  
2. newgrp docker  
3. docker run ubuntu /bin/echo 'Hello world'  

