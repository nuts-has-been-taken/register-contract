from fastapi.middleware.cors import CORSMiddleware
from model import Election, VoterInfo
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import FastAPI
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
        return False
    else:
        return True

@app.get("/election")
def get_election():
    elections = ELECTION.find()
    return list(elections)

@app.post("/election/")
def add_election(election: Election):
    ELECTION.insert_one(election.model_dump())
    return {'msg':'add success'}

@app.delete("/election/{election_name}")
def del_election(election_name: str):
    ELECTION.delete_one({"name":election_name})
    return {'msg':'del success'}