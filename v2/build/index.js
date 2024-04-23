"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const menubar_1 = require("menubar");
const mb = (0, menubar_1.menubar)();
mb.on("ready", () => {
    console.log("app is ready");
    // your app code here
});
