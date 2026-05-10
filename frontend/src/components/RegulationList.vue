<template>
  <div>
    <h2>Regulation List</h2>
    <ul>
      <li v-for="reg in regulations" :key="reg.regulation_id">
        <router-link :to="{ name: 'RegulationDetail', params: { id: reg.regulation_id } }">
          {{ reg.regulation_name }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const regulations = ref([]);

onMounted(async () => {
  const res = await axios.get('/api/regulations');
  regulations.value = res.data;
});
</script>

<style scoped>
ul { list-style: none; padding: 0; }
li { margin: 0.5rem 0; }
</style>
