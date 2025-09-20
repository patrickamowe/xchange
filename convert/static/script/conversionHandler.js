import { addConversion, removeConversion } from "./API.js";

export function conversionHandler() {
    // Add conversion button
    const addBtn = document.getElementById("add-conversion");
    if (addBtn) {
        addBtn.addEventListener("click", async () => {
            const base = document.getElementById("fromCurrency").value;
            const quote = document.getElementById("toCurrency").value;

            try {
                const data = await addConversion(base, quote);
                window.alert("Currency pair added to saved conversions!");
            } catch (error) {
                console.error("Error adding currency pair:", error);
            }
        });
    }

    // Remove wishlist buttons
    const removeBtns = document.querySelectorAll(".delete-icon");
    removeBtns.forEach((btn) => {
        btn.addEventListener("click", async () => {
            const base = btn.getAttribute("data-value-base");
            const quote = btn.getAttribute("data-value-quote");

            try {
                const data = await removeConversion(base, quote);
                location.reload();
            } catch (error) {
                console.error("Error removing currency pair:", error);
            }
        });
    });
}
