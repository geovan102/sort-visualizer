import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def record(steps, arr):
    if steps is None:
        return
    if not steps or steps[-1] != arr:
        steps.append(arr[:])

def bubble_sort(arr, steps):
    record(steps, arr)
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                record(steps, arr)
    record(steps, arr)
    return arr

def selection_sort(arr, steps):
    record(steps, arr)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            record(steps, arr)
    record(steps, arr)
    return arr

def insertion_sort(arr, steps):
    record(steps, arr)
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            record(steps, arr)
        arr[j + 1] = key
        record(steps, arr)
    record(steps, arr)
    return arr

def merge_sort(arr, steps):
    record(steps, arr)

    def merge(a, left_idx, mid_idx, right_idx):
        left = a[left_idx:mid_idx + 1]
        right = a[mid_idx + 1:right_idx + 1]
        i = j = 0
        k = left_idx
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]; i += 1
            else:
                a[k] = right[j]; j += 1
            k += 1
            record(steps, a)
        while i < len(left):
            a[k] = left[i]; i += 1; k += 1
            record(steps, a)
        while j < len(right):
            a[k] = right[j]; j += 1; k += 1
            record(steps, a)

    def merge_sort_rec(a, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        merge_sort_rec(a, l, m)
        merge_sort_rec(a, m + 1, r)
        merge(a, l, m, r)

    merge_sort_rec(arr, 0, len(arr) - 1)
    record(steps, arr)
    return arr

def quick_sort(arr, steps):
    record(steps, arr)

    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    record(steps, a)
        if i + 1 != high:
            a[i + 1], a[high] = a[high], a[i + 1]
            record(steps, a)
        return i + 1

    def quick_rec(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_rec(a, low, pi - 1)
            quick_rec(a, pi + 1, high)

    quick_rec(arr, 0, len(arr) - 1)
    record(steps, arr)
    return arr

def heap_sort(arr, steps):
    record(steps, arr)

    def heapify(a, heap_size, root_idx):
        largest = root_idx
        l = 2 * root_idx + 1
        r = 2 * root_idx + 2
        if l < heap_size and a[l] > a[largest]:
            largest = l
        if r < heap_size and a[r] > a[largest]:
            largest = r
        if largest != root_idx:
            a[root_idx], a[largest] = a[largest], a[root_idx]
            record(steps, a)
            heapify(a, heap_size, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        record(steps, arr)
        heapify(arr, i, 0)

    record(steps, arr)
    return arr

def counting_sort(arr, steps):
    record(steps, arr)
    if not arr:
        record(steps, [])
        return arr

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
    count = [0] * k

    for num in arr:
        count[num - min_val] += 1

    index = 0
    for num in range(min_val, max_val + 1):
        while count[num - min_val] > 0:
            arr[index] = num
            record(steps, arr)
            index += 1
            count[num - min_val] -= 1
    record(steps, arr)
    return arr

def radix_sort(arr, steps):
    record(steps, arr)
    if not arr:
        record(steps, [])
        return arr

    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    def lsd_radix(a, record_callback=None):
        if not a:
            return a
        max_val = max(a)
        exp = 1
        while max_val // exp > 0:
            n = len(a)
            output = [0] * n
            count = [0] * 10
            for num in a:
                count[(num // exp) % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            for i in range(n - 1, -1, -1):
                idx = (a[i] // exp) % 10
                output[count[idx] - 1] = a[i]
                count[idx] -= 1
            a[:] = output
            if record_callback:
                record_callback(a[:])
            exp *= 10
        return a

    def rec_pos(p):
        record(steps, negatives + p)
    lsd_radix(positives, record_callback=rec_pos)

    if negatives:
        neg_abs = [-x for x in negatives]

        def rec_neg(nv):
            record(steps, [-x for x in reversed(nv)] + positives)
        lsd_radix(neg_abs, record_callback=rec_neg)
        negatives = [-x for x in reversed(neg_abs)]

    arr[:] = negatives + positives
    record(steps, arr)
    return arr

def bucket_sort(arr, steps):
    record(steps, arr)
    n = len(arr)
    if n <= 1:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    buckets = [[] for _ in range(min(10, n))]
    range_size = (max_val - min_val + 1) / len(buckets)

    for num in arr:
        idx = int((num - min_val) / range_size)
        if idx >= len(buckets):
            idx = len(buckets) - 1
        buckets[idx].append(num)

    pos = 0
    for b in buckets:
        b.sort()
        for x in b:
            arr[pos] = x
            record(steps, arr)
            pos += 1
    record(steps, arr)
    return arr

def shell_sort(arr, steps):
    record(steps, arr)
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                record(steps, arr)
            arr[j] = temp
            record(steps, arr)
        gap //= 2
    record(steps, arr)
    return arr

ALGORITHMS = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort,
    'Heap Sort': heap_sort,
    'Counting Sort': counting_sort,
    'Radix Sort': radix_sort,
    'Bucket Sort': bucket_sort,
    'Shell Sort': shell_sort,
}


class GUI:
    def __init__(self, parent):
        self.root = parent
        self.root.title("Integer Sorting Comparison")
        self.root.geometry("345x570")
        self.root.resizable(False, False)
        self.results = {}

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

        self.base_array = None
        self.algorithm_list = []
        self.current_algorithm_index = 0

        tk.Label(parent, text="Array Size:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.size_entry = tk.Entry(parent, width=10)
        self.size_entry.insert(0, "")
        self.size_entry.grid(row=0, column=1, sticky="w", padx=5, pady=2)

        tk.Label(parent, text="Min Value:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.min_entry = tk.Entry(parent, width=10)
        self.min_entry.insert(0, "")
        self.min_entry.grid(row=1, column=1, sticky="w", padx=5, pady=2)

        tk.Label(parent, text="Max Value:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.max_entry = tk.Entry(parent, width=10)
        self.max_entry.insert(0, "")
        self.max_entry.grid(row=2, column=1, sticky="w", padx=5, pady=2)

        self.duplicates_var = tk.BooleanVar(value=False)
        tk.Checkbutton(parent, text="Allow Duplicates", variable=self.duplicates_var).grid(row=3, column=0, columnspan=2, sticky="n", pady=2)

        tk.Label(parent, text="Select Case:").grid(row=4, column=0, sticky="e", padx=5, pady=2)
        self.case_var = tk.StringVar(value="average")
        tk.Radiobutton(parent, text="Best Case", variable=self.case_var, value="best").grid(row=4, column=1,sticky="w", padx=5, pady=2)
        tk.Radiobutton(parent, text="Average Case", variable=self.case_var, value="average").grid(row=5, column=1, sticky="w", padx=5, pady=2)
        tk.Radiobutton(parent, text="Worst Case", variable=self.case_var, value="worst").grid(row=6, column=1, sticky="w", padx=5, pady=2)

        btn_frame = tk.Frame(parent)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=6, sticky="n")

        tk.Button(btn_frame, text="Execute", command=self.run_sorting).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Show Graphs", command=self.show_graphs).pack(side="left", padx=4)

        self.results_text = tk.Text(parent, width=40, height=20)
        self.results_text.grid(row=8, column=0, columnspan=2, padx=5, pady=6, sticky="n")

        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def validate_input(self):
        try:
            size = int(self.size_entry.get())
            min_val = int(self.min_entry.get())
            max_val = int(self.max_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid integers")
            return False

        if size <= 0 or size > 500:
            messagebox.showerror("Error", "Size must be 1-500")
            return False

        if min_val >= max_val:
            messagebox.showerror("Error", "Min must be less than Max!")
            return False

        if not self.duplicates_var.get() and (max_val - min_val + 1) < size:
            messagebox.showerror("Error", "Need more unique values for requested size")
            return False

        return True

    def create_array(self):
        size = int(self.size_entry.get())
        min_val = int(self.min_entry.get())
        max_val = int(self.max_entry.get())
        case = self.case_var.get()

        if self.duplicates_var.get():
            arr = [random.randint(min_val, max_val) for _ in range(size)]
        else:
            vals = list(range(min_val, max_val + 1))
            random.shuffle(vals)
            arr = vals[:size]

        if case == "best":
            arr.sort()
        elif case == "worst":
            arr.sort(reverse=True)
        else:
            random.shuffle(arr)

        return arr

    def run_sorting(self):
        if not self.validate_input():
            return

        self.results_text.delete(1.0, tk.END)

        self.base_array = self.create_array()
        self.results = {}
        self.algorithm_list = list(ALGORITHMS.items())
        self.current_algorithm_index = 0

        self.run_next_algorithm()

    def run_next_algorithm(self):
        if self.current_algorithm_index >= len(self.algorithm_list):
            self.show_results()
            return

        name, func = self.algorithm_list[self.current_algorithm_index]
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Running: {name}...\n")
        self.results_text.see(tk.END)
        self.root.update_idletasks()

        arr_copy = self.base_array[:]
        steps = []
        start = time.time()

        try:
            func(arr_copy, steps)
            elapsed = (time.time() - start) * 1000.0
            if not steps:
                steps.append(arr_copy[:])
            self.results[name] = {'time': elapsed, 'steps': steps, 'sorted': arr_copy[:]}
        except Exception as e:
            self.results[name] = {'error': str(e)}

        self.current_algorithm_index += 1

        self.root.after(10, self.run_next_algorithm)

    def show_results(self):
        self.results_text.delete(1.0, tk.END)

        sorted_results = sorted(self.results.items(), key=lambda x: x[1].get('time', float('inf')))

        for name, info in sorted_results:
            if 'error' in info:
                self.results_text.insert(tk.END, f"{name}: ERROR -> {info['error']}\n\n")
            else:
                self.results_text.insert(tk.END, f"{name}: {info['time']:.3f} ms\n\n")

    def show_graphs(self):
        if not self.results:
            messagebox.showwarning("Warning", "Run algorithms first!")
            return
        Graph(self.root, self.results)


class Graph:
    def __init__(self, master, results):
        self.top = tk.Toplevel(master)
        self.top.title("Sorting Visualization")
        self.results = {k: v for k, v in results.items() if 'error' not in v}
        if not self.results:
            messagebox.showerror("Error", "No successful results")
            self.top.destroy()
            return
        self.algo_names = list(self.results.keys())
        self.current_algo = 0
        self.current_step = 0

        tk.Label(self.top, text="Algorithm:").pack(side="top", anchor="w")
        self.combo = ttk.Combobox(self.top, values=self.algo_names, state='readonly')
        self.combo.current(0)
        self.combo.pack(side="top", fill="x")
        self.combo.bind("<<ComboboxSelected>>", self.change_algo)

        btn_frame = tk.Frame(self.top)
        btn_frame.pack(side="top", pady=4)
        tk.Button(btn_frame, text="Start", command=self.first_step).pack(side="left", padx=7)
        tk.Button(btn_frame, text="Previous", command=self.prev_step).pack(side="left", padx=7)
        tk.Button(btn_frame, text="Next", command=self.next_step).pack(side="left", padx=7)
        tk.Button(btn_frame, text="Finish", command=self.last_step).pack(side="left", padx=7)

        self.canvas_frame = tk.Frame(self.top)
        self.canvas_frame.pack(fill="both", expand=True)
        self.draw_plot()

        self.center_window()

    def center_window(self):
        self.top.update_idletasks()
        window_width = self.top.winfo_width()
        window_height = self.top.winfo_height()
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.top.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def change_algo(self, _event=None):
        self.current_algo = self.combo.current()
        self.current_step = 0
        self.draw_plot()

    def first_step(self): self.current_step = 0; self.draw_plot()

    def get_step_jump(self):
        algo = self.algo_names[self.current_algo]
        total_steps = len(self.results[algo]['steps'])
        jump = max(1, total_steps // 10)
        return jump

    def next_step(self):
        algo = self.algo_names[self.current_algo]
        max_s = len(self.results[algo]['steps']) - 1
        jump = self.get_step_jump()
        if self.current_step < max_s:
            self.current_step = min(self.current_step + jump, max_s)
            self.draw_plot()

    def prev_step(self):
        jump = self.get_step_jump()
        if self.current_step > 0:
            self.current_step = max(self.current_step - jump, 0)
            self.draw_plot()

    def last_step(self):
        algo = self.algo_names[self.current_algo]
        self.current_step = len(self.results[algo]['steps']) - 1
        self.draw_plot()

    def draw_plot(self):
        for w in self.canvas_frame.winfo_children():
            w.destroy()

        algo = self.algo_names[self.current_algo]
        steps = self.results[algo]['steps']
        if not steps:
            return

        arr = steps[self.current_step]
        fig, ax = plt.subplots(figsize=(7, 4))
        x = range(len(arr))
        ax.bar(x, arr)
        ax.set_title(f"{algo} — Step {self.current_step + 1}/{len(steps)}")
        ax.set_xticks([])

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        plt.close(fig)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()