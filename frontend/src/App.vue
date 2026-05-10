<template>
  <router-view />
</template>

<script setup>
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

axios.defaults.baseURL = '/';

createApp(App).use(router).mount('#app');
</script>
