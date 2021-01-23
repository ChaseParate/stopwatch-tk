import tkinter as tk
import tkinter.font as tk_font
from time import time


def format_time(t):
    minutes, seconds = map(int, divmod(t, 60))
    hours, minutes = map(int, divmod(minutes, 60))
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def stopwatch_update():
    def count(start_time):
        global stopwatch
        if running:
            loop_time = time() - start_time
            lbl_stopwatch['text'] = format_time(loop_time + stopwatch)
            start_time = time()
            stopwatch += loop_time
            lbl_stopwatch.after(100, count, start_time)

    count(time())


def start():
    print('Start')
    btn_start_stop['text'] = 'Stop'
    btn_start_stop['bg'] = 'red'

    global running
    running = True
    stopwatch_update()


def stop():
    print('Stop')
    btn_start_stop['text'] = 'Start'
    btn_start_stop['bg'] = 'lime'

    global running
    running = False


def reset():
    print('Reset')

    stop()
    global stopwatch
    stopwatch = 0
    lbl_stopwatch['text'] = format_time(stopwatch)


running = False
stopwatch = 0

window = tk.Tk()
window.resizable(False, False)
font = tk_font.Font(size=30)

# Stopwatch Label
lbl_stopwatch = tk.Label(
    text=format_time(stopwatch),
    font=font
)
lbl_stopwatch.pack()

# Buttons Frame
frm_buttons = tk.Frame(window)
frm_buttons.pack(
    padx=5,
    pady=(0, 5)
)

# Start/Stop Button
btn_start_stop = tk.Button(
    master=frm_buttons,
    text='Start',
    width=10,
    height=2,
    bg='lime',
    command=lambda: start() if btn_start_stop['text'] == 'Start' else stop()
)
btn_start_stop.pack(side=tk.LEFT)

# Reset Button
btn_reset = tk.Button(
    master=frm_buttons,
    text='Reset',
    width=10,
    height=2,
    bg='lightgray',
    command=reset
)
btn_reset.pack(side=tk.LEFT)

window.mainloop()
