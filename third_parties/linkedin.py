import os
from http.client import responses

import requests
from dotenv import load_dotenv

load_dotenv()

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from LinkedIn profiles.
    Manually scrape the information from the LinkedIn profile.
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/TuyenTrungLe/27bfeee71a30ed3386c0ef1a38fe4ec5/raw/4e862a15c1ec432228995217d84761b302a225ed/le-trung-tuyen-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "LinkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params = params,
            timeout= 10,
        )
    data = response.json().get("person")
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/letrungtuyen3101/", mock=True,
        ),
    )