import axios from 'axios';

const API_BASE = '/api';

export const getRegulations = () => axios.get(`${API_BASE}/regulations`);
export const getRegulationById = (id) => axios.get(`${API_BASE}/regulations/${id}`);
export const createRegulation = (data) => axios.post(`${API_BASE}/regulations`, data);
export const updateRegulation = (id, data) => axios.put(`${API_BASE}/regulations/${id}`, data);
export const deleteRegulation = (id) => axios.delete(`${API_BASE}/regulations/${id}`);
