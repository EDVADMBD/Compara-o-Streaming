import re

def parse_price_text(price_text):
    match = re.search(r"R\$ ?([\d,]+)", price_text)
    if match:
        value = float(match.group(1).replace(",", "."))
    else:
        value = None
    return {"price": value, "currency": "BRL", "period": "mensal"}

def normalize(entry):
    raw = entry["raw"]
    plan = raw.get("plan_name")
    parsed = parse_price_text(raw.get("price_text", ""))
    return {
        "provider": entry["provider"],
        "plan": plan,
        "price": parsed["price"],
        "currency": parsed["currency"],
        "period": parsed["period"]
    }
