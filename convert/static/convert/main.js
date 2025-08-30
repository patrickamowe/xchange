// main.js
import { setupUIHandlers } from "./UI.js";
import { setupWishlistHandlers } from "./wishlist.js";

document.addEventListener("DOMContentLoaded", () => {
    setupWishlistHandlers();
    setupUIHandlers();
});
