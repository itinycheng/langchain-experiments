from base import BaseLlmApp
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI


class SqlAgentApp(BaseLlmApp):
    """Q&A over SQL + CSV"""

    def __init__(self):
        super().__init__("sql_agent", self.__doc__)

    def build_llm(self, uri: str = ""):
        print("~~~")
