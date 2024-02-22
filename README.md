# Interview_challenge
This is my answer to the interview. Python Django is used to implement the API. A Python slim container will serve the API query. Every query is recorded in PostgreSQL container.

This is the purpose of each sub-directory under project directory:
- Chart  
  Helm Chart templates and values
- django  
  Python Django code to implement the API
- docker-compose.yml  
  Docker Compose YAML
- Dockerfile  
  Container definition
- requirements.txt  
  Python venv requirements.txt
- venv  
  Python venv
- .gitlab-ci.yml  
  Gitlab CI YAML


## How to install:
Please run this to install Helm Chart in Kubernetes:
```
helm install myweb-release Chart
```

## How to test:
Root endpoint
```
patrick@minikube:~$ curl -s http://192.168.49.2:30000/
{"version": "0.1.0", "date": 1708634337, "kubernetes": true}
```

Domain query
```
patrick@minikube:~$ curl -s http://192.168.49.2:30000/
{"version": "0.1.0", "date": 1708634337, "kubernetes": true}
```

Validate IP
```
patrick@minikube:~$ curl http://192.168.49.2:30000/v1/tools/validate/?ip_address=192.168.1.1
{"valid":true}

patrick@minikube:~$ curl http://192.168.49.2:30000/v1/tools/validate/?ip_address=1.2.3.A
{"valid":false}
```


History
```
patrick@minikube:~$ curl -s http://192.168.49.2:30000/v1/history/ | jq .
[
  {
    "id": 3,
    "domain": "www.cisco.com",
    "ip_address": "173.222.10.60",
    "created_at": "2024-02-22T20:38:49.154850Z"
  },
  {
    "id": 2,
    "domain": "www.cisco.com",
    "ip_address": "2.22.69.207",
    "created_at": "2024-02-22T20:38:03.859364Z"
  },
  {
    "id": 1,
    "domain": "www.cisco.com",
    "ip_address": "2.22.69.207",
    "created_at": "2024-02-22T20:16:35.314428Z"
  }
]
```


