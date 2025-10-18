from .base import BaseFetcher

class PrimeFetcher(BaseFetcher):
    def __init__(self):
        self.name = "Prime Video"

    def fetch(self):
        return [
            {"provider": self.name, "raw": {"plan_name": "Único", "price_text": "R$ 19,90/mês"}}
        ]
