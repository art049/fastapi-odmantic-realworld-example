import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoints.user import router as user_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


app.include_router(user_router, tags=["user"])

if __name__ == "__main__":
    uvicorn.run(app)
