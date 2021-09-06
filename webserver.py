import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import shutil
import random

app = FastAPI()


def generate_name():
    """
    Generates a new filename
    :return: returns a string of 3 words
    """
    name = ""
    with open('words.txt') as f:
        lines = f.readlines()
        for i in range(0, 3):
            name = f"{name}{lines[random.randint(0, 25486)].capitalize().strip()}"
        f.close()

    return name


@app.post("/upload")
async def upload(image: UploadFile = File(...)):
    image_filetype = image.filename.split('.')[-1]
    file_name = generate_name()

    full_name = f'{file_name}.{image_filetype}'
    with open(f'website/f/{full_name}', "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
        buffer.close()

    return JSONResponse({"file_name": full_name})


app.mount("/", StaticFiles(directory="website", html=True), name="website")
app.add_middleware(CORSMiddleware, allow_origins=["*"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
