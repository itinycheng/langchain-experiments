import getpass
from enum import Enum


class LlmType(Enum):
    OPENAI = 1,
    MOONSHOT = 2


class BaseLlmApp:
    """llm app basic class"""

    def __init__(self, name: str, description: str):
        self.llm_type = LlmType.OPENAI
        self.name = name
        self.description = description

    def input_openai_config(self):
        openai_key = getpass.getpass("Please input OpenAI Key: ")
        while True:
            print("test")
            break

        self.llm_type = LlmType.OPENAI

    def llm_config(self):
        pass

