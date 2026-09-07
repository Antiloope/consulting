#!/usr/bin/env python3
"""Verifica la sección personal y su integración con la landing."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class AboutParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.section_order: list[str] = []
        self.nav_hrefs: list[str] = []
        self.in_nav = False
        self.about_image: dict[str, str | None] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)

        if tag == "nav" and "site-nav" in (attributes.get("class", "") or "").split():
            self.in_nav = True

        if tag == "section" and (identifier := attributes.get("id")):
            self.section_order.append(identifier)

        if self.in_nav and tag == "a" and (href := attributes.get("href")):
            self.nav_hrefs.append(href)

        if tag == "img" and "about__photo" in (attributes.get("class", "") or "").split():
            self.about_image = attributes

    def handle_endtag(self, tag: str) -> None:
        if tag == "nav" and self.in_nav:
            self.in_nav = False


def main() -> None:
    parser = AboutParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))

    assert "sobre-mi" in parser.section_order, "falta la sección #sobre-mi"
    assert parser.section_order.index("sobre-mi") + 1 == parser.section_order.index("contacto"), (
        "#sobre-mi debe aparecer inmediatamente antes de #contacto"
    )
    assert "#sobre-mi" in parser.nav_hrefs, "falta el acceso a #sobre-mi en el menú"

    image = parser.about_image
    assert image is not None, "falta el retrato en la sección personal"
    assert image.get("alt") == "Rodrigo Pizarro", "el retrato necesita un texto alternativo útil"
    assert image.get("loading") == "lazy", "el retrato fuera del primer viewport debe cargar en diferido"
    assert image.get("width") and image.get("height"), "el retrato debe reservar su espacio"

    source = image.get("src") or ""
    assert source.startswith("assets/img/"), "el retrato debe ser un activo local"
    assert (ROOT / source).is_file(), f"no existe el retrato publicado: {source}"

    print("Sobre mí: sección verificada")


if __name__ == "__main__":
    main()
