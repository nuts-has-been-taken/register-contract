# Description

This is a project for block-chain class in **National Yang Ming Chiao Tung University**.

This project is a simple E-voting system based on blockchain.

# Unit

This project requires the following components to run:

- Frontend (Vue)
- Backend (FastAPI)
- Blockchain node (hardhat/or your test net)
- Database (MongoDB)

# Install

```bash
git clone https://github.com/nuts-has-been-taken/register-contract.git
cd register-contract```

# Run

## hardhat node (run the chain in local)

start the hardhat chain with their example

```python
git clone https://github.com/NomicFoundation/hardhat-boilerplate.git
cd hardhat-boilerplate
npm install
npx hardhat node
```

move the following files :

`register-contract/contracts/deploy.js` to `hardhat-boilerplate/scripts` replace the file

`register-contract/contracts/register.sol` to `hardhat-boilerplate/contracts` 

```python
npx hardhat run scripts/deploy.js --network localhost
```

record the `contract address` & `deploy wallet address`

## Backend

```python
cd ..
```

now the path should be /register-contract

revise the content in `register-contact/API/.env copy` and change name to `.env`

the var in the env :

- MONGO_CLIENT : MongoDB url (you need to have a MongoDB setup)
- WEB3_URL : chain url  (deafult should be http://localhost:8545/ if you run the hardhat node)
- REGISTRY_CONTRACT_ADDRESS : contract address below
- ADMIN_ADDRESS : deploy wallet address below

```python
pip install -r requirements.txt
cd API
uvicorn main:app --reload
```

## Frontend

```python
cd ..
cd vue-dapp-main
cd vue-dapp
npm install
npm run dev
```
