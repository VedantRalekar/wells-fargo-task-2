import tkinter as tk
import random
import time

# ------------------------------
# Sorting Algorithms
# ------------------------------

def bubble_sort(data, drawData, speed):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
                time.sleep(speed)
    drawData(data, ['green' for _ in range(len(data))])

def selection_sort(data, drawData, speed):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            drawData(data, ['red' if x == j or x == min_idx else 'blue' for x in range(len(data))])
            time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
    drawData(data, ['green' for _ in range(len(data))])

def insertion_sort(data, drawData, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
            time.sleep(speed)
        data[j + 1] = key
    drawData(data, ['green' for _ in range(len(data))])

def merge_sort(data, drawData, speed):
    merge_sort_rec(data, 0, len(data) - 1, drawData, speed)
    drawData(data, ['green' for _ in range(len(data))])

def merge_sort_rec(data, left, right, drawData, speed):
    if left < right:
        mid = (left + right) // 2
        merge_sort_rec(data, left, mid, drawData, speed)
        merge_sort_rec(data, mid + 1, right, drawData, speed)
        merge(data, left, mid, right, drawData, speed)

def merge(data, left, mid, right, drawData, speed):
    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1
        k += 1
        drawData(data, ['red' if x == k else 'blue' for x in range(len(data))])
        time.sleep(speed)

    while i < len(left_part):
        data[k] = left_part[i]
        i += 1
        k += 1
        drawData(data, ['red' if x == k else 'blue' for x in range(len(data))])
        time.sleep(speed)

    while j < len(right_part):
        data[k] = right_part[j]
        j += 1
        k += 1
        drawData(data, ['red' if x == k else 'blue' for x in range(len(data))])
        time.sleep(speed)

def quick_sort(data, head, tail, drawData, speed):
    if head < tail:
        partition_idx = partition(data, head, tail, drawData, speed)
        quick_sort(data, head, partition_idx - 1, drawData, speed)
        quick_sort(data, partition_idx + 1, tail, drawData, speed)

def partition(data, head, tail, drawData, speed):
    border = head
    pivot = data[tail]

    drawData(data, ['yellow' if x == tail else 'red' if x == border else 'blue' for x in range(len(data))])
    time.sleep(speed)

    for j in range(head, tail):
        if data[j] < pivot:
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, ['yellow' if x == tail else 'red' if x == border or x == j else 'blue' for x in range(len(data))])
        time.sleep(speed)

    data[border], data[tail] = data[tail], data[border]
    return border

# ------------------------------
# GUI Functions
# ------------------------------

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 5
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]), font=("Helvetica", 8), fill="black")
    root.update_idletasks()

def generate():
    global data
    data = [random.randint(10, 100) for _ in range(20)]
    drawData(data, ['blue' for _ in range(len(data))])

def start_algorithm():
    global data
    if alg_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())
    elif alg_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, speedScale.get())
    elif alg_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())
    elif alg_menu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    elif alg_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())
        drawData(data, ['green' for _ in range(len(data))])

# ------------------------------
# GUI Setup
# ------------------------------

root = tk.Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='black')

algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort']
alg_menu = tk.StringVar()
alg_menu.set(algorithms[0])

UI_frame = tk.Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = tk.Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

tk.Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tk.OptionMenu(UI_frame, alg_menu, *algorithms).grid(row=0, column=1, padx=5, pady=5)

speedScale = tk.Scale(UI_frame, from_=0.01, to=1.0, length=200, digits=3,
                      resolution=0.01, orient=tk.HORIZONTAL, label="Select Speed")
speedScale.grid(row=0, column=2, padx=5, pady=5)
speedScale.set(0.2)

tk.Button(UI_frame, text="Generate Array", command=generate, bg='lightblue').grid(row=0, column=3, padx=5, pady=5)
tk.Button(UI_frame, text="Start", command=start_algorithm, bg='green').grid(row=0, column=4, padx=5, pady=5)

root.mainloop()
