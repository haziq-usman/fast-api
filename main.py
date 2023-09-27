import logging
import sys
from llama_index import SummaryIndex, NotionPageReader
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/runquery")
def qa(query:str):
    integration_token = "secret_Pl4SjrFzxjcxWs3dW3VRZudWaY4vxbhbtFmhpBfBDAW"
    page_ids = ["74b62523c28944f29340a7b8af9975ff"]
    documents = NotionPageReader(integration_token=integration_token).load_data(
        page_ids=page_ids
    )
    index = SummaryIndex.from_documents(documents)

    # set Logging to DEBUG for more detailed outputs
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return {"response": response.response}
