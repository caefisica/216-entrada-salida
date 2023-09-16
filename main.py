import flet as ft
import datetime

minute_format = lambda m: m if len(str(m))!=1 else '0'+str(m)
time_format = lambda x: f'{x.hour}:{minute_format(x.minute)}'

def main(page:ft.Page):
    entry = ft.Ref[ft.ElevatedButton]()
    leave = ft.Ref[ft.ElevatedButton]()
    checkin = ft.Text('Entrada registrada')
    checkout = ft.Text('Salida registrada')
    today = datetime.datetime.now()

    def cmd_entry(e):
        entry_time = datetime.datetime.now()
        checkin.value = f'Entrada registrada a las {time_format(entry_time)}'
        page.controls.append(checkin)
        entry.current.disabled = True
        leave.current.disabled = False
        page.update()


    def cmd_leave(e):
        departure_time = datetime.datetime.now()
        checkout.value = f'Salida registrada a las {time_format(departure_time)}'
        page.controls.append(checkout)
        entry.current.disabled = False
        leave.current.disabled = True
        page.update()


    page.add(
        ft.Text('Registro de entrada y salida del salón 216'),
        ft.Text(f'Fecha de hoy {today.day}/{today.month}/{today.year}'),
        ft.ElevatedButton(ref=entry, text='Entrada', on_click=cmd_entry),
        ft.ElevatedButton(ref=leave, text='Salida', on_click=cmd_leave, disabled=True)
    )

ft.app(target=main)