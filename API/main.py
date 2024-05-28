from fastapi.middleware.cors import CORSMiddleware
from block_chain import registry_voter
from model import Election, VoterInfo
from bson.json_util import dumps
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import FastAPI
import json
import os

load_dotenv()

CLIENT = MongoClient(os.getenv("MONGO_CLIENT"))
DB = CLIENT["BlockChain"]
ELECTION = DB["election"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源的请求
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有HTTP头
)

@app.get("/")
def read_root():
    return {"message": "Hello, this is central node !"}

@app.post("/register")
def register_voter(voter: VoterInfo):
    # 用來當作檢查條件
    if voter.age <= 18:
        print(f'Voter {voter.address} is not eligible.')
        pass
    else:
        try:
            registry_voter(voter.address)
            print(f'Voter {voter.address} register success.')
            return True
        except Exception as e:
            print(f"Error: {e}")
    return False

@app.get("/election")
def get_election():
    elections = ELECTION.find()
    return json.loads(dumps(list(elections)))

@app.post("/election/")
def add_election(election: Election):
    ELECTION.insert_one(election.model_dump())
    return {'msg':'add success'}

@app.delete("/election/{contract_id}")
def del_election(contract_id: str):
    ELECTION.delete_one({"contract_id":contract_id})
    return {'msg':'del success'}