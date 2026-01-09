# FastAPI CRUD
## Project Overview

**FastAPI CRUD** is a FastAPI web application designed to perform CRUD operations in memory or on a SQLite database, or on a PostgreSQL database.


## Project Structures
  ```
    1  /home/henryjia/Projects/fastapi_crud/
    2  ├── main.py
    3  ├── main_sqlite.py
    4  ├── main_postgresql.py
    5  ├── main_in_memory1.py
    6  ├── main_in_memory2.py
    7  ├── verify_crud.py
    8  ├── database.py
    9  ├── models.py
    10 ├── schemas.py
    11 └── README.md
  ```

## Program Explaination

### main.py
```
fast api application for perform CRUD. Data are in sqlite database sql_app.db.  It uses multple helper files: database.py, models.py, schemas.py, verify_crud.py.
```

### main_sqlite.py
```
fast api application for perform CRUD. Data are in sqlite database item.db. Standalone version.
```

### main_postgresql.py
```
fast api application for perform CRUD. Data are in postgresql database item.db. Standalone version.
```

### main_in_memory1.py
```
fast api application for perform CRUD. In memory version. Use a list of Item objects (text, isdone) to store data.
```

### main_in_memory2.py
```
fast api application for perform CRUD. In memory version. Use a list of Item objects (id, name, price, is_offer) to store data.
```

### verify_crud.py
```
verify CRUD operations for main.py. 
```

### database.py
```
helper file for database connection for main.py.
```

### models.py
```
define the database models for main.py.
```

### schemas.py
```
define the data schemas for main.py.
```

## Running the Application Locally
1. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```   
3. **Start the FastAPI application**
   ```bash
   uvicorn app.main:app --reload
   ```
4. **Open the app in your browser**
   ```bash
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) 
   ```
5. **run verify_crud.py to verify CRUD operations for main.py**
   ```bash
   python3 verify_crud.py
   ```
     
     