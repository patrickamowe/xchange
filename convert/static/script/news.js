export function hiddenNews() {
    const btn = document.getElementById("news-toggle-btn");
    const items = document.querySelectorAll(".news-card");

    let visibleCount = 8; // starting with 8

    // Hide items after the first 8 initially
    items.forEach((item, index) => {
        if (index >= visibleCount) {
            item.classList.add("hidden");
        }
    });

    btn.addEventListener("click", function(e) {
        e.preventDefault();

        if (btn.textContent.trim().toLowerCase() === "read more") {
            // Show next 8
            visibleCount += 8;
            items.forEach((item, index) => {
                if (index < visibleCount) {
                    item.classList.remove("hidden");
                }
            });

            // If all are visible, change to "Read Less"
            if (visibleCount >= items.length) {
                btn.textContent = "Read Less";
            }

        } else {
            // Reset back to 8
            visibleCount = 8;
            items.forEach((item, index) => {
                if (index >= visibleCount) {
                    item.classList.add("hidden");
                }
            });
            btn.textContent = "Read More";
        }
    });
}
