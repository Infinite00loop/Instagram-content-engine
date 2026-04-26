import json
import os
import requests
from crewai.tools import tool

class InternetSearchUtilities():

  @tool("Perform web search")
  def perform_web_search(query: str):
    """Extremely useful for finding up-to-date information on the internet based on a search query."""
    return InternetSearchUtilities.execute_search(query)

  @tool("Perform instagram search")
  def perform_instagram_search(query: str):
    """Specifically tailored for finding Instagram posts and social media trends for a given topic."""
    search_query = f"site:instagram.com {query}"
    return InternetSearchUtilities.execute_search(search_query)

  @staticmethod
  def execute_search(search_term, limit=5):
    endpoint_url = "https://google.serper.dev/search"
    request_data = json.dumps({"q": search_term})
    request_headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    
    api_resp = requests.request("POST", endpoint_url, headers=request_headers, data=request_data)
    organic_results = api_resp.json().get('organic', [])
    
    formatted_output = []
    for item in organic_results[:limit]:
      try:
        formatted_output.append('\n'.join([
            f"Headline: {item['title']}", 
            f"URL: {item['link']}",
            f"Preview: {item['snippet']}", 
            "\n================="
        ]))
      except KeyError:
        continue

    final_str = '\n'.join(formatted_output)
    return f"\nWeb Search Outcomes: {final_str}\n"
