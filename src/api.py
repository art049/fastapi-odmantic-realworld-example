import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoints.article import router as article_router
from endpoints.comment import router as comment_router
from endpoints.profile import router as profile_router
from endpoints.tag import router as tag_router
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
app.include_router(article_router, tags=["article"])
app.include_router(comment_router, tags=["article"])
app.include_router(tag_router, tags=["tag"])
app.include_router(profile_router, tags=["profile"])

if __name__ == "__main__":
    uvicorn.run(app)
