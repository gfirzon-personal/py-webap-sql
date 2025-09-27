### Build Docker image and prune orpans so not to have to delete old image
```sh
docker build -t simple-python-webapp . && docker image prune -f
```

```sh
docker run --rm -it -p 8081:8000 simple-python-webapp:latest
#docker run --rm -it -v policyhubchatbot:/app/data -p 8083:80 core-globalarchitecture-ilab-policyhub-chatbot-syncher
```

