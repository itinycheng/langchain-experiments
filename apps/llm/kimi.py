from langchain.chains import create_sql_query_chain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.utilities import SQLDatabase


class Kwargs:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Person(Kwargs):
    name: str
    age: int


if __name__ == '__main__':
    person = Person(favor="music")
    print(type(person.kwargs))
    print(person)

    llm = ChatOpenAI(
        openai_api_base="https://api.moonshot.cn/v1/",
        openai_api_key="sk-***",
        model_name="moonshot-v1-8k",
    )

    db = SQLDatabase.from_uri("sqlite:///Chinook.db", sample_rows_in_table_info=3)
    print(db.dialect)

    chain = create_sql_query_chain(llm, db)
    chain.get_prompts()[0].pretty_print()
    print(llm.invoke("how can langsmith help with testing?"))
