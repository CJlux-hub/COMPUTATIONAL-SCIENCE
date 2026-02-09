# 🕰️ Computational Science: Pendulum Precision Analysis

### **Project Overview**
This project investigates the impact of floating-point precision on physics simulations, specifically comparing **Truncation** (cutting off decimals) vs. **Rounding** (rounding to the nearest digit).

While most standard tests use the *Area of a Circle* ($A = \pi r^2$), this project demonstrates a practical application in timekeeping physics by calculating the **Period of a Simple Pendulum**.

### **The Physics Formula**
The simulation calculates the time ($T$) it takes for a pendulum to complete one full swing based on the length of the string ($L$) and gravity ($g$).

$$T = 2\pi \sqrt{\frac{L}{g}}$$

* **$L$ (Length):** 67 meters (Modeled after the Foucault Pendulum in Paris)
* **$g$ (Gravity):** $9.80665 \text{ m/s}^2$
* **$\pi$ (Pi):** The variable tested at different precision levels.

---

### **1. The Data (Terminal Output)**
The simulation runs a precision test at 20, 40, 60, and 100 decimal places. As shown in the output below, the **Gap** column highlights the penalty for using Truncation instead of Rounding.

![Terminal Output Screenshot](terminal_output.png)
*(Note: At 40 decimal places, the gap is clearly visible. At 100 decimal places, the error converges to zero.)*

---

### **2. The Visualization (Graph)**
The project generates a logarithmic graph to visualize the Error Decay.

* **X-Axis:** Precision (Number of Decimals Used)
* **Y-Axis:** Time Error in Seconds (Logarithmic Scale)
* **Green Line (Rounding):** Consistently lower error (Better Accuracy).
* **Red Line (Truncation):** Consistently higher error (Worse Accuracy).

![Graph Visualization](graph_result.png)

---

### **Methodology**
We utilize Python's `decimal` module to bypass standard hardware floating-point limits (which usually stop at ~15 digits).

* **Step 1:** Define a "True Pi" with 100 digits of precision.
* **Step 2:** Create a "Truncated" version (Floor) and a "Rounded" version (Half-Up).
* **Step 3:** Calculate the Pendulum Period for both versions.
* **Step 4:** Compare the difference (The "Gap") against the True Pi.

