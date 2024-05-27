const Web3 = require('web3');

// 鍊地址
const web3 = new Web3('');

// 合约的ABI和地址
const voterRegistryABI = [];
const voterRegistryAddress = '';

const voterRegistryContract = new web3.eth.Contract(voterRegistryABI, voterRegistryAddress);

// voter info example
let data = {
    name: 'John',
    age: 30,
    id: 'A123456789'
  };

// register voter
function registerVoter(voterInfo, adminAddress, voterAddress) {

    // 向 server 核對 voter 資格
    fetch('https://localhost:8080/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        // body, data 替換成 voterInfo
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        if (data === 'true'){
            try {
                voterRegistryContract.methods.registerVoter(voterAddress).send({ from: adminAddress });
                console.log(`Voter ${voterAddress} has been registered.`);
            } catch (error) {
                console.error('Error registering voter:', error);
            }
        } else {
            console.error('資格不符合')
        }
    })
    .catch(error => console.error('錯誤:', error));
}

// check if voter is eligible
function isEligible(voterAddress) {
    try {
        const eligible = voterRegistryContract.methods.isEligible(voterAddress).call();
        if (eligible){
            console.log(`Voter ${voterAddress} is eligible.`)
        } else {
            console.log(`Voter ${voterAddress} is not eligible.`)
        }
        return eligible;
    } catch (error) {
        console.error('錯誤:', error);
    }
}