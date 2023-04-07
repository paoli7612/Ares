# Ares

## purpose
Develop a novel system which makes it possible to realize mixed real and simulated testbeds, where each device can be real or simulated on the PC. There is the need to use docker containers to emulate real performance.

### makefile
```makefile
buildWeb:
	sudo docker build -t ares ./website
runWeb:
	sudo docker run -it --network bridge ares:latest
```

Then this makefile contain also short command to do usual action with docker
```makefile
ps:
	sudo docker ps -a
images:
	sudo docker image ls
containers:
	sudo docker container ls

rmi:
	sudo docker rmi -f $$(sudo docker images -aq)
stop:
	sudo docker stop $$(sudo docker ps -a -q)
	sudo docker rm $$(sudo docker ps -a -q)

deleteAll:
	sudo docker system prune -a
```

### /website

This Docker image allows you to create Flask web applications in Python that run in a single container.

- **auth**: With this `flask.BluePrint` we can create a new user and login
- **comunity**: With this, every user can public experiments and see other experiments
- **experiment**: We can create a new experiment, we can add a source, and then we can select how many devices load that code. Next, we can run a testbet: this experiment will be frozen, and we will receive an email when the experiment ends.
- **source**: After loading the cpp files we can also view or delete them

#### Test page
In the test page, we can test our source code: loading it or compiling the main functions. The webapp will compile the code in preparation for the selected device (esp32 or esp8266)



### DISPOSITIVI

### CODA