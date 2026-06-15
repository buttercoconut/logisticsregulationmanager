<template>
  <div class="regulation-list">
    <h2>Regulation List</h2>
    <input v-model="search" @input="fetchRegulations" placeholder="Search regulations..." />
    <ul>
      <li v-for="reg in regulations" :key="reg.regulation_id" @click="selectRegulation(reg)" class="reg-item">
        {{ reg.regulation_name }} ({{ reg.effective_date }} - {{ reg.expiry_date }})
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { fetchRegulationsAPI } from '@/services/api';

const regulations = ref([]);
const search = ref('');
const selectedRegulation = ref(null);

const fetchRegulations = async () => {
  const data = await fetchRegulationsAPI(search.value);
  regulations.value = data;
};

const selectRegulation = (reg) => {
  selectedRegulation.value = reg;
  // Emit event to parent or navigate to detail view
  // For simplicity, we just log here
  console.log('Selected regulation:', reg);
};

onMounted(() => {
  fetchRegulations();
});
</script>

<style scoped>
.regulation-list {
  padding: 1rem;
}
.reg-item {
  cursor: pointer;
  padding: 0.5rem 0;
}
.reg-item:hover {
  background-color: #f0f0f0;
}
</style>
