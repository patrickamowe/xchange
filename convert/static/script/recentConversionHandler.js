import { clearRecentConversions } from "./API.js";


export function recentConversionHandler() {
    
    // Clear button functionality
    const clearBtn = document.getElementById("clear-recent");
    const listContainer = document.getElementById("recent-activity-list");
    const isEmpty = listContainer.getAttribute("isEmpty");
    
    if (isEmpty === "False") {
        clearBtn.addEventListener("click", () => {
            clearRecentConversions();
            listContainer.innerHTML = "";
            const listItem = document.createElement("li");
            listItem.className = "list-group-item";
            listItem.textContent = "No recent conversions.";
            listContainer.appendChild(listItem);
        });
    }else {
        return;
    }
}