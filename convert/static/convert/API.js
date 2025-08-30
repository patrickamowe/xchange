// api.js
const BACKEND_URL = "http://127.0.0.1:8000";
const API_KEY = "7fe0597fce4c9eadaa610d6b";
const FX_API_BASE = "https://v6.exchangerate-api.com/v6";

// Add currency pair to wishlist
export async function addCurrencyPair(base, quote) {
    const url = `${BACKEND_URL}/add_currency/${base}/${quote}/`;
    const response = await fetch(url);
    return response.json();
}

// Remove currency pair from wishlist
export async function removeCurrencyPair(base, quote) {
    const url = `${BACKEND_URL}/remove_currency/${base}/${quote}/`;
    const response = await fetch(url);
    return response.json();
}

// Convert currency
export async function convertCurrency(amount, from, to) {
    const url = `${FX_API_BASE}/${API_KEY}/pair/${from}/${to}/${amount}`;
    const response = await fetch(url);
    return response.json();
}
