import tkinter as tk

class App:
    def __init__(self):
        
        self.master = tk.Tk()
        self.frames = []
        self.current_frame_index = 0
        self.master.geometry('500x500')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.btn_prev = tk.Button(
            self.master,
            text="<",
            command=self.prev_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background='yellow',
            activebackground='yellow',
        )
        self.btn_prev.grid(row=0, column=0, sticky="nsew")

        self.btn_next = tk.Button(
            self.master,
            text=">",
            command=self.next_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background='yellow',
            activebackground='yellow',
        )
        self.btn_next.grid(row=0, column=2, sticky="nsew")

        frame1 = tk.Frame(self.master, width=300, height=500,background='black')
        frame2 = tk.Frame(self.master, width=300, height=500,background='green')
        frame3 = tk.Frame(self.master, width=300, height=500,background='red')

        self.frames = [frame1, frame2, frame3]
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=1, sticky="nsew")

        self.master.mainloop()

    def next_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=1, sticky="nsew")

    def prev_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_index = (self.current_frame_index - 1) % len(self.frames)
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=1, sticky="nsew")


if __name__ == "__main__":
    App()



