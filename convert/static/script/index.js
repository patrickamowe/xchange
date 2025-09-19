// main.js
import { UIHandler } from "./UI.js";
import { popularConversionHandler } from "./popularConversionHandler.js";
import { conversionHandler} from "./conversionHandler.js"


document.addEventListener("DOMContentLoaded", () => { 
    popularConversionHandler();
    conversionHandler();
    UIHandler();
});
