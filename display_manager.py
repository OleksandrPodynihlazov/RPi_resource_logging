import time
import os
import psutil
import socket
from RPLCD.i2c import CharLCD

# Налаштування LCD (змініть адресу I2C, якщо необхідно)
lcd = CharLCD(i2c_expander='PCF8574', address=0x3f, port=1, cols=16, rows=2, dotsize=8)


def is_program_running(program_name):
    """Перевіряє, чи виконується програма"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and program_name.lower() in proc.info['name'].lower():
            return True
    return False

def get_cpu_usage():
    """Отримати завантаження CPU у відсотках"""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Отримати використання RAM у відсотках"""
    return psutil.virtual_memory().percent

def get_disk_space():
    """Отримати вільне місце на SD-карті у відсотках"""
    disk = psutil.disk_usage('/')
    return disk.free / disk.total * 100

def is_connected():
    """Перевіряє наявність підключення до інтернету"""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

def display_message(line1, line2=""):
    """Вивести повідомлення на LCD"""
    lcd.clear()
    lcd.write_string(line1[:16])  # Обмеження в 16 символів
    if line2:
        lcd.crlf()
        lcd.write_string(line2[:16])

try:
    while True:
        # 1. Чи виконується певна програма
        program_name = "handlers.py"  # Змініть назву програми, якщо потрібно
        if is_program_running(program_name):
            display_message("Bot:","Running")
        else:
            display_message("Bot:", "Waiting")
        time.sleep(5)

        # 2. Навантаження на CPU та RAM
        cpu = get_cpu_usage()
        ram = get_memory_usage()
        display_message(f"CPU: {cpu:.1f}%", f"RAM: {ram:.1f}%")
        time.sleep(5)

        # 3. Вільне місце на SD-карті
        free_space = get_disk_space()
        display_message("SD free space:", f"{free_space:.1f}%")
        time.sleep(5)

        # 4. Стан підключення до інтернету
        if is_connected():
            display_message("Wi-Fi:", "Conn")
        else:
            display_message("Wifi:", "No")
        time.sleep(5)

except KeyboardInterrupt:
    print("Stop")
finally:
    lcd.clear()
