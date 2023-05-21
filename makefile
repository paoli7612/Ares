runWeb:
	python3 app/runWeb.py
runEngine:
	python3 app/runEngine.py
runAres:
	python3 app/runAres.py

buildApp:
	sudo docker build -t ares ./app
runApp:
	sudo docker run -it --network bridge ares:latest

# - docker 
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