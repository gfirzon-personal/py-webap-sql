### This command starts your FastAPI app (defined as app in main.py) using Uvicorn, and will reload on code changes. Make sure your virtual environment is activated and you have FastAPI and Uvicorn installed.
```sh
uvicorn main:app --reload
```

## This tells Python to include the src directory in its module search path, so imports like from common.pretty_json_response import PrettyJSONResponse will work.
```sh
export PYTHONPATH=src
```

### run w/o reload
```sh
#uvicorn main:app
uvicorn src.main:app
```

### endpoint links
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
http://127.0.0.1:8000/vendors
http://127.0.0.1:8000/products


