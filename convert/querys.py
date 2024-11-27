import requests

def fetch_top_headlines(api_key, country):
    """
    Fetches the top headlines for a specified country using News API.

    Parameters:
        api_key (str): Your News API key.
        country (str): The country code (e.g., 'us' for the United States).

    Returns:
        dict: A dictionary with the status, total results, and list of articles.
    """
    # Define the base URL and parameters
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": api_key
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful

        # Parse the JSON response
        data = response.json()

        # Check if the response contains articles
        if "articles" in data:
            return {
                "status": data.get("status", "error"),
                "totalResults": data.get("totalResults", 0),
                "articles": data["articles"]
            }
        else:
            return {"status": "error", "message": "No articles found"}

    except requests.exceptions.RequestException as e:
        # Handle any HTTP errors or other issues
        print(f"An error occurred: {e}")
        return {"status": "error", "message": str(e)}


def fetch_everything(api_key, query):
    """
        Fetches news according to a specify query using News API.

        Parameters:
            api_key (str): Your News API key.
            query (str): Keywords or phrases to search for in the article title and body.

        Returns:
            respond: A dictionary with the status, total results, and list of articles.
    """
    # Define the base URL and parameters
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": api_key
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful

        # Parse the JSON response
        data = response.json()

        # Check if the response contains articles
        if "articles" in data:
            return {
                "status": data.get("status", "error"),
                "totalResults": data.get("totalResults", 0),
                "articles": data["articles"]
            }
        else:
            return {"status": "error", "message": "No articles found"}

    except requests.exceptions.RequestException as e:
        # Handle any HTTP errors or other issues
        print(f"An error occurred: {e}")
        return {"status": "error", "message": str(e)}


def live_rates(api_key, base_code, target_code):
    """
    Fetches the ExchangeRate API to get the conversion rate.

    Parameters:
        api_key (str): Your ExchangeRate API key.
        base_code (str): A three-letter code representing the base currency.
        target_code (str): A three-letter code representing the target currency.

    Returns:
        dict: A dictionary with the status, conversion rate, and error message if any.
    """
    # Define the base URL and endpoint
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_code}/{target_code}"

    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful

        # Parse the JSON response
        data = response.json()

        # Check if the response contains the conversion rate
        if data.get("conversion_rate"):
            return {
                "status": "success",
                "base_code": base_code,
                "target_code": target_code,
                "conversion_rate": data["conversion_rate"]
            }
        else:
            return {"status": "error", "message": "No conversion_rate found in the response"}

    except requests.exceptions.RequestException as e:
        # Handle any HTTP errors or other issues
        print(f"An error occurred: {e}")
        return {"status": "error", "message": str(e)}


def get_live_rate():
    api_key = '7fe0597fce4c9eadaa610d6b'
    pairs = [{"base_code": "USD", "target_code": "NGN"},
             {"base_code": "EUR", "target_code": "NGN"},
             {"base_code": "GBP", "target_code": "NGN"},
             {"base_code": "GHS", "target_code": "NGN"}]

    currency_rates = []

    for pair in pairs:
        result = live_rates(api_key, pair["base_code"], pair["target_code"])
        if result["status"] == "success":
            currency_rates.append({
                "base_code": result["base_code"],
                "target_code": result["target_code"],
                "conversion_rate": result["conversion_rate"]
            })
        else:
            # Handle errors, for example, appending the error message
            currency_rates.append({
                "base_code": pair["base_code"],
                "target_code": pair["target_code"],
                "error": result["message"]
            })

    return currency_rates
