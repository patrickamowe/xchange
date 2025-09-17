// Save recent conversions to local storage
export function saveConversion(base, quote) {
    let recentConversions = JSON.parse(localStorage.getItem('recentConversions')) || [];
    
    const newConversion = { "base":base, "quote":quote , "timestamp": Date.now() };

    // Add the new conversion to the start of the array
    recentConversions.unshift(newConversion);

    // keep only the 5 most recent conversions
    recentConversions = recentConversions.slice(0, 5);

    localStorage.setItem('recentConversions', JSON.stringify(recentConversions));

}

// Retrieve recent conversions
export function getConversions() {
    return JSON.parse(localStorage.getItem('recentConversions')) || [];
}

// Clear recent conversions
export function clearConversions() {
    localStorage.removeItem('recentConversions');
}
