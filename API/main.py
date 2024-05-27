from model import Candidate, VoterInfo
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import FastAPI
import os

load_dotenv()

CLIENT = MongoClient(os.getenv("MONGO_CLIENT"))
DB = CLIENT["BlockChain"]
CANDIDATE_COL = DB["candidate"]

app = FastAPI()

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

@app.get("/candidate")
def get_candidate():
    candidates = CANDIDATE_COL.find()
    return list(candidates)

@app.post("/candidate/")
def add_candidate(candidate: Candidate):
    CANDIDATE_COL.insert_one(candidate.model_dump())
    return {'msg':'add success'}

@app.delete("/candidate/{candidate_name}")
def del_candidate(candidate_name: str):
    CANDIDATE_COL.delete_one({"name":candidate_name})
    return {'msg':'del success'}