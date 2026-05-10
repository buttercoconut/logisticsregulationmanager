import { createRouter, createWebHistory } from 'vue-router';
import RegulationList from './components/RegulationList.vue';
import RegulationDetail from './components/RegulationDetail.vue';

const routes = [
  { path: '/', name: 'RegulationList', component: RegulationList },
  { path: '/regulation/:id', name: 'RegulationDetail', component: RegulationDetail, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
