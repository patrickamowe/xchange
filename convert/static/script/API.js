import {BACKEND_URL, API_KEY, FX_API_BASE} from './constant.js';

// Add conversion to saved conversions
export async function addConversion(base, quote) {
    const url = `${BACKEND_URL}/add_conversion/${base}/${quote}/`;
    const response = await fetch(url);
    return response.json();
}

// Remove conversion from saved conversions
export async function removeConversion(base, quote) {
    const url = `${BACKEND_URL}/remove_conversion/${base}/${quote}/`;
    const response = await fetch(url);
    return response.json();
}

// Convert currency
export async function convertCurrency(amount, from, to) {
    const url = `${FX_API_BASE}/${API_KEY}/pair/${from}/${to}/${amount}`;
    const response = await fetch(url);
    return response.json();
}


// Add conversion to recent conversions
export async function addRecentConversion(base, quote) {
    const url = `${BACKEND_URL}/add_recent_conversion/${base}/${quote}/`;
    const response = await fetch(url);
    return response.json();
}

// Clear all recent conversions
export async function clearRecentConversions() {
    const url = `${BACKEND_URL}/clear_recent_conversions/`;
    const response = await fetch(url);
    return response.json();
}   

// Fetch the API key from the backend
export async function getApiKey() {
    const url = `${BACKEND_URL}/get_api_key/`;
    const response = await fetch(url);
    return response.json();
}