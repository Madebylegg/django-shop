document.addEventListener("DOMContentLoaded", () => {
	const sidebar = document.querySelector(".sidebar");
	const btn = document.querySelector("#btn");
	const searchBtn = document.querySelector(".bx-search");
	const peekBtn = document.querySelector("#hideBtn");
	const submenuToggles = document.querySelectorAll(".has-submenu > .submenu-toggle");
	const submenuItems = document.querySelectorAll(".has-submenu");
  
	// Start in peeked mode
	sidebar.classList.add("peeked");
  
	// Helper: update hamburger icon
	function updateMenuIcon() {
	  btn.classList.toggle("bx-menu", !sidebar.classList.contains("open"));
	  btn.classList.toggle("bx-menu-alt-right", sidebar.classList.contains("open"));
	}
  
	// Handle sidebar toggle with submenu reset
	function toggleSidebar() {
	  const isOpen = sidebar.classList.contains("open");
  
	  sidebar.classList.toggle("open");
	  updateMenuIcon();
  
	  // If sidebar is closing, remove open-submenu from all
	  if (isOpen) {
		submenuItems.forEach(item => item.classList.remove("open-submenu"));
	  }
	}
  
	// Toggle sidebar from hamburger or search
	btn.addEventListener("click", toggleSidebar);
	searchBtn.addEventListener("click", toggleSidebar);
  
	// Toggle peek mode
	peekBtn.addEventListener("click", () => {
	  sidebar.classList.toggle("peeked");
	});
  
	// Submenu toggles
	submenuToggles.forEach((toggle) => {
	  toggle.addEventListener("click", (e) => {
		e.preventDefault();
		toggle.parentElement.classList.toggle("open-submenu");
	  });
	});
  });