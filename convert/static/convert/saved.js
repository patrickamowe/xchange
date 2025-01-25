document.addEventListener('DOMContentLoaded', () => {

    const elements = document.querySelectorAll('.remove-wishlist');
    elements.forEach((element) => {
        element.addEventListener('click', async () => {
            const baseCurrency = element.getAttribute('data-value-base');
            const quoteCurrency = element.getAttribute('data-value-quote');
            const url = `http://127.0.0.1:8000/remove_currency/${baseCurrency}/${quoteCurrency}/`
            try{
                const response = await fetch(url);
                const data = await response.json();
                console.log(data);
                location.reload();
            } catch (error) {
                console.error("Error removing currency pair:", error)
            }
        });
    });
});