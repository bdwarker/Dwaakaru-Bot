import requests
import os
from dotenv import load_dotenv
load_dotenv()
url = f"https://quotes15.p.rapidapi.com/quotes/random/?rapidapi-key={str(os.environ['QUOTEAPI'])}"

def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_quote():
    request = requests.get(url)
    data = check_valid_status_code(request)
    return data