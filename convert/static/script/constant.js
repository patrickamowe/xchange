import { getApiKey } from './api.js';

const BACKEND_URL = "http://127.0.0.1:8000";
const API_KEY = await getApiKey().then(data => data.api_key);
const FX_API_BASE = "https://v6.exchangerate-api.com/v6";