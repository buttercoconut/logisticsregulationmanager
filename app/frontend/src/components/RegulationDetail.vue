# app/frontend/src/components/RegulationDetail.vue
<template>
  <div>
    <h2>Regulation Detail</h2>
    <p>Name: {{ regulation.regulation_name }}</p>
    <p>Law ID: {{ regulation.law_id }}</p>
    <p>Description: {{ regulation.description }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const regulation = ref({})

onMounted(async () => {
  try {
    const res = await axios.get(`http://localhost:8000/regulations/${route.params.id}`)
    regulation.value = res.data
  } catch (e) {
    console.error(e)
  }
})
</script>
