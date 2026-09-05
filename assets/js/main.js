/* ==========================================================================
   main.js — progressive enhancement. La página funciona entera sin esto.
   Sin dependencias, sin build. Mantenerlo por debajo de ~3 KB.
   ========================================================================== */
(function () {
  'use strict';

  // Le avisa al fallback del <head> que el enhancement sí corrió.
  document.documentElement.dataset.enhanced = 'true';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var header = document.querySelector('[data-header]');
  var hero = document.querySelector('[data-hero]');
  var ctaBar = document.querySelector('[data-cta-bar]');

  /* ---- Header sólido y CTA fija: ambos dependen de haber pasado el hero.
     Un solo observer para las dos cosas.
     El rootMargin negativo arriba equivale al alto del header: el hero deja
     de "intersectar" justo cuando su borde inferior toca la barra. ----- */
  if (hero && (header || ctaBar)) {
    var headerH = parseFloat(
      getComputedStyle(document.documentElement).getPropertyValue('--header-h')
    ) * 16 || 56;

    new IntersectionObserver(function (entries) {
      var past = !entries[0].isIntersecting;
      if (header) header.dataset.scrolled = String(past);
      if (ctaBar) ctaBar.dataset.visible = String(past);
    }, { rootMargin: '-' + headerH + 'px 0px 0px 0px' }).observe(hero);
  }

  /* ---- Aparición progresiva de bloques -------------------------------- */
  var revealables = document.querySelectorAll('.reveal');
  if (reduceMotion) {
    revealables.forEach(function (el) { el.dataset.visible = 'true'; });
  } else {
    var revealObserver = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.dataset.visible = 'true';
        obs.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    revealables.forEach(function (el) { revealObserver.observe(el); });
  }

  /* ---- Scroll-spy del nav (solo desktop) ------------------------------ */
  var navLinks = Array.prototype.slice.call(
    document.querySelectorAll('[data-nav] a[href^="#"]')
  );
  if (navLinks.length) {
    var byId = {};
    var targets = [];
    navLinks.forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      var section = document.getElementById(id);
      if (!section) return;
      byId[id] = link;
      targets.push(section);
    });

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (l) { l.removeAttribute('aria-current'); });
        var active = byId[entry.target.id];
        if (active) active.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });

    targets.forEach(function (t) { spy.observe(t); });
  }

  /* ---- Un solo servicio abierto a la vez ------------------------------ */
  var disclosures = Array.prototype.slice.call(
    document.querySelectorAll('[data-exclusive] > details')
  );
  disclosures.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      disclosures.forEach(function (other) { if (other !== d) other.open = false; });
    });
  });
})();
