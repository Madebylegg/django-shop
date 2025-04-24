document.addEventListener('DOMContentLoaded', () => {
  const sidebar   = document.querySelector('.sidebar');
  const closeBtn  = document.querySelector('#btn');
  const searchBtn = document.querySelector('.bx-search');
  const peekBtn   = document.querySelector('#hideBtn'); // ← chevrons
  const submenuToggles = document.querySelectorAll('.has-submenu > .submenu-toggle');

  // Auto open if screen is wide enough
  if (window.innerWidth >= 430) {
    sidebar.classList.add('open');
  }

  // Optional: Add peeked default
  sidebar.classList.add('peeked');

  // toggle open/closed with menu icon
  closeBtn?.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    updateMenuIcon();
  });

  // toggle open/closed with search icon
  searchBtn?.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    updateMenuIcon();
  });

  // peek in/out by 80px
  peekBtn?.addEventListener('click', () => {
    sidebar.classList.toggle('peeked');
  });

  // toggle submenu visibility
  submenuToggles.forEach(toggle => {
    toggle.addEventListener('click', e => {
      e.preventDefault();
      toggle.parentElement.classList.toggle('open-submenu');
    });
  });

  function updateMenuIcon() {
    if (sidebar.classList.contains('open')) {
      closeBtn?.classList.replace('bx-menu', 'bx-menu-alt-right');
    } else {
      closeBtn?.classList.replace('bx-menu-alt-right', 'bx-menu');
    }
  }
});

  // JS to toggle the submenu open/closed
  document.querySelectorAll('.has-submenu > .submenu-toggle').forEach(toggle => {
    toggle.addEventListener('click', e => {
      e.preventDefault();
      toggle.parentElement.classList.toggle('open-submenu');
    });
  });