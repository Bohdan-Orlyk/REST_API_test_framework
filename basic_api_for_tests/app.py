import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI, Response, Request, Depends, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from services.auth_service import auth_user

from users.users import users_router

ORIGINS = ["http://localhost", "http://localhost:8000"]
ROUTERS = [users_router]


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('START')
    yield
    print("END")


app = FastAPI(
    title="Simple API for REST API test framework",
    lifespan=lifespan
)

[app.include_router(router) for router in ROUTERS]

app.add_middleware(CORSMiddleware,
                   allow_origins=ORIGINS,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )


@app.get('/')
def redirect_to_docs(request: Request):
    return RedirectResponse(f'{request.url}docs')


@app.post("/setup")
def setup(auth: None = Depends(auth_user)):
    return Response(status_code=status.HTTP_202_ACCEPTED)


if __name__ == "__main__":
    uvicorn.run(app)
