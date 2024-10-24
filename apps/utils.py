import logging
import os
from typing import Dict, Callable

from langchain_community.chat_models import ChatOpenAI

from apps.base import LlmType


def is_valid_openai_config(key: str) -> bool:
    if key is None:
        return False

    try:
        llm = ChatOpenAI(openai_api_key=key, model="gpt-3.5-turbo", temperature=0)
        response = llm.invoke("Hello world!")
        logging.info(f"call openai: {response}")
        return True
    except Exception as ex:
        logging.warning("Validate llm config failed", ex)
        return False


fn_dict: Dict[LlmType, Callable[[str], bool]] = {
    LlmType.OPENAI: is_valid_openai_config,
}

if __name__ == '__main__':
    os.environ["OPENAI_API_KEY"] = "sk-***"
    flag = is_valid_openai_config("sk-***")
    print(flag)
