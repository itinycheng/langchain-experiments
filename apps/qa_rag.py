from base import BaseLlmApp


class QaRagApp(BaseLlmApp):
    """Q&A with RAG"""

    def __init__(self):
        super().__init__("qa_rag", self.__doc__)
