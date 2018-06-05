from Tkinter import *
import ttk
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

#############################
#  Written by Jake Piccini  #
#          v1.0.0           #
#############################

channel = "PyChat/Default/"


# Make Subscription #
def on_connect(client, userdata, flags, rc):
    set_room()


# Receive Function #
def on_message(client, userdata, msg):
    Message, Name, Color = str(msg.payload).split('#!?#@@!')
    print_message(Name + ': ' + Message, colorDic[Color])


# Send Function #    
def send(e=None):
    if name.get() and message.get():
        msg = message.get() + '#!?#@@!' + name.get() + '#!?#@@!' + color.get()
        try:
            a, b, c = msg.split('#!?#@@!')
            publish.single(current_room.get(), msg, hostname="test.mosquitto.org")
            message.set('')
        except ValueError:
            print_message("Please remove '#!?#@@!' from your name or message.", "darkgrey")
    elif not name.get():
        print_message("Please enter a name.", "darkgrey")
    elif not message.get():
        print_message("Please enter a message.", "darkgrey")


# Print Message to Window #
def print_message(message, color):
    mWindow.insert('end', message)
    num = mWindow.size() - 1
    mWindow.itemconfig(num, foreground=color)
    mWindow.see(END)


# Change Chat Room #
def set_room():
    client.unsubscribe(current_room.get())
    current_room.set(channel + room.get())
    client.subscribe(current_room.get())
    print_message("You have joined the chat room '%s'" % (room.get()), "darkgrey")
    app.title("PyChat - Room: %s" % (room.get()))


# Start Mosquito #
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_start()

# Window #
app = Tk()
window = ttk.Frame(app, padding="10 5 10 8")
Grid.rowconfigure(app, 0, weight=1)
Grid.columnconfigure(app, 0, weight=1)
window.grid(column=0, row=0, sticky=(N, W, E, S))
grid = ttk.Frame(window)
grid.grid(column=1, row=1, columnspan=4, sticky=(N, W, E, S))
Grid.rowconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 1, weight=1)

# Chat Room Select #
room = StringVar()
room.set("default")
current_room = StringVar()
current_room.set(channel + room.get())
ttk.Label(window, text="Room:").grid(column=1, row=1, sticky=W)
room_entry = ttk.Entry(window, textvariable=room)
room_entry.grid(column=2, row=1, columnspan=3, sticky=(W, E))
roomButt = ttk.Button(window, text="Set Room", command=set_room)
roomButt.grid(column=4, row=1, sticky=(W, E))

# Message Window #
mWindow = Listbox(window, height=10, width=30)
mWindow.grid(column=1, row=2, columnspan=4, pady=5, sticky=(N, S, W, E))
scroll = ttk.Scrollbar(window, orient=VERTICAL, command=mWindow.yview)
scroll.grid(column=5, row=2, pady=5, sticky=(N, S, W))
mWindow['yscrollcommand'] = scroll.set

# Message Entry #
message = StringVar()
message_entry = ttk.Entry(window, textvariable=message)
message_entry.grid(column=1, row=3, columnspan=3, sticky=(W, E))
sendButt = ttk.Button(window, text="Send", command=send)
sendButt.grid(column=4, row=3, sticky=(W, E))

app.bind("<Return>", send)

ttk.Separator(window, orient=HORIZONTAL).grid(column=1, row=4, columnspan=5, pady=10, sticky=(W, E))

# Name Entry #
name = StringVar()
ttk.Label(window, text="Name:").grid(column=1, row=5, sticky=(E))
name_entry = ttk.Entry(window, width=13, textvariable=name)
name_entry.grid(column=2, row=5, sticky=(W, E))

# Color Selection #
colorvar = StringVar()
ttk.Label(window, text="Color:").grid(column=3, row=5, sticky=(E))
color = ttk.Combobox(window, width=7, textvariable=colorvar, state='readonly')
color['values'] = ('Black', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Brown')
color.grid(column=4, row=5, sticky=(W))
color.set("Black")
colorDic = {'Black': 'black', 'Red': 'crimson', 'Orange': 'darkorange', 'Yellow': 'gold', 'Green': 'olivedrab',
            'Blue': 'mediumblue', 'Purple': 'darkmagenta', 'Brown': 'saddlebrown'}


# Menu Commands #
def about():
    AboutMe = Toplevel(app)
    AboutMe.title('About')
    AboutMe.resizable(width=FALSE, height=FALSE)

    aboutWindow = Listbox(AboutMe, height=6, width=45)
    aboutWindow.grid(column=1, row=1)
    aboutText = ['PyChat Version 1.0', 'Developed by Jake Piccini', 'j.piccini@icloud.com', '',
                 'Current Room: %s' % (room.get())]

    for line in aboutText:
        aboutWindow.insert('end', line)


def readme():
    ReadMe = Toplevel(app)
    ReadMe.title('README')
    ReadMe.resizable(width=FALSE, height=FALSE)

    readWindow = Listbox(ReadMe, height=30, width=130)
    readWindow.grid(column=1, row=1)
    scroll2 = ttk.Scrollbar(ReadMe, orient=VERTICAL, command=readWindow.yview)
    scroll2.grid(column=2, row=1, sticky=(N, S, W))
    readWindow['yscrollcommand'] = scroll2.set

    f = open('README.md')
    for line in f:
        readWindow.insert('end', line.strip('\n'))


# Create Menu #
menubar = Menu(app)

filemenu = Menu(menubar)
filemenu.add_command(label='Open README', command=readme)
filemenu.add_command(label='About', command=about)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=app.destroy)
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label='Open README', command=readme)
menubar.add_cascade(label='Help', menu=helpmenu)

app.config(menu=menubar)

# Resize Window #
app.minsize(width=400, height=290)
app.maxsize(width=700, height=500)

for x in range(3, 4):
    Grid.columnconfigure(window, x, weight=1)

for y in range(1, 2):
    Grid.rowconfigure(window, y, weight=1)

# App Loop #
app.mainloop()
