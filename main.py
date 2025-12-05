# main.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from routes.user import router as user_router  # <-- FONTOS

app = FastAPI()

# ----- STATIC FILES (React Build) -----
build_dir = os.path.join(os.path.dirname(__file__), "build")

app.mount("/static", StaticFiles(directory=os.path.join(build_dir, "static")), name="static")


# ----- API ROUTES -----
app.include_router(user_router, prefix="/api")   # <-- USER ROUTES importálása


# ----- REACT ROUTE -----
@app.get("/{full_path:path}")
def serve_react(full_path: str):
    index_file = os.path.join(build_dir, "index.html")
    return FileResponse(index_file)
