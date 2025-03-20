# Xchange

## Description
Xchange is a currency convertor website application that uses an exchange API to fetch real-time currency rates and convert them into different currencies. Additionally, it integrates the News API to provide crypto-related news, keeping users informed about the latest trends in the cryptocurrency market.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript and BootStrap
- **Backend:** Django, Python
- **APIs:** Exchange Rate API, News API

## Pages in the Application
- **Index Page:** The homepage where users can input currencies and get conversion results.
- **News:** Displays the latest financial and cryptocurrency-related news.
- **Login & Register Page:** Allows users to create accounts and login to access additional features.
- **Available Currency Page:** Lists all supported currencies and their exchange rates.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (version 3.x)
- Django

### Steps to Install
1. Clone the repository:
   ```sh
   git clone https://github.com/patrickamowe/xchange.git
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```sh
   python manage.py makemigrations
   ```
   ```sh
   python manage.py migrate
   ```
6. Add supported currencies to the database:
   ```sh
   python manage.py add_currencies
   ```
7. Start the development server:
   ```sh
   python manage.py runserver
   ```
8. Open the application in a web browser:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- Enter the amount and select currencies to convert.
- View real-time exchange rates.
- Register/login to access saved conversion history.
- Check financial and cryptocurrency news related to currency markets.

## License
This project is licensed under the MIT License.

