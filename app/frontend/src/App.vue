# app/frontend/src/App.vue
<template>
  <div id="app">
    <h1>Logistics Regulation Manager</h1>
    <router-view></router-view>
  </div>
</template>

<script setup>
import { createRouter, createWebHistory } from 'vue-router'
import RegulationList from './components/RegulationList.vue'

const routes = [
  { path: '/', component: RegulationList },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
}
</style>
