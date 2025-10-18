from .base import BaseFetcher

class HBOMaxFetcher(BaseFetcher):
    def __init__(self):
        self.name = "HBO Max"

    def fetch(self):
        return [
            {"provider": self.name, "raw": {"plan_name": "Mobile", "price_text": "R$ 29,90/mês"}},
            {"provider": self.name, "raw": {"plan_name": "Multitelas", "price_text": "R$ 39,90/mês"}}
        ]
