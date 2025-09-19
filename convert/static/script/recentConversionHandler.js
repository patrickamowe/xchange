import { clearRecentConversions } from "./api";


export function recentConversionHandler() {
        
        // Clear button functionality
        const clearBtn = document.getElementById("clear-recent");
        clearBtn.addEventListener("click", () => {
            clearRecentConversions();
            listContainer.innerHTML = "";
            const listItem = document.createElement("li");
            listItem.className = "list-group-item";
            listItem.textContent = "No recent conversions.";
            listContainer.appendChild(listItem);
        });
    }