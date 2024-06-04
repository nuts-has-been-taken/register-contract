<template>
  <v-container>
    <v-row justify="center" class="mt-10">
      <h1>{{ electionName }}</h1>
    </v-row>
    <v-row justify="center" class="mt-10">
      <v-col cols="2" class="d-flex justify-end">
        <p class="text-h6">voter address:</p>
      </v-col>
      <v-col cols="5">
        <p class="text-h6">{{ signerAddress }}</p>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-0">
      <v-col cols="2" class="d-flex justify-end">
        <p class="text-h6">contract address:</p>
      </v-col>
      <v-col cols="5">
        <p class="text-h6">{{ contractAddress }}</p>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-10">
      <v-col cols="8">
        <v-timeline direction="horizontal">
          <v-timeline-item :dot-color="dotColor[0]" size="small">
            <p>
              vote create
            </p>
            <template v-slot:opposite>
              <p>
                {{ voteData[0] }}
              </p>
              <p class="text-center">
                {{ voteTime[0] }}
              </p>
            </template>
          </v-timeline-item>
          <v-timeline-item :dot-color="dotColor[1]" size="small">
            <template v-slot:opposite>
              vote start
            </template>
            <p>
              {{ voteData[1] }}
            </p>
            <p class="text-center">
              {{ voteTime[1] }}
            </p>
          </v-timeline-item>
          <v-timeline-item :dot-color="dotColor[2]" size="small">
            <p>
              vote end
            </p>
            <template v-slot:opposite>
              <p>
                {{ voteData[2] }}
              </p>
              <p class="text-center">
                {{ voteTime[2] }}
              </p>
            </template>
          </v-timeline-item>
          <v-timeline-item :dot-color="dotColor[3]" size="small">
            <template v-slot:opposite>
              count vote
            </template>
            <p>
              {{ voteData[3] }}
            </p>
            <p class="text-center">
              {{ voteTime[3] }}
            </p>
          </v-timeline-item>
        </v-timeline>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-10">
      <v-col cols="8">
        <v-table>
          <tbody>
            <tr v-for="(item, index) in candidates" :key="item.name">
              <td class="text-center text-h6">{{ item.name }}</td>
              <td class="text-center text-h6">{{ item.voteCount }}</td>
              <td class="text-center text-h6"> <v-btn @click="vote(index)" :disabled="!voteStatus">vote</v-btn></td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-10">
      <v-col cols="3" class="d-flex justify-end">
        <p class="text-h6">remain time:</p>
      </v-col>
      <v-col cols="3">
        <p class="text-h6">{{ remainTime }}</p>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-10">
      <v-col cols="2">
        <v-btn block class="text-subtitle-1" @click="() => { router.push('/electionlist') }">
          <p>Back</p>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
  <!-- <div>your account: {{ signerAddress }}</div>
  <v-btn @click="test()">test</v-btn>
  <v-text-field v-model="privateKey" placeholder="edit me" /> -->
</template>

<script setup>
import { ethers } from 'ethers'
import { useRoute, useRouter } from 'vue-router';
import { ref } from 'vue'
const route = useRoute();
const router = useRouter();

let signer
let provider

const candidates = ref([])
const dotColor = ref(['white', 'white', 'white', 'white'])
const voteData = ref([])
const voteTime = ref([])
const voteStatus = ref(false)
const remainTime = ref('-----------')
const electionName = ref('')
const signerAddress = ref('')

