#!/usr/bin/env python3
"""Checks the static component inventory's user-visible contract."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "mockups" / "component-inventory.html"
LANDING = ROOT / "index.html"
AGENTS = ROOT / "AGENTS.md"


class InventoryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.document_language = ""
        self.ids: set[str] = set()
        self.stylesheets: set[str] = set()
        self.nav_labels: list[str] = []
        self.classes: set[str] = set()
        self.hrefs: set[str] = set()
        self.final_components: list[str] = []
        self.minimum_targets: list[int] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.document_language = attributes.get("lang", "") or ""
        if identifier := attributes.get("id"):
            self.ids.add(identifier)
        if tag == "link" and attributes.get("rel") == "stylesheet":
            self.stylesheets.add(attributes.get("href", "") or "")
        if tag == "nav":
            self.nav_labels.append(attributes.get("aria-label", "") or "")
        if href := attributes.get("href"):
            self.hrefs.add(href)
        if component := attributes.get("data-final-component"):
            self.final_components.append(component)
        if minimum_target := attributes.get("data-min-target"):
            self.minimum_targets.append(int(minimum_target))
        self.classes.update((attributes.get("class", "") or "").split())


def main() -> None:
    assert INVENTORY.exists(), "Falta mockups/component-inventory.html"

    parser = InventoryParser()
    parser.feed(INVENTORY.read_text(encoding="utf-8"))

    landing_parser = InventoryParser()
    landing_parser.feed(LANDING.read_text(encoding="utf-8"))

    assert parser.document_language == "es"
    assert parser.stylesheets == {
        "../assets/css/tokens.css",
        "../assets/css/base.css",
        "../assets/css/layout.css",
        "../assets/css/components.css",
        "../assets/css/sections.css",
    }
    assert "sistema-final" in parser.ids
    assert "propuesta" not in parser.ids
    assert "Secciones del inventario" in parser.nav_labels
    assert len(parser.final_components) == 10
    assert not any(name.startswith("v2-") for name in parser.classes)
    assert not ({"btn--sm", "tag--neutral"} & landing_parser.classes)
    assert parser.minimum_targets and min(parser.minimum_targets) >= 44
    assert {
        "btn",
        "tag",
        "card",
        "quote",
        "stat",
        "timeline",
        "compare",
        "disclosure",
        "matrix",
        "hero",
        "contact",
    } <= parser.classes

    assert AGENTS.exists(), "Falta AGENTS.md"
    agent_rules = AGENTS.read_text(encoding="utf-8")
    assert "PRODUCT.md" in agent_rules
    assert "DESIGN.md" in agent_rules
    assert "mockups/component-inventory.html" in agent_rules

    print("component inventory: ok")


if __name__ == "__main__":
    main()
