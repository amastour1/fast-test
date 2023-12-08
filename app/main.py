import logging


from fastapi import FastAPI

def get_application() -> FastAPI:
    application = FastAPI(
        title="FastAPI sample",
        description="FastAPI sample",
        version="0.1.0",
        debug=True,

    )
    return application

app= get_application()

@app.get("/ping")
async def ping():
    logging.info("ping")
    return "pong"