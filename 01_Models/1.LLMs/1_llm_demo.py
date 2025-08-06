from langchain_openai import OpenAI
from dotenv import load_dotenv

# NOTE: All LLMS are inherited from `BaseLLM` class.
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India?")

print(result) # O/P: The capital of India is New Delhi. (as a string)