import json
import os

DEFAULT_BASE_CURRENCY = "COP"
TASAS_PATH = "tasas_cambio.json"


def normalize_currency(code):
    if code is None:
        return ""
    return str(code).strip().upper()


def load_tasas():
    if not os.path.exists(TASAS_PATH):
        return []
    try:
        with open(TASAS_PATH, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
    except (json.JSONDecodeError, IOError):
        return []
    if isinstance(contenido, dict):
        return [contenido]
    if isinstance(contenido, list):
        return contenido
    return []


def save_tasas(tasas):
    with open(TASAS_PATH, "w", encoding="utf-8") as archivo:
        json.dump(tasas, archivo, indent=4, ensure_ascii=False)


def get_base_currency(tasas):
    for tasa in tasas:
        moneda_base = normalize_currency(tasa.get("moneda_base"))
        if moneda_base:
            return moneda_base
    return DEFAULT_BASE_CURRENCY


def get_rate(moneda_origen, moneda_base, tasas):
    origen = normalize_currency(moneda_origen)
    base = normalize_currency(moneda_base) or get_base_currency(tasas)
    if not origen or not base:
        return None
    if origen == base:
        return 1.0
    for tasa in tasas:
        if normalize_currency(tasa.get("moneda_origen")) == origen and normalize_currency(tasa.get("moneda_base")) == base:
            try:
                valor = float(tasa.get("tasa", 0))
                return valor if valor > 0 else None
            except (TypeError, ValueError):
                return None
    return None


def convert_to_base(monto, moneda_origen, moneda_base, tasas):
    tasa = get_rate(moneda_origen, moneda_base, tasas)
    if tasa is None:
        return None
    try:
        return round(float(monto) * tasa, 2)
    except (TypeError, ValueError):
        return None
