# aihive_tools/duckduckgo/tools.py
import json
from typing import Any, Optional

try:
    from duckduckgo_search import DDGS
except ImportError:
    raise ImportError(
        "`duckduckgo-search` not installed. Please install using `pip install aihive-tools-duckduckgo`"
    )

def duckduckgo_search(query: str, max_results: Optional[int] = 5, **kwargs) -> str:
    """Search DuckDuckGo for a query.
    
    Args:
        query (str): The query to search for
        max_results (Optional[int]): Maximum number of results to return
        **kwargs: Additional arguments passed to DDGS
            - headers (Optional[Any]): Custom headers for requests
            - proxy (Optional[str]): Single proxy configuration
            - proxies (Optional[Any]): Multiple proxy configuration
            - timeout (Optional[int]): Request timeout in seconds
        
    Returns:
        str: JSON string of search results
    """
    ddgs = DDGS(
        headers=kwargs.get('headers'),
        proxy=kwargs.get('proxy'),
        proxies=kwargs.get('proxies'),
        timeout=kwargs.get('timeout', 10)
    )
    results = ddgs.text(
        keywords=query,
        max_results=max_results
    )
    return json.dumps(list(results), indent=2)  # Convert generator to list

def duckduckgo_news(query: str, max_results: Optional[int] = 5, **kwargs) -> str:
    """Get latest news from DuckDuckGo.
    
    Args:
        query (str): The query to search for
        max_results (Optional[int]): Maximum number of results to return
        **kwargs: Additional arguments passed to DDGS
            - headers (Optional[Any]): Custom headers for requests
            - proxy (Optional[str]): Single proxy configuration
            - proxies (Optional[Any]): Multiple proxy configuration
            - timeout (Optional[int]): Request timeout in seconds
        
    Returns:
        str: JSON string of news results
    """
    ddgs = DDGS(
        headers=kwargs.get('headers'),
        proxy=kwargs.get('proxy'),
        proxies=kwargs.get('proxies'),
        timeout=kwargs.get('timeout', 10)
    )
    results = ddgs.news(
        keywords=query,
        max_results=max_results
    )
    return json.dumps(list(results), indent=2)  # Convert generator to list