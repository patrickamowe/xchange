document.addEventListener('DOMContentLoaded', function() {
    const convert = document.getElementById('convert');
    const chart = document.getElementById('chart');
    let convertView = document.getElementById('convert-view');
    let chartView = document.getElementById('chart-view');
    let convertText = document.getElementById('convert-text');
    let chartText = document.getElementById('chart-text');

    convert.addEventListener('click', function() {
        convertView.classList.remove('hidden');
        chartView.classList.add('hidden');
        convertText.classList.remove('hidden');
        chartText.classList.add('hidden');
    });

    chart.addEventListener('click', function() {
        chartView.classList.remove('hidden');
        convertView.classList.add('hidden');
        convertText.classList.add('hidden');
        chartText.classList.remove('hidden');
    });

    async function convertCurrency() {
        // Show loading indicator
        document.getElementById("result").textContent = "Loading...";

        // Get user input values
        const amount = document.getElementById('amount').value;
        const fromCurrency = document.getElementById('fromCurrency').value.toUpperCase();
        const toCurrency = document.getElementById('toCurrency').value.toUpperCase();

        // Check if input values are valid
        if (!amount || !fromCurrency || !toCurrency) {
            alert("Please fill in all fields.");
            return;
        }

        const apiKey = '7fe0597fce4c9eadaa610d6b';
        const url = `https://v6.exchangerate-api.com/v6/${apiKey}/pair/${fromCurrency}/${toCurrency}/${amount}`;

        try {
            // Fetch the conversion rate
            const response = await fetch(url);
            const data = await response.json();

            if (data.result === "success") {
                const conversionRate = data.conversion_rate;
                const convertedAmount = data.conversion_result;
                document.getElementById("result").textContent =
                    `${amount} ${fromCurrency} = ${convertedAmount.toFixed(2)} ${toCurrency} (Rate: ${conversionRate})`;
            } else {
                document.getElementById("result").textContent = "Conversion failed. Please check your input.";
            }
        } catch (error) {
            console.error("Error fetching conversion rate:", error);
            document.getElementById("result").textContent = "An error occurred. Please try again.";
        }
    }

    document.getElementById('convert-button').addEventListener('click', convertCurrency);

});