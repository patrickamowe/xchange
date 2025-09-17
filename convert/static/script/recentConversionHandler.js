import { clearConversions, getConversions } from "./recentConversion.js";


export function recentConversionHandler() {
    // Display recent conversions
    const recentConversions = getConversions();
    const listContainer = document.getElementById("recent-activity-list");
    listContainer.innerHTML = ""; // Clear existing list

    if (recentConversions.length === 0) {
        const listItem = document.createElement("li");
        listItem.className = "list-group-item";
        listItem.textContent = "No recent conversions.";
        listContainer.appendChild(listItem);
        return;
    }

    recentConversions.forEach(conversion => {
        const listItem = document.createElement("li");
        listItem.className = "list-group-item";
        const date = new Date(conversion.timestamp);
        listItem.textContent = `${conversion.base} → ${conversion.quote} (on ${date.toLocaleString()})`;
        listContainer.appendChild(listItem);
        
    });


    // Clear button functionality
    const clearBtn = document.getElementById("clear-recent");
    clearBtn.addEventListener("click", () => {
        clearConversions();
        listContainer.innerHTML = "";
        const listItem = document.createElement("li");
        listItem.className = "list-group-item";
        listItem.textContent = "No recent conversions.";
        listContainer.appendChild(listItem);
    });
}