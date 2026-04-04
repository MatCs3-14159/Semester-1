document.addEventListener("DOMContentLoaded", () => {
    /* =========================
       DERIVIX – SCIENTIFIC CALCULATOR
       ORIGINAL STRUCTURE + FIXES
    ========================= */

    // --------- Variables ----------
    const display = document.querySelector(".calc-input");
    const buttons = document.querySelectorAll(".btn");
    const historyList = document.getElementById("history-list");
    const modeDisplay = document.querySelector(".calc-mode");

    // ---------- State ----------
    let expression = "";
    let angleMode = "DEG";

    // ------ Angle Conversion ------
    function toRadians(x) {
        return angleMode === "DEG" ? (x * Math.PI) / 180 : x;
    }
    function fromRadians(x) {
        return angleMode === "DEG" ? (x * 180) / Math.PI : x;
    }

    /* 🔑 IMPORTANT
       Make helper functions visible to eval safely
    */
    window.toRadians = toRadians;
    window.fromRadians = fromRadians;

    // ------ History ------
    function addToHistory(expr, result) {
        if (!historyList) return;
        const li = document.createElement("li");
        li.textContent = `${expr} = ${result}`;
        historyList.prepend(li);
    }

    // ------ Normalize operators ------
    function normalizeExpression(expr) {
        return expr
            .replace(/×/g, "*")
            .replace(/÷/g, "/")
            .replace(/−/g, "-");
    }

    // ---------- Math Helpers ----------
    function gcd(a, b) {
        a = Math.abs(a); b = Math.abs(b);
        while (b) [a, b] = [b, a % b];
        return a;
    }

    function toFraction(decimal) {
        if (Number.isInteger(decimal)) return decimal.toString();
        const len = decimal.toString().split(".")[1].length;
        const denom = 10 ** len;
        const num = decimal * denom;
        const common = gcd(num, denom);
        return `${num / common}/${denom / common}`;
    }

    function toMixedFraction(frac) {
        const [n, d] = frac.split("/").map(Number);
        const whole = Math.floor(n / d);
        const rem = n % d;
        return rem === 0 ? `${whole}` : `${whole} ${rem}/${d}`;
    }

    // ---------- Statistics ----------
    function parseList(expr) {
        return expr.split(",").map(Number).filter(n => !isNaN(n));
    }

    function sum(v) { return v.reduce((a, b) => a + b, 0); }
    function mean(v) { return v.length ? sum(v) / v.length : 0; }
    function variance(v) {
        if (!v.length) return 0;
        const m = mean(v);
        return sum(v.map(x => (x - m) ** 2)) / v.length;
    }
    function stdDev(v) { return Math.sqrt(variance(v)); }

    // ---------- Advanced ----------
    function factorial(n) {
        n = Number(n);
        if (!Number.isInteger(n) || n < 0) return NaN;
        return n <= 1 ? 1 : n * factorial(n - 1);
    }

    function nPr(n, r) {
        return factorial(n) / factorial(n - r);
    }

    function nCr(n, r) {
        return factorial(n) / (factorial(r) * factorial(n - r));
    }

    // ---------- Handle Functions ----------
    function handleFunction(func) {
        switch (func) {

            case "DEG":
            case "RAD":
                angleMode = func;
                modeDisplay.textContent = angleMode;
                return;

            case "C":
                expression = "";
                display.value = "";
                return;

            case "±": {
                const m = expression.match(/(-?\d+\.?\d*)(?!.*\d)/);
                if (!m) return;
                const num = m[0];
                const toggled = num.startsWith("-") ? num.slice(1) : "-" + num;
                expression = expression.slice(0, -num.length) + toggled;
                display.value = expression;
                return;
            }

            case "%":
                expression = `(${expression})/100`;
                display.value = expression;
                return;

            case "π":
                expression += Math.PI;
                display.value = expression;
                return;

            case "e":
                expression += Math.E;
                display.value = expression;
                return;

            case "x²":
                expression = `(${expression})**2`;
                display.value = expression;
                return;

            case "x³":
                expression = `(${expression})**3`;
                display.value = expression;
                return;

            case "xʸ":
                expression += "**";
                display.value = expression;
                return;

            case "√":
                expression = `Math.sqrt(${expression})`;
                display.value = expression;
                return;

            case "∛":
                expression = `Math.cbrt(${expression})`;
                display.value = expression;
                return;

            case "log":
                expression = `Math.log10(${expression})`;
                display.value = expression;
                return;

            case "ln":
                expression = `Math.log(${expression})`;
                display.value = expression;
                return;

            case "eˣ":
                expression = `Math.exp(${expression})`;
                display.value = expression;
                return;

            case "10ˣ":
                expression = `10**(${expression})`;
                display.value = expression;
                return;

            case "sin":
                expression = `Math.sin(toRadians(${expression}))`;
                display.value = expression;
                return;

            case "cos":
                expression = `Math.cos(toRadians(${expression}))`;
                display.value = expression;
                return;

            case "tan":
                expression = `Math.tan(toRadians(${expression}))`;
                display.value = expression;
                return;

            case "sin⁻¹":
                expression = `fromRadians(Math.asin(${expression}))`;
                display.value = expression;
                return;

            case "cos⁻¹":
                expression = `fromRadians(Math.acos(${expression}))`;
                display.value = expression;
                return;

            case "tan⁻¹":
                expression = `fromRadians(Math.atan(${expression}))`;
                display.value = expression;
                return;

            case "!": {
                const m = expression.match(/(\d+)(?!.*\d)/);
                if (!m) return;
                expression = expression.slice(0, -m[0].length) + factorial(m[0]);
                display.value = expression;
                return;
            }

            case "nPr":
                expression = expression.replace(/(\d+),(\d+)/, (_, n, r) => nPr(n, r));
                display.value = expression;
                return;

            case "nCr":
                expression = expression.replace(/(\d+),(\d+)/, (_, n, r) => nCr(n, r));
                display.value = expression;
                return;

            case "|x|": {
                const m = expression.match(/(-?\d+\.?\d*)(?!.*\d)/);
                if (!m) return;
                expression = expression.slice(0, -m[0].length) + Math.abs(m[0]);
                display.value = expression;
                return;
            }

            case "Σx":
                expression = sum(parseList(expression));
                display.value = expression;
                return;

            case "Mean":
                expression = mean(parseList(expression));
                display.value = expression;
                return;

            case "Variance":
                expression = variance(parseList(expression));
                display.value = expression;
                return;

            case "Std Dev":
                expression = stdDev(parseList(expression));
                display.value = expression;
                return;
        }
    }

    // ---------- Calculate ----------
    function calculateResult() {
        try {
            const normalized = normalizeExpression(expression);
            const result = Function(`"use strict"; return (${normalized})`)();

            if (!isFinite(result)) throw new Error();

            addToHistory(expression, result);
            expression = result.toString();
            display.value = expression;
        } catch {
            display.value = "Error";
            expression = "";
        }
    }

    // ---------- Buttons ----------
    buttons.forEach(btn => {
            btn.addEventListener("click", () => {

                const value = btn.textContent.trim();

                // NUMBERS & OPERATORS
                if (btn.classList.contains("num") || btn.classList.contains("op")) {
                    if (!canInsert(value)) return;
                    saveState();
                    insertAtCursor(value);
                }

                // CLEAR (C)
                else if (btn.classList.contains("danger")) {
                    saveState();
                    expression = "";
                    display.value = "";
                }

                // BACKSPACE (⌫)
                else if (btn.classList.contains("delete")) {
                    saveState();
                    deleteAtCursor();
                }

                // EQUAL (=)
                else if (btn.classList.contains("equal")) {
                    calculateResult();
                }

                // FUNCTIONS (sin, cos, log, π, etc.)
                else if (btn.classList.contains("func")) {
                    handleFunction(value);
                }

                });
            });

    document.addEventListener("keydown", e => {

        // Undo / Redo
        if (e.ctrlKey && e.key === "z") return undo();
        if (e.ctrlKey && e.key === "y") return redo();

        // Backspace
        if (e.key === "Backspace") {
            e.preventDefault();
            deleteAtCursor();
            return;
        }

        // Enter
        if (e.key === "Enter") {
            e.preventDefault();
            calculateResult();
            return;
        }

        // Numbers
        if (!isNaN(e.key)) {
            if (!canInsert(e.key)) return;
            saveState();
            insertAtCursor(e.key);
            highlightButton(e.key);
        }

        // Operators
        const opMap = { "+": "+", "-": "−", "*": "×", "/": "÷" };
        if (opMap[e.key]) {
            if (!canInsert(opMap[e.key])) return;
            saveState();
            insertAtCursor(opMap[e.key]);
            highlightButton(opMap[e.key]);
        }

        // Decimal
        if (e.key === ".") {
            if (!canInsert(".")) return;
            saveState();
            insertAtCursor(".");
            highlightButton(".");
        }
    });

    function insertAtCursor(text) {
        const start = display.selectionStart;
        const end = display.selectionEnd;

        expression =
            expression.slice(0, start) +
            text +
            expression.slice(end);

        display.value = expression;
        display.selectionStart = display.selectionEnd = start + text.length;
    }

    function deleteAtCursor() {
        const start = display.selectionStart;
        const end = display.selectionEnd;

        if (start === end && start > 0) {
            expression =
                expression.slice(0, start - 1) +
                expression.slice(end);
            display.selectionStart = display.selectionEnd = start - 1;
        } else {
            expression =
                expression.slice(0, start) +
                expression.slice(end);
            display.selectionStart = display.selectionEnd = start;
        }
        display.value = expression;
    }

    function highlightButton(text) {
        buttons.forEach(btn => {
            if (btn.textContent.trim() === text) {
                btn.classList.add("active-key");
                setTimeout(() => btn.classList.remove("active-key"), 150);
            }
        });
    }
    function canInsert(char) {
        if (!expression) return !"+×÷−".includes(char);

        const last = expression.slice(-1);

        if ("+×÷−".includes(last) && "+×÷−".includes(char)) {
            return false;
        }

        if (char === "." && last === ".") {
            return false;
        }

        return true;
    }

    let undoStack = [];
    let redoStack = [];

    function saveState() {
        undoStack.push(expression);
        if (undoStack.length > 50) undoStack.shift();
        redoStack = [];
    }

    function undo() {
        if (!undoStack.length) return;
        redoStack.push(expression);
        expression = undoStack.pop();
        display.value = expression;
    }

    function redo() {
        if (!redoStack.length) return;
        undoStack.push(expression);
        expression = redoStack.pop();
        display.value = expression;
    }


});
