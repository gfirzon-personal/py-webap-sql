### This command starts your FastAPI app (defined as app in main.py) using Uvicorn, and will reload on code changes. Make sure your virtual environment is activated and you have FastAPI and Uvicorn installed.
```sh
uvicorn main:app --reload
```

### run w/o reload
```sh
uvicorn main:app
```

### endpoint links
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
http://127.0.0.1:8000/vendors

