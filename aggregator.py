def find_best(plans, rates=None):
    rates = rates or {"BRL": 1.0}
    valid = [p for p in plans if p["price"] is not None]
    for p in valid:
        rate = rates.get(p["currency"], 1.0)
        p["price_brl"] = p["price"] * rate
    return min(valid, key=lambda x: x["price_brl"], default=None)
