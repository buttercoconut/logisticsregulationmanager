# app/frontend/src/components/RegulationList.vue
<template>
  <div>
    <h2>Regulation List</h2>
    <ul>
      <li v-for="reg in regulations" :key="reg.regulation_id">
        {{ reg.regulation_name }} - {{ reg.law_id }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const regulations = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://localhost:8000/regulations/')
    regulations.value = res.data
  } catch (e) {
    console.error(e)
  }
})
</script>
