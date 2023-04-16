import os
import uvicorn
from embedbase import get_app

from embedbase.database.supabase_db import Supabase
from embedbase.embedding.openai import OpenAI


app = (
    get_app()
    .use_embedder(OpenAI(os.getenv("OPENAI_API_KEY")))
    .use_db(Supabase(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")))
).run()

if __name__ == "__main__":
    uvicorn.run("main:app")