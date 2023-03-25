import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()
apiKeyNasa = os.environ["NASA"]
params = {
  'api_key' : apiKeyNasa,
  'hd':'True'
}
url = f'https://api.nasa.gov/planetary/apod?api_key={str(apiKeyNasa)}'

def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False
def getAPOD():
  request = requests.get(url)
  data = check_valid_status_code(request)

  return data