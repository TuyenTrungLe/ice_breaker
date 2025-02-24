import os
from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.tools import BaseTool, Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import  hub
from tools.tools import get_profile_url_tavily
# def lookup(name: str) -> str:
#     return "https://www.linkedin.com/in/letrungtuyen3101/"

def lookup(name: str) -> str:
    llm = ChatOllama(
        model="llama3"  # Hoặc bạn có thể chọn "llama3" hoặc mô hình Ollama khác
    )

    template = """Given the full name {name_of_person}, return only the LinkedIn profile URL 
                in the following exact format: `https://www.linkedin.com/in/<USERNAME>`. 
                Do not include any extra text or comments."""


    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl_Google_Linkedin_Profile",
            func=get_profile_url_tavily,  # Đây có thể là một function để tìm kiếm trên Google hoặc API
            description="Useful for when you need to get the LinkedIn Page URL"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url

if __name__ == "__main__":
    linkedin_url = lookup("Tuyen Le - Data Science Student")
