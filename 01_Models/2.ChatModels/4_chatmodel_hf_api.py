from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os


load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="google/flan-t5-small",
    # task="text2text-generation"
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    # api_key=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")  
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result)
