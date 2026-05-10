<template>
  <div>
    <h2>{{ regulation.regulation_name }}</h2>
    <p>{{ regulation.description }}</p>
    <p>Effective: {{ regulation.effective_date }}</p>
    <p>Expiry: {{ regulation.expiry_date }}</p>
    <p v-if="regulation.document_url">
      <a :href="regulation.document_url" target="_blank">Download Document</a>
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const regulation = ref({});

onMounted(async () => {
  const res = await axios.get(`/api/regulations/${route.params.id}`);
  regulation.value = res.data;
});
</script>
