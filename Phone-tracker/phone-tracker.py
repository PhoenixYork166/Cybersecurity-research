from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
from PIL import Image, ImageTk
import pytz

root = Tk()
# App title
root.title('Phone Number Tracker')
# App resolutions
root.geometry('500x584+100+200')
root.resizable(False, False)

# Icon image
icon = PhotoImage(file='icon.png')
root.iconphoto(False, icon)

# Logo
logo = PhotoImage(file='phone-track.png')
Label(root,image=logo, width=100, height=100).place(x=20,y=30)

# Search bar
Eback = PhotoImage(file='search.png')
Label(root,image=Eback).place(x=130,y=30)

# Heading
Heading = Label(root, text='Track Number', font=('arial', 16, 'bold'))
Heading.place(x=330, y=50)

# Bottom
Box = PhotoImage(file='bottom.png')
Label(root, image=Box).place(x=-2, y=255)

# Entry
entry = StringVar()
enter_number = Entry(root, textvariable=entry, width=17, justify='center', bd=0, font=('aerial',20))
enter_number.place(x=100, y=150)

# Search button
Search_image = PhotoImage(file='search-button.png')
search = Button(root, image=Search_image, height = 50, width = 50, borderwidth=0, cursor='hand2')
search.place(x=380, y=140)


root.mainloop()

