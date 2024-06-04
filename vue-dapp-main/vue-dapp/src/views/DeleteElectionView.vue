<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
const router = useRouter();
const url = 'http://hc5.isl.lab.nycu.edu.tw:8000/election';
const electionList = ref([])
onMounted(() => {
  axios.get(url)
    .then((res) => {
      electionList.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

function deleteElection(contract_id) {
  if (confirm("Are you sure to delete this election?")) {
    axios.delete(url + "/" + contract_id)
      .then((res) => {
        alert("Delete success")
        axios.get(url)
          .then((res) => {
            electionList.value = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>

<template>
  <v-container>
    <v-row justify="center" style="margin-top: 10%">
      <h1>Election List</h1>
    </v-row>
    <v-row justify="center" style="margin-top: 5%">
      <v-col cols="3" class="d-flex justify-center" v-for="(item) in electionList">
        <v-card :title="item.name">
          <v-card-text>
            {{ item.description }}
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn variant="flat" rounded="xl" color="red" @click="deleteElection(item.contract_id)">delete</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-10">
      <v-col cols="2">
        <v-btn block class="text-subtitle-1" @click="() => { router.push('/admin') }">
          <p>Back</p>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
