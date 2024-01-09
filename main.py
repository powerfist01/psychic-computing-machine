import logging
from fastapi import FastAPI

from app.api import home_router

app = FastAPI(
    title="Category Classifier", 
    description="Category Classifier API",
    version='0.0.1',
    contact= {
        "name": "Sujeet Singh",
        "email": "sujeet.singh@greyb.com"
    },
    keep_alive=True
)

@app.get("/")
async def root():
    '''
        Root access is granted
    '''

    return {
        "message": "Root access is granted",
        "action": "Go to /docs to see the documentation"
    }


app.include_router(home_router)
