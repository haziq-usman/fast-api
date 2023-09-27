import logging
import sys
from llama_index import SummaryIndex, NotionPageReader
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/runquery")
async def qa(query:str):
    os.environ['OPENAI_API_KEY'] = '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'

    integration_token = "secret_Pl4SjrFzxjcxWs3dW3VRZudWaY4vxbhbtFmhpBfBDAW"
    page_ids = ["74b62523c28944f29340a7b8af9975ff"]
    documents = NotionPageReader(integration_token=integration_token).load_data(
        page_ids=page_ids
    )
    index = SummaryIndex.from_documents(documents)

    # set Logging to DEBUG for more detailed outputs
    query_engine = index.as_query_engine()
    return {"response": await query_engine.query(query).response}
