// main.js
import { UIHandler } from "./UI.js";
import { popularConversionHandler } from "./popularConversionHandler.js";
import { hiddenNews } from "./news.js";
import { recentConversionHandler } from "./recentConversionHandler.js";


document.addEventListener("DOMContentLoaded", () => { 
    popularConversionHandler();
    UIHandler();
    recentConversionHandler();
    hiddenNews();
});