let contractAddress = route.params.id
let contractAbi = [
  {
    "inputs": [
      {
        "internalType": "string[]",
        "name": "_candidateNames",
        "type": "string[]"
      },
      {
        "internalType": "uint256",
        "name": "_startTime",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_endTime",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_votingCount",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "_voteName",
        "type": "string"
      },
      {
        "internalType": "address",
        "name": "_userRegistryAddress",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "voter",
        "type": "address"
      }
    ],
    "name": "VoteCast",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "candidates",
    "outputs": [
      {
        "internalType": "string",
        "name": "name",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "voteCount",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getAllVotesOfCandiates",
    "outputs": [
      {
        "components": [
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "voteCount",
            "type": "uint256"
          }
        ],
        "internalType": "struct Voting.Candidate[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getBlockTimestamp",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getRemainingTime",
    "outputs": [
      {
        "internalType": "uint256[4]",
        "name": "",
        "type": "uint256[4]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getVoteName",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getVotingStatus",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "newFunc",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_candidateIndex",
        "type": "uint256"
      }
    ],
    "name": "vote",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "voters",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "votingCount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "votingCreate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "votingEnd",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "votingName",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "votingStart",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]
let contractInstance


await connectWallet()
await setDateTime()
await contractInit()

window.ethereum.on('accountsChanged', async () => {
  provider = new ethers.BrowserProvider(window.ethereum)
  await provider.send('eth_requestAccounts', [])
  signer = await provider.getSigner()
  signerAddress.value = await signer.getAddress()
});



// async function test() {
//   let provider2 = HTTPProvider("http://127.0.0.1:8545/")
//   let signer2 = new ethers.Wallet(privateKey, provider2);
//   contractInstance = new ethers.Contract(contractAddress, contractAbi, signer2)
// }

// count two unix timestamp difference
function timeDiff(curr, prev) {
  var ms_Min = 60 * 1000; // milliseconds in Minute 
  var ms_Hour = ms_Min * 60; // milliseconds in Hour 
  var ms_Day = ms_Hour * 24; // milliseconds in day 
  var ms_Mon = ms_Day * 30; // milliseconds in Month 
  var ms_Yr = ms_Day * 365; // milliseconds in Year 
  var diff = curr - prev; //difference between dates. 
  // If the diff is less then milliseconds in a minute 
  if (diff < ms_Min) {
    return Math.round(diff / 1000) + ' seconds';

    // If the diff is less then milliseconds in a Hour 
  } else if (diff < ms_Hour) {
    return Math.round(diff / ms_Min) + ' minutes';

    // If the diff is less then milliseconds in a day 
  } else if (diff < ms_Day) {
    return Math.round(diff / ms_Hour) + ' hours';

    // If the diff is less then milliseconds in a Month 
  } else if (diff < ms_Mon) {
    return 'Around ' + Math.round(diff / ms_Day) + ' days';

    // If the diff is less then milliseconds in a year 
  } else if (diff < ms_Yr) {
    return 'Around ' + Math.round(diff / ms_Mon) + ' months';
  } else {
    return 'Around ' + Math.round(diff / ms_Yr) + ' years';
  }
}

// convert unix timestamp to [year, month, day, hours, minutes, seconds]
function unixToDateTime(unix_timestamp) {
  let date = new Date(unix_timestamp * 1000);
  let year = date.getFullYear();
  let month = String(date.getMonth() + 1).padStart(2, '0');
  let day = String(date.getDate()).padStart(2, '0');
  let hours = String(date.getHours()).padStart(2, '0');
  let minutes = String(date.getMinutes()).padStart(2, '0');
  let seconds = String(date.getSeconds()).padStart(2, '0');
  return [year, month, day, hours, minutes, seconds];
}

// init datetime
async function setDateTime() {
  // set timestamp now
  const timestamp = Math.floor(Date.now() / 1000);
  let contractTime = await contractInstance.getRemainingTime()

  // from bigInt to number
  contractTime = contractTime.map(bigIntValue => Number(bigIntValue));

  // set dot color
  if (timestamp > contractTime[3]) {
    dotColor.value = ['white', 'white', 'white', 'grey-darken-1'];
  } else if (timestamp > contractTime[2]) {
    dotColor.value = ['white', 'white', 'grey-darken-1', 'white'];
  } else if (timestamp > contractTime[1]) {
    dotColor.value = ['white', 'grey-darken-1', 'white', 'white'];
  } else {
    dotColor.value = ['grey-darken-1', 'white', 'white', 'white'];
  }

  // check is voting available
  if (timestamp > contractTime[1] && timestamp < contractTime[2]) {
    voteStatus.value = true
    // set countdown timer
    setInterval(() => {
      remainTime.value = timeDiff(contractTime[2] * 1000, Date.now());
    }, 1000);
  }


  // set voteData and voteTime
  for (let time in contractTime) {
    voteData.value.push(`${unixToDateTime(contractTime[time])[0]}/${unixToDateTime(contractTime[time])[1]}/${unixToDateTime(contractTime[time])[2]}`);
    voteTime.value.push(`${unixToDateTime(contractTime[time])[3]}:${unixToDateTime(contractTime[time])[4]}:${unixToDateTime(contractTime[time])[5]}`);
  }
}

async function vote(num) {
  // provider = new ethers.BrowserProvider(window.ethereum);
  // await provider.send("eth_requestAccounts", []);
  signer = await provider.getSigner();
  contractInstance = new ethers.Contract(
    contractAddress, contractAbi, signer
  );
  try {
    await contractInstance.vote(num);
    alert('Voted successfully!')
    contractInit()
  } catch (error) {
    alert(error.message)
  }
}

async function connectWallet() {
  // This is the most common way to connect to MetaMask
  if (window.ethereum == null) {
    // If MetaMask is not installed, we use the default provider,
    // which is backed by a variety of third-party services (such
    // as INFURA). They do not have private keys installed,
    // so they only have read-only access
    console.log('MetaMask not installed; using read-only defaults')
    provider = ethers.getDefaultProvider()
  } else {
    // Connect to the MetaMask EIP-1193 object. This is a standard
    // protocol that allows Ethers access to make all read-only
    // requests through MetaMask.
    provider = new ethers.BrowserProvider(window.ethereum)

    // It also provides an opportunity to request access to write
    // operations, which will be performed by the private key
    // that MetaMask manages for the user.
    signer = await provider.getSigner()
    let network = await provider.getNetwork()
    signerAddress.value = await signer.getAddress()
    await provider.send('eth_requestAccounts', [])
    contractInstance = new ethers.Contract(contractAddress, contractAbi, signer)
  }
}

async function contractInit() {
  electionName.value = await contractInstance.getVoteName()
  let candidate = await contractInstance.getAllVotesOfCandiates()
  candidates.value = []
  for (let i = 0; i < candidate.length; i++) {
    candidates.value.push({
      name: candidate[i][0],
      voteCount: candidate[i][1]
    })
  }
}
</script>