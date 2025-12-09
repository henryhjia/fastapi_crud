# FastAPI SQLite CRUD Walkthrough

We have successfully migrated the application to use a persistent **SQLite** database.

## Changes Created

### File Structure
We refactored `main.py` into a modular structure:
- **`database.py`**: Configures the SQLite connection (`sql_app.db`).
- **`models.py`**: Defines the SQLAlchemy `Item` model (database table).
- **`schemas.py`**: Defines Pydantic models (data validation).
- **`main.py`**: Now uses `Session` dependency to interact with the database.
- **`main_in_memory.py`**: A backup of the original in-memory implementation.

### Git Version Control
- Initialized a git repository.
- Created `.gitignore` to exclude `.venv`, `__pycache__`, and `*.db`.
- Committed the original code and the new SQLite implementation.

## Verification Results

### Automated Verification
We ran `verify_crud.py` against the new SQLite-backed application.
**Result**: ✅ All tests passed.

### How to Run Locally
1. **Start the server**:
   ```bash
   uvicorn main:app --reload
   ```
   *This will automatically create the `sql_app.db` file if it doesn't exist.*

2. **Verify Persistence**:
   - Create an item using the API.
   - Restart the server.
   - The item will still be there!

3. **Check the Database**:
   You can inspect `sql_app.db` using the `sqlite3` command line tool or a GUI like DB Browser for SQLite.
