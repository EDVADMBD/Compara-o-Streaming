from .base import BaseFetcher

class DisneyPlusFetcher(BaseFetcher):
    def __init__(self):
        self.name = "Disney+"

    def fetch(self):
        return [
            {"provider": self.name, "raw": {"plan_name": "Standard", "price_text": "R$ 46,90/mês"}},
            {"provider": self.name, "raw": {"plan_name": "Premium", "price_text": "R$ 66,90/mês"}}
        ]
