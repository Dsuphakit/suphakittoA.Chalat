import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข Flet"

    # ช่องแสดงผลลัพธ์
    display = ft.TextField(value="", text_align="right", width=300, read_only=True)

    # เก็บสมการ
    equation = ""

    # ฟังก์ชันเมื่อกดปุ่ม
    def on_button_click(e):
        nonlocal equation
        val = e.control.text
        if val == "C":
            equation = ""
        elif val == "=":
            try:
                equation = str(eval(equation))
            except Exception:
                equation = "Error"
        else:
            equation += val
        display.value = equation
        page.update()

    # สร้างปุ่มตัวเลขและเครื่องหมาย
    buttons = [
        ["1", "2", "3", "+"],
        ["4", "5", "6", "-"],
        ["7", "8", "9", "*"],
        ["C", "0", "=", "/"]
    ]

    rows = []
    for row in buttons:
        btn_row = []
        for b in row:
            btn_row.append(
                ft.ElevatedButton(text=b, width=65, height=65, on_click=on_button_click)
            )
        rows.append(ft.Row(btn_row, alignment="center"))

    # เพิ่ม element ลงในหน้า
    page.add(display)
    for r in rows:
        page.add(r)

ft.app(main)
