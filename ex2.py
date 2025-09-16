import flet as ft
import math

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข Flet"

    display = ft.TextField(value="", text_align="right", width=300, read_only=True)
    equation = ""

    def on_button_click(e):
        nonlocal equation
        val = e.control.text
        if val == "C":
            equation = ""
        elif val == "=":
            try:
                expr = equation.replace("^", "**")
                while "√" in expr:
                    idx = expr.index("√")
                    if expr[idx+1] == "(":
                        count = 1
                        end = idx+2
                        while count > 0 and end < len(expr):
                            if expr[end] == "(":
                                count += 1
                            elif expr[end] == ")":
                                count -= 1
                            end += 1
                        expr = expr[:idx] + f"math.sqrt({expr[idx+2:end-1]})" + expr[end:]
                    else:
                        num = ""
                        i = idx+1
                        while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                            num += expr[i]
                            i += 1
                        expr = expr[:idx] + f"math.sqrt({num})" + expr[i:]
                equation = str(eval(expr))
            except Exception:
                equation = "Error"
        else:
            equation += val
        display.value = equation
        page.update()

    buttons = [
        ["1", "2", "3", "+"],
        ["4", "5", "6", "-"],
        ["7", "8", "9", "*"],
        ["C", "0", "=", "/"],
        ["√", "^", None, None]  # ใช้ None แทนช่องว่าง
    ]

    rows = []
    for row in buttons:
        btn_row = []
        for b in row:
            if b is not None:
                btn_row.append(
                    ft.ElevatedButton(text=b, width=65, height=65, on_click=on_button_click)
                )
            else:
                btn_row.append(ft.Container(width=65, height=65))  # ช่องว่าง
        rows.append(ft.Row(btn_row, alignment="center"))

    page.add(display)
    for r in rows:
        page.add(r)

ft.app(main)