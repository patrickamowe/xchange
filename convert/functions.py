import requests

def fetch_top_headlines(api_key, country):
    """
    Fetches the top headlines for a specified country using News API.

    Parameters:
        api_key (str): Your News API key.
        country (str): The country code (e.g., 'us' for the United States).

    Returns:
        respond: A dictionary with the status, total results, and list of articles.
    """
    # Define the base URL and parameters
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": api_key
    }

    respond = requests.get(base_url, params=params)
    return respond


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

    respond = requests.get(base_url, params=params)
    return respond
