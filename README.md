# 📊 Sorting Algorithm Visualization

A small Python desktop application that generates integer arrays and compares sorting algorithms visually and by execution time. It was developed as part of my bachelor thesis.

The interface is built with `tkinter` and the step-by-step charts with `matplotlib`.

---

## 🎓 Bachelor thesis

- 📄 [Thesis (PDF)](Thesis.pdf)
- 🖥️ [Presentation (PDF)](Presentation.pdf)

---

## ✨ Features

- Generate integer arrays with a chosen size, minimum and maximum value, and an option to allow or block duplicates
- Choose the input case: **Best**, **Average** or **Worst**
- Compare these sorting algorithms:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort
  - Counting Sort
  - Radix Sort
  - Bucket Sort
  - Shell Sort
- See each algorithm step by step in a bar chart
- Measure and show the execution time in milliseconds

---

## 🛠️ Requirements

- Python 3.8 or newer
- `tkinter` (included with most Python installations)
- `matplotlib`

Install `matplotlib` with:

```bash
pip install matplotlib
```

> On some Linux systems `tkinter` must be installed separately (for example the package `python3-tk`).

---

## 🚀 How to run it

1. Download or clone the repository.
2. Install `matplotlib` (see above).
3. Run the program:

```bash
python sort-visualizer.py
```

### Controls

- **Array Size:** number of integers (1 to 500)
- **Min Value / Max Value:** range of the numbers (min must be smaller than max)
- **Allow Duplicates:** when unchecked, all values are unique
- **Select Case:** Best (sorted ascending), Average (random) or Worst (sorted descending)
- **Execute:** runs all algorithms and records their time and steps
- **Show Graphs:** opens the visualization, where you can choose an algorithm and move through its steps with the Start, Previous, Next and Finish buttons

---

## 📝 Notes

- Each algorithm saves its intermediate steps in a list, so the graphs can show how the sorting progresses.
- Time is measured in milliseconds with `time.time()`.
- Radix Sort handles negative numbers by sorting them separately from the positive ones.
- Invalid settings are blocked (size out of range, min not smaller than max, not enough unique values).

---

## 📁 Project files

```
sort-visualizer.py   The application (interface, algorithms, graphs)
Thesis.pdf           The bachelor thesis
Presentation.pdf     The thesis presentation
LICENSE              License
```

---

## 🗺️ Known limitations

- Very large arrays (close to 500) create many steps and can be slow to draw.
- Step navigation is basic, with no smooth animation.
- There are no automated tests yet.

---

## 📄 License

The code is available under the MIT License. See the `LICENSE` file.

---

## 👤 Author

Georgios Vanasas
