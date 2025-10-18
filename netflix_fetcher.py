from .base import BaseFetcher

class NetflixFetcher(BaseFetcher):
    def __init__(self):
        self.name = "Netflix"

    def fetch(self):
        return [
            {"provider": self.name, "raw": {"plan_name": "Padrão com anúncios", "price_text": "R$ 20,90/mês"}},
            {"provider": self.name, "raw": {"plan_name": "Padrão", "price_text": "R$ 44,90/mês"}},
            {"provider": self.name, "raw": {"plan_name": "Premium", "price_text": "R$ 59,90/mês"}}
        ]
