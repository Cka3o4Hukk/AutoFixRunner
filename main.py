import ctypes
import pyautogui
import subprocess
import time

exe_path = r"C:\Users\Алексей\Downloads\EZ_FIX\EZ_FIX.exe"

BUTTON_X, BUTTON_Y = 919, 490

# Константы для флага движения мыши
MOUSEEVENTF_MOVE = 0x0001


def activate_mouse():
    # Эмулируем физическое движение мыши
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, -1, -1, 0, 0)


subprocess.Popen(exe_path)
print("Файл успешно запущен.")

# Даем системе время на загрузку программы
time.sleep(5)

# "Пробуждаем" курсор
activate_mouse()

# Перемещаем курсор на кнопку
pyautogui.moveTo(BUTTON_X, BUTTON_Y)
time.sleep(1)  # Небольшая задержка

# Выполняем клик
pyautogui.click(BUTTON_X, BUTTON_Y)
