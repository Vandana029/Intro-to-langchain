from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# NOTE: All Chat Models are inherited from `BaseChatModel` class.

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("What is the capital of India?")

# gives additional metadata alongside the actual result
print(result)

# gives only the result without any metadata
print(result.content) 