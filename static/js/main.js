document.addEventListener('DOMContentLoaded', () => {
    const sidebar   = document.querySelector('.sidebar');
    const closeBtn  = document.querySelector('#btn');
    const searchBtn = document.querySelector('.bx-search');
    const peekBtn   = document.querySelector('#hideBtn'); // ← your “chevrons” button
  
    // toggle open/closed
    closeBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      updateMenuIcon();
    });
  
    // same for search icon
    searchBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      updateMenuIcon();
    });
  
    // peek in/out by 80px
    peekBtn.addEventListener('click', () => {
      sidebar.classList.toggle('peeked');
    });
  
    function updateMenuIcon() {
      if (sidebar.classList.contains('open')) {
        closeBtn.classList.replace('bx-menu', 'bx-menu-alt-right');
      } else {
        closeBtn.classList.replace('bx-menu-alt-right', 'bx-menu');
      }
    }
  });
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.sidebar').classList.add('peeked');
  });
  
  // JS to toggle the submenu open/closed
  document.querySelectorAll('.has-submenu > .submenu-toggle').forEach(toggle => {
    toggle.addEventListener('click', e => {
      e.preventDefault();
      toggle.parentElement.classList.toggle('open-submenu');
    });
  });
  