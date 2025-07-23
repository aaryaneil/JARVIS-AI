import logging
from livekit.agents import function_tool, RunContext

import requests

from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(
    run_context: RunContext,
    location: str,) -> str:
    """
    Get the current weather for a given location.
    """

    try:
        response = requests.get(
            f"https://wttr.in/{location}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {location}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"Failed to get weather for {location}: {response.status_code}")
            return f"Could not retrieve weather data for {location}."
    except Exception as e:
        logging.error(f"Error fetching weather data: {e}")
        return f"An error occurred while retrieving weather data for {location}."
    


@function_tool()
async def search_web(
    run_context: RunContext,
    query: str,
) -> str:
    """
    Search the web using DuckDuckGo and return the results.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        if results:
            logging.info(f"Search results for '{query}': {results}")
            return results
        else:
            logging.warning(f"No results found for '{query}'.")
            return "No results found."
    except Exception as e:
        logging.error(f"Error during web search: {e}")
        return "An error occurred while searching the web."