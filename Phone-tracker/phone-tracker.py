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

def Track():
    enter_number = entry.get()
    number = phonenumbers.parse(enter_number)
    
    # Country
    locate = geocoder.description_for_number(number, 'en')
    country.config(text=locate)
    
    # operator e.g. Idea, airtel, jio
    operator = carrier.name_for_number(number, 'en')
    sim.config(text=operator)
    
    # Phone timeZone
    time = timezone.time_zones_for_number(number)
    zone.config(text=time)
    
    # Longitude and Latitude
    geolocator = Nominatim(user_agent='geoapiExercises')   
    location = geolocator.geocode(locate)
    lng = location.longitude
    lat = location.latitude
    longitude.config(text=lng)    
    latitude.config(text=lat)
    
    # Time on Phone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %[]')
    clock.config(text=current_time)

# ======= GUI =========
# Icon image
icon = PhotoImage(file='icon.png')
root.iconphoto(False, icon)

# Logo
logo = PhotoImage(file='phone-track.png')
Label(root,image=logo, width=100, height=100).place(x=200,y=30)

# Search bar
#Eback = PhotoImage(file='search.png')
#Label(root,image=Eback).place(x=130,y=30)

# Heading
Heading = Label(root, text='Track Number', font=('arial', 16, 'bold'))
Heading.place(x=180, y=10)

# Bottom
Box = PhotoImage(file='bottom.png')
Label(root, image=Box).place(x=-2, y=255)

# Entry
entry = StringVar()
enter_number = Entry(root, textvariable=entry, width=17, justify='center', bd=0, font=('aerial',20))
enter_number.place(x=100, y=150)

# Search button
Search_image = PhotoImage(file='search-button.png')
search = Button(root, image=Search_image, height = 50, width = 50, borderwidth=0, cursor='hand2', bd=0, command=Track)
search.place(x=380, y=140)

# label(information)
country = Label(root, text='Country: ', bg='#57adff', fg='black', font=('arial', 10, 'bold'))
country.place(x=100, y=200)

sim = Label(root, text='SIM: ', bg='#57adff', fg='black', font=('arial', 10, 'bold'))
sim.place(x=100, y=250)

zone = Label(root, text='TimeZone: ', bg='#57adff', fg='black', font=('arial', 10, 'bold'))
zone.place(x=100, y=300)

clock = Label(root, text='Phone Time: ', bg='#57adff', fg='black', font=('arial', 10, 'bold'))
clock.place(x=280, y=200)

latitude = Label(root, text='Latitude (N): ', bg='#57adff', fg='black', font=('arial', 10, 'bold'))
latitude.place(x=280, y=250)

longitude = Label(root, text='Longitude (E): ', bg='#57adff', fg='black', font=('arial', 10, 'bold'))
longitude.place(x=280, y=300)

root.mainloop()

