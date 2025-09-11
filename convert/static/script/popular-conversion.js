// Clickable currency rates
import { convertCurrency } from "./api.js";

export function setupPopularConversionHandlers() {
    const convertView = document.getElementById("convert-view");
    const chartView = document.getElementById("chart-view");
    const convertText = document.getElementById("convert-text");
    const chartText = document.getElementById("chart-text");
    const rateRows = document.querySelectorAll(".rate-row");
    const fromCurrencyInput = document.getElementById("fromCurrency");
    const toCurrencyInput = document.getElementById("toCurrency");

    rateRows.forEach((row) => {
        row.addEventListener("click", async () => {

            // Extract base and target currencies from data attributes
            const base = row.getAttribute("data-base");
            const target = row.getAttribute("data-target");

            // Set the currency inputs and switch to convert view
            fromCurrencyInput.value = base;
            toCurrencyInput.value = target;
            convertView.classList.remove("hidden");
            chartView.classList.add("hidden");
            convertText.classList.remove("hidden");
            chartText.classList.add("hidden");

            //scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
            
            // Perform a quick conversion and display result
            document.getElementById("result").textContent = "Loading...";
            try {   
                const amount = 1; // Default amount for quick conversion
                const data = await convertCurrency(amount, base, target);
                if (data.result === "success") {
                    document.getElementById("result").textContent = `${amount} ${base} = ${data.conversion_result.toFixed(2)} ${target}`;
                } else {
                    document.getElementById("result").textContent = "Conversion failed.";
                }
            } catch (error) {
                console.error("Error during conversion:", error);
                document.getElementById("result").textContent = "Error during conversion.";
            }
        });
    });
}
