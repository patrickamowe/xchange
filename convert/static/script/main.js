// main.js
import { setupUIHandlers } from "./UI.js";
import { setupWishlistHandlers } from "./wishlist.js";
import { setupPopularConversionHandlers } from "./popular-conversion.js";

document.addEventListener("DOMContentLoaded", () => {
    
    setupWishlistHandlers();
    setupPopularConversionHandlers();
    setupUIHandlers();
});
