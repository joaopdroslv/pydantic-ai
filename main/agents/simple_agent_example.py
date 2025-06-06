from pydantic_ai import Agent

from main.models.local_qwen import local_qwen
from main.schemas.location import Location

# Minimal configuration, just one response template for the output
agent = Agent(local_qwen, output_type=Location)

# result = agent.run_sync('Where were the olympics held in 2012?')
result = agent.run_sync("Where was Isac Newton born?")

print(result.output)
# > city='London' country='United Kingdom'

print(result.usage())
# > Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65)
