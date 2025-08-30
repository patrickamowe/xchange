// wishlist.js
import { addCurrencyPair, removeCurrencyPair } from "./api.js";

export function setupWishlistHandlers() {
    // Add wishlist button
    const addBtn = document.getElementById("add-wishlist");
    if (addBtn) {
        addBtn.addEventListener("click", async () => {
            const base = document.getElementById("fromCurrency").value;
            const quote = document.getElementById("toCurrency").value;

            try {
                const data = await addCurrencyPair(base, quote);
            } catch (error) {
                console.error("Error adding currency pair:", error);
            }
        });
    }

    // Remove wishlist buttons
    const removeBtns = document.querySelectorAll(".remove-wishlist");
    removeBtns.forEach((btn) => {
        btn.addEventListener("click", async () => {
            const base = btn.getAttribute("data-value-base");
            const quote = btn.getAttribute("data-value-quote");

            try {
                const data = await removeCurrencyPair(base, quote);
                location.reload();
            } catch (error) {
                console.error("Error removing currency pair:", error);
            }
        });
    });
}
