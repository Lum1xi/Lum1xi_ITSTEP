import tkinter as tk

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(eval(f"{num1} {op} {num2}"))
    except:
        result.set("Помилка")

root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
result = tk.StringVar()
label_result = tk.Label(root, textvariable=result)

btn_add = tk.Button(root, text="+", command=lambda: calculate("+"))
btn_sub = tk.Button(root, text="-", command=lambda: calculate("-"))
btn_mul = tk.Button(root, text="*", command=lambda: calculate("*"))
btn_div = tk.Button(root, text="/", command=lambda: calculate("/"))

entry1.pack()
entry2.pack()
btn_add.pack()
btn_sub.pack()
btn_mul.pack()
btn_div.pack()
label_result.pack()

root.mainloop()
