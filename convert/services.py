import requests

def fetchNewsHeadline(api_key, country):
    """
    Fetches news headline for a specified country using News API.

    Parameters:
        api_key (str): Your News API key.
        country (str): The country code (e.g., 'us' for United States).

    Returns:
        dict: A dictionary with the status, total results, and list of articles.
    """

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
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
        print(f"An error occurred: {e}")
        return {"status": "error", "message": str(e)}


def fetchNews(api_key, query):
    """
        Fetches news according to a specify query using News API.

        Parameters:
            api_key (str): Your News API key.
            query (str): Keywords or phrases to search for in the article title and body.

        Returns:
            respond: A dictionary with the status, total results, and list of articles.
    """
    # Define the base URL and parameters
    url = f"https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
        data = response.json()

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


def liveRate(api_key, base_code, target_code):
    """
    Uses ExchangeRate API to get live conversion rate.

    Parameters:
        api_key (str): Your ExchangeRate API key.
        base_code (str): A three-letter code representing the base currency.
        target_code (str): A three-letter code representing the target currency.

    Returns:
        dict: A dictionary with the status, conversion rate, and error message if any.
    """

    url = f"https://v6.exchangerate-api.com/v6/pair/{base_code}/{target_code}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
        data = response.json()

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


def pairsLiveRate(api_key, pairs):

    """
    Fetches live conversion rates for multiple currency pairs using ExchangeRate API.

    Parameters:
        api_key (str): Your ExchangeRate API key.
        pairs (list): A list of dictionaries, each containing 'base_code' and 'target_code'.
    Returns:
        list: A list of dictionaries with conversion rates or error messages for each pair.
    """

    currency_rates = []

    for pair in pairs:
        result = liveRate(api_key, pair["base_code"], pair["target_code"])
        if result["status"] == "success":
            currency_rates.append({
                "base_code": result["base_code"],
                "target_code": result["target_code"],
                "conversion_rate": result["conversion_rate"]
            })
        else:
            currency_rates.append({
                "base_code": pair["base_code"],
                "target_code": pair["target_code"],
                "error": result["message"]
            })

    return currency_rates
