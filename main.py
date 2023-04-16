import os
import uvicorn
from embedbase import get_app

from embedbase.database.postgres_db import Postgres
from embedbase.embedding.openai import OpenAI

 
app = (
    get_app()
    .use_embedder(OpenAI(os.getenv("OPENAI_API_KEY")))
    .use_db(Postgres())
).run()

if __name__ == "__main__":
    uvicorn.run("main:app")