import flet as ft
import csv

def main(page: ft.Page):
    page.title = "แบบฟอร์มรับสมัคร"

    name_input = ft.TextField(label="ชื่อ-สกุล", width=300)
    phone_input = ft.TextField(label="หมายเลขโทรศัพท์", width=300)
    team_input = ft.TextField(label="ชื่อทีม", width=300)
    result_text = ft.Text(value="", color="green")

    def save_data(e):
        name = name_input.value.strip()
        phone = phone_input.value.strip()
        team = team_input.value.strip()
        if name and phone and team:
            with open("register.csv", "a", newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([name, phone, team])
            result_text.value = "บันทึกข้อมูลเรียบร้อยแล้ว!"
            name_input.value = ""
            phone_input.value = ""
            team_input.value = ""
        else:
            result_text.value = "กรุณากรอกข้อมูลให้ครบถ้วน"
        page.update()

    save_btn = ft.ElevatedButton(text="บันทึกข้อมูล", on_click=save_data)

    page.add(name_input, phone_input, team_input, save_btn, result_text)

ft.app(main)
