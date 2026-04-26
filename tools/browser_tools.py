import json
import os
import requests
from crewai import Agent, Task
from crewai.tools import tool
from unstructured.partition.html import partition_html

class WebScrapingUtilities():

  @tool("Extract webpage data")
  def extract_and_summarize_webpage(website: str):
    """A highly effective tool for scraping and generating a summary of a website's content.
    Provide the full URL without a trailing slash (e.g., https://apple.com)."""
    endpoint = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    req_payload = json.dumps({"url": website})
    req_headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    api_response = requests.request("POST", endpoint, headers=req_headers, data=req_payload)
    
    parsed_elements = partition_html(text=api_response.text)
    full_text = "\n\n".join([str(element) for element in parsed_elements])
    text_chunks = [full_text[idx:idx + 8000] for idx in range(0, len(full_text), 8000)]
    
    generated_summaries = []
    for chunk_data in text_chunks:
      summarizer_agent = Agent(
          role='Senior Data Summarizer',
          goal='Conduct thorough research and distill complex web content into highly accurate summaries',
          backstory="You are an elite Senior Data Summarizer. Your job is to extract the core value from raw internet data.",
          llm=os.environ['MODEL'],
          allow_delegation=False)
          
      summarization_task = Task(
          agent=summarizer_agent,
          description=f'Read the following text and write an extensive, detailed summary capturing all vital information. Do not return anything other than the summary itself.\n\nSOURCE TEXT:\n----------\n{chunk_data}',
          expected_output="A comprehensive text summary of the given content chunk."
      )
      
      chunk_summary = summarization_task.execute_sync()
      if hasattr(chunk_summary, 'raw'):
          generated_summaries.append(chunk_summary.raw)
      else:
          generated_summaries.append(str(chunk_summary))
      
    final_output = "\n\n".join(generated_summaries)
    return f'\nExtracted Web Content Summary: {final_output}\n'
