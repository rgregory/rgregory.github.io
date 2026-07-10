#!/usr/bin/env python3
from __future__ import annotations

from typing import Any

GOOD_MODELS = {
    ("toyota", "corolla"),
    ("toyota", "camry"),
    ("toyota", "sienna"),
    ("toyota", "tacoma"),
    ("toyota", "avalon"),
    ("honda", "civic"),
    ("honda", "accord"),
    ("honda", "cr-v"),
    ("bmw", "325i"),
}

BAD_YEAR_MODELS = {
    (2012, "ford", "focus"): "PowerShift automatic-transmission complaints make this year/model a known reliability risk.",
    (2013, "ford", "focus"): "PowerShift automatic-transmission complaints make this year/model a known reliability risk.",
    (2014, "ford", "focus"): "PowerShift automatic-transmission complaints make this year/model a known reliability risk.",
    (2011, "chevrolet", "cruze"): "Common reports include turbo/cooling-system issues for this generation.",
    (2012, "chevrolet", "cruze"): "Common reports include turbo/cooling-system issues for this generation.",
    (2013, "chevrolet", "cruze"): "Common reports include turbo/cooling-system issues for this generation.",
    (2014, "nissan", "altima"): "Nissan CVT complaints make this year/model a known reliability risk.",
    (2015, "nissan", "altima"): "Nissan CVT complaints make this year/model a known reliability risk.",
    (2016, "nissan", "altima"): "Nissan CVT complaints make this year/model a known reliability risk.",
}

MAKE_ALIASES = {"chevy": "chevrolet"}


def _norm(value: Any) -> str:
    return str(value or "").strip().lower()


def _year(value: Any) -> int | None:
    try:
        return int(value) if value not in (None, "") else None
    except (TypeError, ValueError):
        return None


def _model_key(model: Any, vehicle: Any = "") -> str:
    text = _norm(model) or _norm(vehicle)
    if not text:
        return ""
    aliases = {
        "crv": "cr-v",
        "cr v": "cr-v",
        "sienna": "sienna",
        "minivan": "sienna",
        "b-series": "b-series",
        "b series": "b-series",
    }
    for needle, canonical in aliases.items():
        if needle in text:
            return canonical
    return text.split()[0].strip(" ,-/")


def reliability_query(listing: dict[str, Any]) -> str:
    year = listing.get("year") or ""
    make = str(listing.get("make") or "").strip()
    model = str(listing.get("model") or "").strip()
    if not make or not model:
        vehicle = str(listing.get("vehicle") or "").strip()
        return f"{vehicle} common problems reliability".strip()
    return f"{year} {make} {model} common problems reliability".strip()


def assess_maintenance_reliability(listing: dict[str, Any]) -> dict[str, str]:
    """Classify year/model reliability as bad, neutral, or good.

    The signal is based on a model-specific common-problems reliability search
    query plus a conservative built-in trend table for common budget cars. It is
    a triage signal, not a mechanical inspection or vehicle-history report.
    """
    year = _year(listing.get("year"))
    make = MAKE_ALIASES.get(_norm(listing.get("make")), _norm(listing.get("make")))
    model = _model_key(listing.get("model"), listing.get("vehicle"))
    query = reliability_query(listing)

    if year is not None and (year, make, model) in BAD_YEAR_MODELS:
        return {
            "maintenance_reliability": "bad",
            "maintenance_reliability_query": query,
            "maintenance_reliability_reason": f"Bad year/model reliability search: known year/model problem trend. {BAD_YEAR_MODELS[(year, make, model)]}",
        }

    if (make, model) in GOOD_MODELS:
        return {
            "maintenance_reliability": "good",
            "maintenance_reliability_query": query,
            "maintenance_reliability_reason": "Good year/model reliability search: no broad known problem trend flagged in the local reliability table; still check recalls, service history, and condition.",
        }

    return {
        "maintenance_reliability": "neutral",
        "maintenance_reliability_query": query,
        "maintenance_reliability_reason": "Neutral year/model reliability search: no specific model problem trend in the local reliability table; manually search/verify common problems before pursuing.",
    }


def enrich_listing(listing: dict[str, Any]) -> dict[str, Any]:
    return {**listing, **assess_maintenance_reliability(listing)}
