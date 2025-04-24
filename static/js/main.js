document.addEventListener("DOMContentLoaded", () => {
	const sidebar = document.querySelector(".sidebar");
	const btn = document.querySelector("#btn");
	const searchBtn = document.querySelector(".bx-search");
	const peekBtn = document.querySelector("#hideBtn"); // your “chevrons” button
	const submenuToggles = document.querySelectorAll(
		".has-submenu > .submenu-toggle"
	);

	// Initialize sidebar in peeked state
	sidebar.classList.add("peeked");

	// Helper to swap the menu icon
	function updateMenuIcon() {
		btn.classList.toggle("bx-menu", !sidebar.classList.contains("open"));
		btn.classList.toggle(
			"bx-menu-alt-right",
			sidebar.classList.contains("open")
		);
	}

	// Toggle open/closed & update icon
	function toggleSidebar() {
		sidebar.classList.toggle("open");
		updateMenuIcon();
	}

	// Event bindings
	btn.addEventListener("click", toggleSidebar);
	searchBtn.addEventListener("click", toggleSidebar);
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
