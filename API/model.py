from pydantic import BaseModel

class VoterInfo(BaseModel):
    name: str
    age: int
    id: str

class Candidate(BaseModel):
    name: str
    contract_id: str
    description: str