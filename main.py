from db import init_db, save_plans
from aggregator import find_best
from normalizer import normalize

from fetchers.netflix_fetcher import NetflixFetcher
from fetchers.disneyplus_fetcher import DisneyPlusFetcher
from fetchers.prime_fetcher import PrimeFetcher
from fetchers.hbomax_fetcher import HBOMaxFetcher
from fetchers.globoplay_fetcher import GloboplayFetcher

def run_once():
    init_db()

    fetchers = [
        NetflixFetcher(),
        DisneyPlusFetcher(),
        PrimeFetcher(),
        HBOMaxFetcher(),
        GloboplayFetcher(),
    ]

    all_raw = []
    for f in fetchers:
        try:
            data = f.fetch()
            all_raw.extend(data)
        except Exception as e:
            print(f"Erro ao buscar {f.name}: {e}")

    normalized = [normalize(r) for r in all_raw if r]
    save_plans(normalized)

    best = find_best(normalized)
    print("\n--- Melhor plano encontrado ---")
    print(f"{best['provider']} - {best['plan']} => R$ {best['price']} ({best['period']})")

if __name__ == "__main__":
    run_once()
