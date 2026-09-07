#!/usr/bin/env python3
"""Verifica el flujo de contacto directamente sobre el HTML publicado."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent


class ContactParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_contact = False
        self.contact_depth = 0
        self.contact_links: list[str] = []
        self.contact_ctas: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)

        if tag == "section" and attributes.get("id") == "contacto":
            self.in_contact = True
            self.contact_depth = 1
        elif self.in_contact:
            self.contact_depth += 1

        if tag == "a" and "data-contact-cta" in attributes:
            self.contact_ctas.append(attributes.get("href", ""))

        if self.in_contact and tag == "a" and "data-contact-method" in attributes:
            self.contact_links.append(attributes.get("href", ""))

    def handle_endtag(self, tag: str) -> None:
        if not self.in_contact:
            return

        self.contact_depth -= 1
        if self.contact_depth == 0:
            self.in_contact = False


def main() -> None:
    parser = ContactParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))

    assert len(parser.contact_ctas) >= 2, "faltan CTA principales marcados"
    assert all(href == "#contacto" for href in parser.contact_ctas), (
        "todos los CTA principales deben llevar a #contacto"
    )

    assert len(parser.contact_links) == 3, (
        "Contacto debe ofrecer exactamente tres métodos"
    )

    schemes = {urlparse(href).scheme for href in parser.contact_links}
    hosts = {urlparse(href).netloc.removeprefix("www.") for href in parser.contact_links}
    assert "mailto" in schemes, "falta el enlace de email"
    assert "linkedin.com" in hosts, "falta el enlace de LinkedIn"
    assert "cal.com" in hosts, "falta el enlace de Cal.com"
    assert not any("REEMPLAZAR" in href for href in parser.contact_links), (
        "el enlace de Cal.com todavía es un marcador"
    )

    print("Contacto: flujo verificado")


if __name__ == "__main__":
    main()
