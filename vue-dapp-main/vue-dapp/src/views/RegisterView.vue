<template>
  <v-container>
    <v-row justify="center" style="margin-top: 17%;">
      <h1>Register</h1>
    </v-row>
    <v-row justify="center" class="text-center d-flex align-center mt-10">
      <v-col cols="2">
        <p class="text-h6">name:</p>
      </v-col>
      <v-col cols="5">
        <v-text-field hide-details="auto" v-model="name" placeholder="name" />
      </v-col>
      <v-col cols=1></v-col>
    </v-row>
    <v-row justify="center" class="text-center d-flex align-center mt-10">
      <v-col cols="2">
        <p class="text-h6">id:</p>
      </v-col>
      <v-col cols="5">
        <v-text-field hide-details="auto" v-model="id" placeholder="start" />
      </v-col>
      <v-col cols=1></v-col>
    </v-row>
    <v-row justify="center" class="text-center d-flex align-center mt-10">
      <v-col cols="2">
        <p class="text-h6">age:</p>
      </v-col>
      <v-col cols="5">
        <v-text-field hide-details="auto" v-model="age" placeholder="end" />
      </v-col>
      <v-col cols=1></v-col>
    </v-row>
    <v-row justify="center" class="text-center d-flex align-center mt-10">
      <v-col cols="3">
        <v-btn block @click="submitInfo()">submit</v-btn>
      </v-col>
    </v-row>
    <v-row justify="center" class="text-center d-flex align-center">
      <v-col cols="3">
        <v-btn block class="text-subtitle-1" @click="() => { router.push('/voter') }">
          <p>Back</p>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ethers } from 'ethers'
import { ref } from 'vue'
import axios from 'axios'

const router = useRouter()
const name = ref('')
const id = ref('')
const age = ref('')
const url = 'http://hc5.isl.lab.nycu.edu.tw:8000/register';

let provider
let signer

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
    // let network = await provider.getNetwork()
    // let signerAddress = await signer.getAddress()
    await provider.send('eth_requestAccounts', [])

  }
}

async function submitInfo() {
  await connectWallet()
  axios.post(url, {
    name: name.value,
    id: id.value,
    age: age.value,
    address: await signer.getAddress()
  }).then((res) => {
    if(res.data){
      alert('register success')
    }else{
      alert('register fail')
    }
  }).catch((err) => {
    console.log(err)
  })
}
</script>