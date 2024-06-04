<template>
  <v-container class="text-center" style="margin-top: 18%;">
    <div class="mt-5">
      <v-row justify="center">
        <v-col cols="4">
          <router-link style="text-decoration: none; color: inherit;" to="/electionlist">
            <v-btn block>
              election list
            </v-btn>
          </router-link>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="4">
          <router-link to="/register" style="text-decoration: none; color: inherit;">
            <v-btn block>
              <text>register</text>
            </v-btn>
          </router-link>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="4">
          <router-link to="/" style="text-decoration: none; color: inherit;">
            <v-btn block>
              <text>back</text>
            </v-btn>
          </router-link>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>