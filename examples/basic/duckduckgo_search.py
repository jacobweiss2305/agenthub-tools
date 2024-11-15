from hive import Nest, Worker
from hive_tools.duckduckgo import duckduckgo_search, duckduckgo_news

nest = Nest()

english_agent = Worker(
    name="English AI",
    instructions="You only speak English.",
)

messages = [{"role": "user", "content": "What is the weather in Tokyo?"}]
response = nest.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])
 