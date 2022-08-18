### here we will be discussiing docker and command for operating docker

#### Docker command and the operations

docker versiom

docker --help
dcoker container --help
docker system events ## to listing the system event when you run a docker container
docker ps -n 2 docker ps -n 3 ## list the number of container you want to list
docker container run  [optian paramter and indtruction ]  [image]
docker image ls # list image that are locally on your machine
docker image history [image id] to see the layers of the container
docker container run -itd --name redis redis:alpine
docker container run -itd  -p 8000:80 --name nginx nginx:latest #here you specified the host port of the docker on the left and teh conatainer port on the right
docker container run -itd  -P --name nginx nginx:latest # automatic port mapping where docker choos the port when u use capital P 

## so not that you can combine the docker command with linux command to troubleshot or even explor docker
docker container run centos ps
docker container run centos  uptime
docker container run centos uname -a
docker container run centos free
docker container run centos df
docker container run centos whoami
docker container run centos ls
docker container run centos  touch nkem.sh echo " sum : $((2+3)) 

### volume cmd 
docker will persist the data of container on a volume the host 

command template  docker run -idt -P --name {container_name} Volume:{/a/b/path} {container_image}
                       |
                       V
docker run  -idt -P nextcloud:/var/www/html nextcloud

docker volume create <volume_name>
docker volume list
docker volume  inspect <volume_name>

## docker Network 
 docker network list


portainer container 
- docker volume create portainer_data
- docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer

### Stoping,removing and cleaning
docker ps # to get the runing containers and then
docker pause <container_id> # this possible because the linux kenel has the ability to take away cpu from a running process.
docker unpause <container_id>
docker stop <container_id>
docker start<container_id>
docker rm <container_id> # for stopped container  remember you can remove multiple containers by running  docker rm with space separated container ids
docker rm -f <container_id> # for running container
docker container prune # will delete all stop cintaner
docker system # will list sube command that are needed for the operation
docker system prune # will do the following:
    WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - all dangling build cache

#### Docker contianer run process break down to parts and process
  when you execute docker container run 
   - you pull the image from the docker hub registry
   - you create the conatainer 
   - the container lunch sequence -->  pull the image and create the container then start the container and attach it deamon set for monitoring.

   - So when you run a container it runs and exites except you explicitely tell it to continous running

### Troubleshoot a conatainer
 first use docker ps to list the running containers
 for troubleshoting the conatainer you can either use logs or exec to the shell of the conatiner
  #### CMD for trouble shotting 
   - docker log [conatainer id or the first 3 letter of the conatainer id] or [conatainer name] that is -->
   docker logs -f [containerid]
   - The exec command show terminal of the container and also can accept one off command
   _one of command_
   - docker  exec redis ps
   - docker exec redis ifconfig
   _bash or sh_
   - docker exec redis sh

#### Cleaning,Pausing and Removing
you can use the docker pause command to pause a process this possible because linux cannel has a feature to pause or freeze a process
and being the underlining bed rock for docker and container then we can use ir

 -- docker pause <container_id>
 -- docker stop <container_id>  # is used to shot down a container and you can comma separated container_id to stop many container at once

# Packageing Application with Docker
here we are going to dymistify how to write a docker file for applications
# scenario 
imagine having three application in node js python and jave with each ways of build and packaging different 
and your supervisor ask you to design a stratgey to have this microservice build and package in an indenpendent ways and devise a one way to build and package these different apps.   
    -- Steps :
    first we need to know how to package docker manaually first then before we could leaverage the automatic way of doing it with the docker file. here is how it done
1. First clone the source code of the application [src]
2. Copy it src to an intermitent container where a version of the base image u need is either node node js or alpine or ubuntu
3. in this intermentement container using docker run  where u compile or build your source code since it has been copied
4. then you commit this container it will become an image and 
5. you will publich it to a docker registry for distribution process 

# important notes  to keep in mind when building docker manually or automaticall
  1. Port mapping is done during  the build and can not be altered in runtime or container runing state so keep that in mind
  so navigate to the /Projects/Automation/SRE/.docker/app4lfs261/example-voting-app/result and rund theis command
  [docker container run -idt --name nodebuild -p 4000:4000 node:8.16.0-alpine]
  2. next is to copy all the file in the current directory to the intermediat container in step one callde node build [docker cp . nodebuild:/app]
  3. the next step is to exec to the shell of theis intermediate container interactively [docker exec -it nodebuild sh]
  4. once you get to the terminal switch your working directory to the /app directory where you copied all the file to in step 2. then do the following linux command for due deligent
     -- pwd for working directory confirmation
     -- ps aux to see all the process runing
     -- [which node , which npm ]or which{your build agent depending on the app you are about to build}
     -- what is the version in this case node --version
  5. here in the shell of the intermediate container we run npm install for node if python python run or pip install 
      for our case in node we ran all this command 
        -- npm install {this command will read package.json to build the dependences}
        -- npm audit  # fix for vulnerability fix due to older dependencies
        -- npm ls > dependecis.txt for reference of all dependencies you installed
        -- npm test [optional if you have unit test]
        -- npm start
  6. next is you commit your docker change in the intermediate container using [docker container commit]  but you would have to pass in your docker registory username to the command so you can push it there see full command[docker container commit nodebuild nkem/result:v1]
  7. use the [docker image list] to see the image the use the [docker image history nkem/result:v1] to see the history of the image or all that has happend to the intermediate container.
  8. finally you push this image to my docker hub [ docker image push  nkem/result:v1 ]

# Building Image automatically
using docker image build we can see the process for building image automatically which comes from using the dockerfile and runing the command as shown below with tags  along side you docker reg user name
 1. Navigate to the /Projects/Automation/SRE/.docker/app4lfs261/example-voting-app/result directory    
 2. Run the command [ls to see that the dockerfile leaves in the directort,cat the dockerfile to see that the steps is like the manual process we did before] then run 
 [docker image build -t nkem/result:v2 . ] # note the dot mean from the current directory if the file is not there use the -f flag to point to the path of the dockerfile
 3. if this you finall image you can then retag as lates using the command as shown[docker image tag nkem/result:v2 nkem/result:latest]
 4. you can then push the image to the registory but cinfirm the version change

Demo1 Building docker image the manual way
##### create the intermediate container for  docker image using  command the command below
1.  docker container run -itd --name nodebuild -p 4000:4000 node:8.16.0-alpine
##### while in the directory where the source file file lives copy the src code to the intermediate container in the directory call app using the command below
2.  docker  cp  . nodebuild-2:/app
##### exec into the intermediate container  using the commnad below
3.  docker exec -it nodebuild-2 sh
##### cd and ls to change directory to app and list the content of the directory to see if the src has been copied successfuklly.
4. cd app && ls 





