from fastapi import FastAPI

from src.api.routes import user_routes
from src.api.routes.authentication_methods import basic_auth, bearer_auth, jwt_auth
from src.database.connection import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(basic_auth.router)
app.include_router(bearer_auth.router)
app.include_router(jwt_auth.router)
