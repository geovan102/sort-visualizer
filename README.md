# Integer Sorting Comparison

A small Python GUI application that generates integer arrays and compares multiple sorting algorithms visually and by execution time. Built with `tkinter` for the interface and `matplotlib` for step-by-step visualizations.

---

## Features

* Generate integer arrays with configurable size, min/max values and duplicate control.
* Choose case: **Best**, **Average**, **Worst**.
* Compare the following sorting algorithms:

  * Bubble Sort
  * Selection Sort
  * Insertion Sort
  * Merge Sort
  * Quick Sort
  * Heap Sort
  * Counting Sort
  * Radix Sort
  * Bucket Sort
  * Shell Sort
* Visualize the sorting process step-by-step with bar charts.
* Measure and display elapsed time (in milliseconds) for each algorithm.

---

## Requirements

* Python 3.8+ (should work with Python 3.x)
* `tkinter` (usually included with standard Python installations)
* `matplotlib`

Install `matplotlib` with pip if you don't have it:

```bash
pip install matplotlib
```

> Note: On some Linux distributions you may need to install system packages for `tkinter` (for example `python3-tk`).

---

## Usage

1. Clone or download the repository.
2. Make sure dependencies are installed (`matplotlib`).
3. Run the application:

```bash
python main.py
```

### GUI controls

* **Array Size**: Number of integers (validated between 1 and 500).
* **Min Value / Max Value**: Range of generated integers. `Min` must be less than `Max`.
* **Allow Duplicates**: When unchecked, values are unique; when checked, random duplicates are allowed.
* **Select Case**: Choose `Best` (sorted ascending), `Average` (random), or `Worst` (sorted descending) input array.
* **Execute**: Runs all algorithms sequentially and records their execution time and the list of intermediate steps.
* **Show Graphs**: Opens a visualization window where you can pick an algorithm and step through its recorded states using `Start`, `Previous`, `Next`, and `Finish` buttons.

The results panel shows each algorithm and the measured time in milliseconds. The visualization uses a bar chart for the current step of the selected algorithm.

---

## Implementation notes

* Each sorting algorithm records intermediate steps into a `steps` list so that the GUI can visualize the algorithm progress.
* Timing is captured in milliseconds using `time.time()` before and after the sort.
* For algorithms that support negative numbers and mixes of signs (e.g., Radix Sort in this project), the implementation separates negatives from positives and combines them after sorting.
* Validation prevents invalid configurations (size out of range, `min >= max`, insufficient unique values when duplicates are disallowed).

---

## Project structure

```
README.md
main.py         # Main application (GUI + sorting algorithms + visualization)
```

---

## Known limitations & TODO

* Very large arrays (close to 500) may produce many visualization steps and become slow to render.
* The GUI uses a simple step-jump heuristic when navigating steps — making smooth animation controls would be a useful enhancement.
* Add unit tests for algorithm correctness and edge cases.
* Add command-line interface to run headless benchmarks without GUI.

---

## Contribution

Contributions are welcome. Please open an issue or submit a pull request with a brief description of the change.

---

## License

This project is provided under the MIT License. See `LICENSE` for details (or add an MIT license file).

---

## Contact

If you have questions or suggestions, open an issue or contact the repository owner.
