<template>
  <v-container class="text-center" style="margin-top: 15%;">
    <div>
      <h1 class="text-grey-darken-2">WHO R U????</h1>
    </div>
    <div class="mt-5">
      <v-row justify="center">
        <v-col cols="4">
          <router-link style="text-decoration: none; color: inherit;" to="/admin">
            <v-btn block>
              admin
            </v-btn>
          </router-link>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="4">
          <router-link to="/voter" style="text-decoration: none; color: inherit;">
            <v-btn block>
              <text>voter</text>
            </v-btn>
          </router-link>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>