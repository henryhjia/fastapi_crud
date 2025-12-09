# FastAPI SQLite Migration Plan

This plan outlines the steps to migrate the existing in-memory CRUD application to use a persistent SQLite database using SQLAlchemy.

## User Review Required

> [!NOTE]
> We will refactor the code into multiple files (`database.py`, `models.py`, `schemas.py`, `main.py`) for better organization, which is best practice for FastAPI with databases.
> The original in-memory version has been preserved as `main_in_memory.py`.

## Proposed Changes

### Dependencies
- Install `sqlalchemy`.

### New Files
#### [NEW] [database.py](file:///home/henryjia/Projects/fastapi_helloworld/database.py)
- Setup SQLAlchemy `create_engine`, `sessionmaker`, and `Base`.
- Use `sqlite:///./sql_app.db`.

#### [NEW] [models.py](file:///home/henryjia/Projects/fastapi_helloworld/models.py)
- Define the `Item` SQLAlchemy model (table definition).
- Columns: `id` (PK), `name` (String), `price` (Float), `is_offer` (Boolean).

#### [NEW] [schemas.py](file:///home/henryjia/Projects/fastapi_helloworld/schemas.py)
- Move Pydantic models here.
- Create `ItemBase`, `ItemCreate`, and `Item` (with `orm_mode=True`).

### Modified Files
#### [MODIFY] [main.py](file:///home/henryjia/Projects/fastapi_helloworld/main.py)
- Remove `items_db` list.
- Add `get_db` dependency.
- Update endpoints to use `Session` and query the database.

## Verification Plan

### Automated Tests
- Reuse `verify_crud.py`.
- **Note**: We may need to slightly update `verify_crud.py` if we want it to handle database cleanup between runs, OR we just accept that data persists (which is the goal).
- I will verify by running `verify_crud.py` and checking if data persists after a restart using the `sqlite3` command line tool or by restarting the server and reading the data again.

### Manual Verification
- Start server.
- Create an item.
- Restart server.
- Get the item and verify it still exists.
