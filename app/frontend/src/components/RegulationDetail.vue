<template>
  <div>
    <h2>Regulation Detail</h2>
    <div v-if="regulation">
      <p><strong>Name:</strong> {{ regulation.regulation_name }}</p>
      <p><strong>Law:</strong> {{ regulation.law_name }}</p>
      <p><strong>Description:</strong> {{ regulation.description }}</p>
      <p><strong>Effective:</strong> {{ regulation.effective_date }}</p>
      <p><strong>Expiry:</strong> {{ regulation.expiry_date }}</p>
      <p><strong>Document:</strong>
        <a :href="regulation.document_url" target="_blank">Download</a>
      </p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const regulation = ref(null);

const fetchRegulation = async () => {
  try {
    const res = await axios.get(`/api/regulations/${route.params.id}`);
    regulation.value = res.data;
  } catch (e) {
    console.error('Failed to fetch regulation', e);
  }
};

onMounted(fetchRegulation);
</script>

<style scoped>
p {
  margin: 4px 0;
}
</style>
