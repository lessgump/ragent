from ragent.models import Answer


class Retriever:
    def __init__(self) -> None:
        pass


    def query(self, query: str, top_k: int = 1) -> Answer:
        pass


class LanguageModel:
    def __init__(self) -> None:
        self._client = None

    def _init_client(self):
        self._client = OpenAI()


class Embedding:
    pass


class KnowledgeBase:
    pass


class EmbeddingStorage:
    pass

