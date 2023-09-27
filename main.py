import logging
import sys
from langchain.chat_models import ChatOpenAI
from llama_index import NotionPageReader, GPTSimpleVectorIndex, ServiceContext, LLMPredictor
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
    os.environ['OPENAI_API_KEY'] = "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"
    # integration_token = "secret_V9k7V8eN9vK31E1CET4PMzeWJ6mDfpHBXiQHZAN6LPn"
    # page_ids = ["1c4e4b7700cb4773a4df2ed8062a2ea9"]
    # print("Starting index generatation...")
    # llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo", max_tokens=512))
    # service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    # documents =  NotionPageReader(integration_token=integration_token).load_data(
    #     page_ids=page_ids
    # )
    # index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
    # index.save_to_disk("index.json")
    index = GPTSimpleVectorIndex.load_from_disk("index.json")
    response = index.query(query)
    return {"response": response.response}
