import os
import uvicorn
from embedbase import get_app

from embedbase.database.memory_db import MemoryDatabase
from embedbase.embedding.openai import OpenAI


app = (
    get_app()
    .use_embedder(OpenAI(os.getenv("OPENAI_API_KEY")))
    .use_db(MemoryDatabase())
).run()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
