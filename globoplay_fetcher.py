from .base import BaseFetcher

class GloboplayFetcher(BaseFetcher):
    def __init__(self):
        self.name = "Globoplay"

    def fetch(self):
        return [
            {"provider": self.name, "raw": {"plan_name": "Mensal", "price_text": "R$ 24,90/mês"}},
            {"provider": self.name, "raw": {"plan_name": "Anual", "price_text": "R$ 19,90/mês"}}
        ]
