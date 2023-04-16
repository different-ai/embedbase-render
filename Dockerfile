FROM ghcr.io/different-ai/embedbase:0.9.9-minimal
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y git && apt-get clean && \
    pip install -r requirements.txt && rm requirements.txt
COPY main.py main.py

ENTRYPOINT ["uvicorn", "main:app"]
CMD ["embedbase"]