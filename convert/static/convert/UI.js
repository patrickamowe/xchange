// ui.js
import { convertCurrency } from "./api.js";

export function setupUIHandlers() {
    // Default values
    document.getElementById("fromCurrency").value = "USD";
    document.getElementById("toCurrency").value = "NGN";
    document.getElementById("from-Currency").value = "USD";
    document.getElementById("to-Currency").value = "NGN";

    const convert = document.getElementById("convert");
    const chart = document.getElementById("chart");
    const convertView = document.getElementById("convert-view");
    const chartView = document.getElementById("chart-view");
    const convertText = document.getElementById("convert-text");
    const chartText = document.getElementById("chart-text");

    // Toggle between convert/chart view
    convert.addEventListener("click", () => {
        convertView.classList.remove("hidden");
        chartView.classList.add("hidden");
        convertText.classList.remove("hidden");
        chartText.classList.add("hidden");
    });

    chart.addEventListener("click", () => {
        chartView.classList.remove("hidden");
        convertView.classList.add("hidden");
        convertText.classList.add("hidden");
        chartText.classList.remove("hidden");
    });

    // Swap button (convert)
    document.getElementById("convert-swap-btn").addEventListener("click", () => {
        let from = document.getElementById("fromCurrency");
        let to = document.getElementById("toCurrency");
        [from.value, to.value] = [to.value, from.value];
    });

    // Swap button (chart)
    document.getElementById("chart-swap-btn").addEventListener("click", () => {
        let from = document.getElementById("from-Currency");
        let to = document.getElementById("to-Currency");
        [from.value, to.value] = [to.value, from.value];
    });

    // Currency conversion
    document.getElementById("convert-button").addEventListener("click", async () => {
        const amount = document.getElementById("amount").value;
        const from = document.getElementById("fromCurrency").value;
        const to = document.getElementById("toCurrency").value;

        if (!amount || !from || !to) {
            alert("Please fill in all fields.");
            return;
        }

        document.getElementById("result").textContent = "Loading...";

        try {
            const data = await convertCurrency(amount, from, to);
            if (data.result === "success") {
                document.getElementById("result").textContent =
                    `${amount} ${from} = ${data.conversion_result.toFixed(2)} ${to} (Rate: ${data.conversion_rate})`;
            } else {
                document.getElementById("result").textContent = "Conversion failed.";
            }
        } catch (error) {
            console.error("Error fetching conversion:", error);
            document.getElementById("result").textContent = "An error occurred.";
        }
    });

    // Chart button (temporary)
    document.getElementById("chart-button").addEventListener("click", () => {
        document.getElementById("chart-result").textContent = "This feature is Coming Soon...";
    });
}
