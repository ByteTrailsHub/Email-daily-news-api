# Daily Email News API
This Python project fetches the latest news headlines from an online API (NewsAPI) and sends them as a daily email. It consists of two main files:

main.py – Fetches articles and formats the email body.
send_email.py – Handles the actual sending of emails via Gmail.

## Table of Contents
1. Features
2. Prerequisites
3. Installation
4. Getting Your NewsAPI Key
5. Setup and Configuration
6. Running the Script
7. Customization
   
### Features
Retrieves the top headlines from a news source using NewsAPI.
Sends an email containing these headlines to a specified recipient.
Easy to schedule as a daily cron job or Windows Task Scheduler to automate your daily news digest.

### Prerequisites
1. Python 3.7+ (or a recent version).
2. A NewsAPI account and API key (free sign-up).
3. A Gmail account with App Passwords enabled (for secure sign-in).

### Installation
1. Clone or download this repository.
2. (Optional but recommended) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3. Install dependencies:
pip install requests

### Getting Your NewsAPI Key
1. Go to https://newsapi.org/ and click Get API Key (or Get Started).
2. Sign up for a free account (or log in if you already have one).
3. Navigate to your Profile or API Key section to find your API key.
4. Copy that key and paste it into your code (in main.py) or set it as an environment variable (recommended).
   
### Setup and Configuration
1. NewsAPI Key
In main.py, locate the line with:
api_key = "YOUR_NEWSAPI_KEY"
url = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&country=us"
Replace "YOUR_NEWSAPI_KEY" with your actual key from NewsAPI.

(Alternatively, you can store the key in an environment variable and read it in Python using os.environ—this is more secure.)

2. Gmail Credentials
In send_email.py, you’ll find:
username = "YOUR_GMAIL_ADDRESS"
password = "YOUR_GMAIL_APP_PASSWORD"
receiver = "RECIPIENT_EMAIL"
username: Your full Gmail address (e.g., myaccount@gmail.com).
password: Your Gmail App Password (not your normal Gmail password!).
receiver: The email address where you want to send the news (can be the same as username or different).

Note: You must enable 2-Step Verification on your Gmail account and create an App Password. Then paste that App Password here.

### Running the Script
1. Make sure you’ve installed dependencies and configured your API key and Gmail credentials.
2. Run:
python main.py
3. The script will:
Fetch the top headlines from NewsAPI.
Build a message body.
Call send_email(message) to email the headlines to the specified recipient.

### Customization
Change the country or category in the NewsAPI URL. For example:
url = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&country=th"
or
url = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&category=technology"
Adjust the number of articles in main.py by modifying:
for article in content['articles'][:20]:
    ...
Schedule the script:
On Linux/macOS, create a cron job.
On Windows, use Task Scheduler. This way, you can receive the email every morning automatically.


Enjoy your daily news updates via email! If you have any questions or issues, please open an issue or submit a pull request.
