document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('fromCurrency').value = 'USD';
    document.getElementById('toCurrency').value = 'NGN';
    document.getElementById('from-Currency').value = 'USD';
    document.getElementById('to-Currency').value = 'NGN';

    const convert = document.getElementById('convert');
    const chart = document.getElementById('chart');
    let convertView = document.getElementById('convert-view');
    let chartView = document.getElementById('chart-view');
    let convertText = document.getElementById('convert-text');
    let chartText = document.getElementById('chart-text');

    convert.addEventListener('click', () => {
        convertView.classList.remove('hidden');
        chartView.classList.add('hidden');
        convertText.classList.remove('hidden');
        chartText.classList.add('hidden');
    });

    chart.addEventListener('click', () => {
        chartView.classList.remove('hidden');
        convertView.classList.add('hidden');
        convertText.classList.add('hidden');
        chartText.classList.remove('hidden');
    });

    document.getElementById('convert-swap-btn').addEventListener('click', () => {
        // Get the select elements
        let fromCurrency = document.getElementById('fromCurrency');
        let toCurrency = document.getElementById('toCurrency');

        // Swap the values
        let tempValue = fromCurrency.value;
        fromCurrency.value = toCurrency.value;
        toCurrency.value = tempValue;
    });

    document.getElementById('chart-swap-btn').addEventListener('click', () => {
        // Get the select elements
        let fromCurrency = document.getElementById('from-Currency');
        let toCurrency = document.getElementById('to-Currency');

        // Swap the values
        let tempValue = fromCurrency.value;
        fromCurrency.value = toCurrency.value;
        toCurrency.value = tempValue;
    });

    async function convertCurrency() {
        // Show loading indicator
        document.getElementById("result").textContent = "Loading...";

        // Get user input values
        const amount = document.getElementById('amount').value;
        const fromCurrency = document.getElementById('fromCurrency').value;
        const toCurrency = document.getElementById('toCurrency').value;

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

     document.getElementById('add-wishlist').addEventListener('click', async () => {
        const baseCurrency = document.getElementById('fromCurrency').value;
        const quoteCurrency = document.getElementById('toCurrency').value;
        const url = `http://127.0.0.1:8000/add_currency/${baseCurrency}/${quoteCurrency}/`
        try{
            const response = await fetch(url);
            const data = await response.json();
            console.log(data)
        } catch (error){
            console.error("Error adding currency pair:", error);
        }
    });


});