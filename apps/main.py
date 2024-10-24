import sys

from apps.qa_rag import QaRagApp
from apps.sql_agent import SqlAgentApp
from apps.base import BaseLlmApp

all_apps = {
    1: SqlAgentApp(),
    2: QaRagApp(),
}


def select_app() -> BaseLlmApp | None:
    print("=============== all apps ===============")
    print(" 1. sql_agent: Q&A over SQL + CSV      =")
    print(" 2. qa_rag: Q&A with RAG               =")
    print("========================================")

    while True:
        app_id = input("\nPlease select an application：").strip().upper()
        if app_id == "QUIT" or app_id == "EXIT":
            break
        elif app_id.isdigit():
            app = all_apps.get(int(app_id))
            if app is not None:
                return app
        print("Input app id: {} is invalid".format(app_id))


def run_app():
    selected = select_app()
    if selected is None:
        sys.exit()

    selected.llm_config()
    print("app name: ", selected.name)


if __name__ == '__main__':
    run_app()
