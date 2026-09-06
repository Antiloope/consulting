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
  var contacto = document.getElementById('contacto');

  /* El rootMargin negativo arriba equivale al alto del header: el hero deja
     de "intersectar" justo cuando su borde inferior toca la barra. Lo usan
     el header sólido y la CTA fija, así que se calcula una sola vez. */
  var headerH = parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue('--header-h')
  ) * 16 || 56;
  var pastHeroMargin = '-' + headerH + 'px 0px 0px 0px';

  /* ---- Header sólido: depende de haber pasado el hero. --------------- */
  if (hero && header) {
    new IntersectionObserver(function (entries) {
      header.dataset.scrolled = String(!entries[0].isIntersecting);
    }, { rootMargin: pastHeroMargin }).observe(hero);
  }

  /* ---- CTA fija: visible después del hero, pero no mientras el visitante
     ya está parado en #contacto (ahí el botón real está a la vista y la
     barra solo taparía contenido). Dos observers, un solo estado derivado. */
  if (hero && ctaBar) {
    var pastHero = false;
    var inContacto = false;
    var syncCtaBar = function () {
      ctaBar.dataset.visible = String(pastHero && !inContacto);
    };

    new IntersectionObserver(function (entries) {
      pastHero = !entries[0].isIntersecting;
      syncCtaBar();
    }, { rootMargin: pastHeroMargin }).observe(hero);

    if (contacto) {
      new IntersectionObserver(function (entries) {
        inContacto = entries[0].isIntersecting;
        syncCtaBar();
      }, { rootMargin: '0px 0px -20% 0px' }).observe(contacto);
    }
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
