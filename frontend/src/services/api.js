import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust to your backend URL
  timeout: 10000,
});

export const fetchRegulationsAPI = async (search = '') => {
  const response = await apiClient.get('/regulations/', {
    params: { search },
  });
  return response.data;
};

export const fetchRegulationByIdAPI = async (id) => {
  const response = await apiClient.get(`/regulations/${id}/`);
  return response.data;
};
