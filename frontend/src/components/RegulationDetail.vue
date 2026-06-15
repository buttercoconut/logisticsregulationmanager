<template>
  <div class="regulation-detail" v-if="regulation">
    <h2>{{ regulation.regulation_name }}</h2>
    <p><strong>Law ID:</strong> {{ regulation.law_id }}</p>
    <p><strong>Description:</strong> {{ regulation.description }}</p>
    <p><strong>Effective Date:</strong> {{ regulation.effective_date }}</p>
    <p><strong>Expiry Date:</strong> {{ regulation.expiry_date }}</p>
    <p><strong>Document:</strong> <a :href="regulation.document_url" target="_blank">Download</a></p>
    <p><strong>Created At:</strong> {{ regulation.created_at }}</p>
    <p><strong>Updated At:</strong> {{ regulation.updated_at }}</p>
  </div>
  <div v-else>
    <p>Select a regulation to view details.</p>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { fetchRegulationByIdAPI } from '@/services/api';

const props = defineProps({
  regulationId: {
    type: Number,
    required: true,
  },
});

const regulation = ref(null);

const loadRegulation = async () => {
  if (!props.regulationId) return;
  regulation.value = await fetchRegulationByIdAPI(props.regulationId);
};

watch(() => props.regulationId, loadRegulation, { immediate: true });
</script>

<style scoped>
.regulation-detail {
  padding: 1rem;
}
</style>
