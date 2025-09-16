// main.js
import { setupUIHandlers } from "./UI.js";
import { savedConversionHandler } from "./conversion.js";
import { setupPopularConversionHandlers } from "./popular-conversion.js";
import { hiddenNews } from "./news.js";

document.addEventListener("DOMContentLoaded", () => {
    
    savedConversionHandler();
    setupPopularConversionHandlers();
    setupUIHandlers();
    hiddenNews();
});
