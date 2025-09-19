export function hiddenNewsHandler() {
    const btn = document.getElementById("news-toggle-btn");
    const items = document.querySelectorAll(".news-card");

    let visibleCount = 8; // starting with 8

    btn.addEventListener("click", () => {
       
        console.log("Button clicked");

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
