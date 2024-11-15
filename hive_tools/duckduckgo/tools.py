from duckduckgo_search import DDGS
from typing import Optional
import json

def duckduckgo_search(headers: dict, proxy: str, proxies: dict, timeout: int, query: str, max_results: Optional[int] = 5) -> str:
    """Use this function to search DuckDuckGo for a query.

    Args:
        headers(dict): The headers to use for the request.
        proxy(str): The proxy to use for the request.
        proxies(dict): The proxies to use for the request.
        timeout(int): The timeout to use for the request.
        query(str): The query to search for.
        max_results (optional, default=5): The maximum number of results to return.

    Returns:
        The result from DuckDuckGo.
    """
    ddgs = DDGS(headers=headers, proxy=proxy, proxies=proxies, timeout=timeout)
    return json.dumps(ddgs.text(keywords=query, max_results=max_results), indent=2)

def duckduckgo_news(headers: dict, proxy: str, proxies: dict, timeout: int, query: str, max_results: Optional[int] = 5) -> str:
    """Use this function to get the latest news from DuckDuckGo.

    Args:
        headers(dict): The headers to use for the request.
        proxy(str): The proxy to use for the request.
        proxies(dict): The proxies to use for the request.
        timeout(int): The timeout to use for the request.
        query(str): The query to search for.
        max_results (optional, default=5): The maximum number of results to return.

    Returns:
        The latest news from DuckDuckGo.
    """
    ddgs = DDGS(headers=headers, proxy=proxy, proxies=proxies, timeout=timeout)
    return json.dumps(ddgs.news(keywords=query, max_results=max_results), indent=2)