from fastapi import FastAPI
from Englis_api import bookroute
from Hindi_api import novelroute
from Tamil_api import nolroute
import uvicorn

app = FastAPI()
app.include_router(bookroute, prefix="/English_api")
app.include_router(novelroute, prefix="/Hindi_api")
app.include_router(nolroute, prefix="/Tamil_api")

@app.get('/Home')
def index():
    return "Hello"

if __name__ == "__main__":
    uvicorn.run("Nlp_main_api:app", host='127.0.0.1', port=8000, reload=True)