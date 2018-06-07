from Tkinter import *
import ttk
import tkFont
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt


#############################
#  Written by Jake Piccini  #
#          v1.1.0           #
#############################

class PyChat:
    def __init__(self):
        # Window #
        self.app = Tk()
        self.window = ttk.Frame(self.app, padding="10 5 10 8")
        Grid.rowconfigure(self.app, 0, weight=1)
        Grid.columnconfigure(self.app, 0, weight=1)
        self.window.grid(column=0, row=0, sticky=(N, W, E, S))
        self.grid = ttk.Frame(self.window)
        self.grid.grid(column=1, row=1, columnspan=4, sticky=(N, W, E, S))
        Grid.rowconfigure(self.window, 1, weight=1)
        Grid.columnconfigure(self.window, 1, weight=1)

        # Room Variables #
        self.channel = "PyChat/Default/"
        self.room = StringVar()
        self.room.set("default")
        self.current_room = StringVar()
        self.current_room.set(self.channel + self.room.get())
        self.app.title("PyChat - Room: %s" % (self.room.get()))

        # Start Mosquito #
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("test.mosquitto.org", 1883, 60)
        self.client.loop_start()

        # Chat Room Entry #
        ttk.Label(self.window, text="Room:").grid(column=1, row=1, sticky=E)
        self.room_entry = ttk.Entry(self.window, textvariable=self.room)
        self.room_entry.grid(column=2, row=1, columnspan=3, sticky=(W, E))
        self.room_entry.bind("<Return>", self.set_room)
        self.roomButt = ttk.Button(self.window, text="Set Room", command=self.set_room)
        self.roomButt.grid(column=4, row=1, columnspan=2, sticky=(W, E))

        # Message Window #
        self.mWindow = Listbox(self.window, height=10, width=30)
        self.mWindow.grid(column=1, row=2, columnspan=4, pady=5, sticky=(N, S, W, E))
        self.scroll = ttk.Scrollbar(self.window, orient=VERTICAL, command=self.mWindow.yview)
        self.scroll.grid(column=5, row=2, pady=5, sticky=(N, S, W))
        self.mWindow['yscrollcommand'] = self.scroll.set

        # Message Entry #
        self.message = StringVar()
        self.message_entry = ttk.Entry(self.window, textvariable=self.message)
        self.message_entry.grid(column=1, row=3, columnspan=3, sticky=(W, E))
        self.message_entry.bind("<Return>", self.send)
        self.sendButt = ttk.Button(self.window, text="Send", command=self.send)
        self.sendButt.grid(column=4, row=3, columnspan=2, sticky=(W, E))
        ttk.Separator(self.window, orient=HORIZONTAL).grid(column=1, row=4, columnspan=5, pady=10, sticky=(W, E))

        # Name Entry #
        self.name = StringVar()
        ttk.Label(self.window, text="Name:", width=5).grid(column=1, row=5, sticky=E)
        self.name_entry = ttk.Entry(self.window, textvariable=self.name)
        self.name_entry.grid(column=2, row=5, sticky=(W, E))

        # Color Selection #
        self.colorvar = StringVar()
        ttk.Label(self.window, text="Color:").grid(column=3, row=5, sticky=E)
        self.color = ttk.Combobox(self.window, width=7, textvariable=self.colorvar, state='readonly')
        self.color['values'] = ('Black', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Brown')
        self.color.grid(column=4, row=5, sticky=(W, E))
        self.color.set("Black")
        self.colorDic = {'Black': 'black', 'Red': 'crimson', 'Orange': 'darkorange', 'Yellow': 'gold',
                         'Green': 'olivedrab', 'Blue': 'mediumblue', 'Purple': 'darkmagenta', 'Brown': 'saddlebrown'}

        # Create Menu #
        self.menu_bar = Menu(self.app)

        self.file_menu = Menu(self.menu_bar)
        self.file_menu.add_command(label='Open README', command=self.readme)
        self.file_menu.add_command(label='About', command=self.about)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Quit', command=self.app.destroy)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        self.helpmenu = Menu(self.menu_bar)
        self.helpmenu.add_command(label='Open README', command=self.readme)
        self.menu_bar.add_cascade(label='Help', menu=self.helpmenu)

        self.app.config(menu=self.menu_bar)

        # Resize Window #
        self.app.minsize(width=400, height=300)
        self.app.maxsize(width=700, height=500)

        for x in range(1, 5):
            Grid.columnconfigure(self.window, x, weight=1)

        for y in range(2, 3):
            Grid.rowconfigure(self.window, y, weight=1)

        # App Loop #
        self.app.mainloop()


    # Make Subscription #
    def on_connect(self, client, userdata, flags, rc):
        self.set_room()

    # Receive Function #
    def on_message(self, client, userdata, msg):
        Message, Name, Color = str(msg.payload).split('#!?#@@!')
        self.print_message(Name + ': ' + Message, self.colorDic[Color])

    # Send Function #
    def send(self, binding_event=None):
        if self.name.get() and self.message.get():
            msg = self.message.get() + '#!?#@@!' + self.name.get() + '#!?#@@!' + self.color.get()
            try:
                a, b, c = msg.split('#!?#@@!')
                publish.single(self.current_room.get(), msg, hostname="test.mosquitto.org")
                self.message.set('')
            except ValueError:
                self.print_message("Please remove '#!?#@@!' from your name or message.", "darkgrey")
        elif not self.name.get():
            self.print_message("Please enter a name.", "darkgrey")
        elif not self.message.get():
            self.print_message("Please enter a message.", "darkgrey")

    # Print Message to Window #
    def print_message(self, message, color):
        self.mWindow.insert('end', message)
        num = self.mWindow.size() - 1
        self.mWindow.itemconfig(num, foreground=color)
        self.mWindow.see(END)

    # Change Chat Room #
    def set_room(self, binding_event=None):
        if not self.room.get():
            self.room.set("default")
        self.client.unsubscribe(self.current_room.get())
        self.current_room.set(self.channel + self.room.get())
        self.client.subscribe(self.current_room.get())
        self.print_message("You have joined the chat room '%s'" % (self.room.get()), "darkgrey")
        self.app.title("PyChat - Room: %s" % (self.room.get()))

    # Menu Commands #
    def about(self):
        about_me = Toplevel(self.app)
        about_me.title('About')
        about_me.resizable(width=FALSE, height=FALSE)

        content_window = Listbox(about_me, height=6, width=45)
        content_window.grid(column=1, row=1)
        about_text = ['PyChat Version 1.0.0', 'Developed by Jake Piccini', '',
                     'Current Channel: %s' % self.channel,
                     'Current Room: %s' % self.room.get()]

        for line in about_text:
            content_window.insert('end', line)

    def readme(self):
        read_me = Toplevel(self.app)
        read_me.title('README')
        read_me.resizable(width=FALSE, height=FALSE)

        content_frame = Listbox(read_me, height=30, width=130, font=tkFont.Font(font="Courier"))
        content_frame.grid(column=1, row=1)
        scroll2 = ttk.Scrollbar(read_me, orient=VERTICAL, command=content_frame.yview)
        scroll2.grid(column=2, row=1, sticky=(N, S, W))
        content_frame['yscrollcommand'] = scroll2.set

        f = open('README.md')
        for line in f:
            content_frame.insert('end', line.strip('\n'))


if __name__ == "__main__":
    app = PyChat()
