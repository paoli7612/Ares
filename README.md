# Ares

Welcome to the repository of the Python-Flask web app for uploading and testing code on physical devices and Docker containers.

## purpose
Develop a novel system which makes it possible to realize mixed real and simulated testbeds, where each device can be real or simulated on the PC. There is the need to use docker containers to emulate real performance.

## Description
This repository contains a web app developed with Python-Flask that allows users to upload their code and test it on physical devices such as ESP32 or ESP8266. In addition, if there are not enough physical devices available, the application is capable of emulating them by creating Docker containers.

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

### website

This Docker image allows you to create Flask web applications in Python that run in a single container.

- **auth**: With this `flask.BluePrint` we can create a new user and login
- **comunity**: With this, every user can public experiments and see other experiments
- **experiment**: We can create a new experiment, we can add a source, and then we can select how many devices load that code. Next, we can run a testbet: this experiment will be frozen, and we will receive an email when the experiment ends.
- **source**: After loading the cpp files we can also view or delete them

#### Test page
In the test page, we can test our source code: loading it or compiling the main functions. The webapp will compile the code in preparation for the selected device (esp32 or esp8266)

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or need further assistance, feel free to contact us at <a href="mailto:280873@studenti.unimore.it">280873</a>

Happy coding!