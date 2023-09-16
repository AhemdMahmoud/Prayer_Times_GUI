                    #only web scraping 
import requests



def fetch_prayer_times(city, country):
  try:
    url = f"http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2"

    response = requests.get(url)
    info = response.json()

    if "data" in info:
      timing = info["data"][0]["timings"]
      return timing
    else:
      return None

  except Exception as e:
    return f"Unexpected error occurred: {e}"
city=input("please enter city name")
country=input("please enter country name") 
if city and country:
  prayer_timings=fetch_prayer_times(city,country)

  for name , time in prayer_timings.items():

    print (f"{name}:{time}")

else :
  print ("unable to fetch")                            
                           
                           
                           
                           # with gui
import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_prayer_times(city, country):
    try:
        url = f"http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2"
        response = requests.get(url)
        info = response.json()

        if "data" in info:
            timing = info["data"][0]["timings"]
            return timing
        else:
            return None

    except Exception as e:
        return f"Unexpected error occurred: {e}"

def fetch_and_display_prayer_times():
    city = city_entry.get()
    country = country_entry.get()

    if city and country:
        prayer_timings = fetch_prayer_times(city, country)

        if prayer_timings:
            result_text.delete(1.0, tk.END)  # Clear previous results
            for name, time in prayer_timings.items():
                result_text.insert(tk.END, f"{name}: {time}\n")
        else:
            messagebox.showerror("Error", "Prayer times not found for the specified location.")
    else:
        messagebox.showerror("Error", "Please enter both city and country.")

# Create the main application window
root = tk.Tk()
root.title("Prayer Times")

# Create and pack input fields
city_label = ttk.Label(root, text="City:")

city_label.pack()
city_entry = ttk.Entry(root)
city_entry.pack()

country_label = ttk.Label(root, text="Country:")

country_label.pack()
country_entry = ttk.Entry(root)
country_entry.pack()

fetch_button = ttk.Button(root, text="Fetch Prayer Times", command=fetch_and_display_prayer_times)
fetch_button.pack()

# Create and pack a text widget to display results
result_text = tk.Text(root, height=10, width=40)
result_text.pack()

# Start the main event loop
root.mainloop()
                                ##dont work
# def fetch_prayer_times(city, country):
#   try:
#     url = f"http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2"

#     response = requests.get(url)
#     info = response.json()

#     if "data" in info:
#       timing = info["data"]["timings"]
#       return timing
#     else:
#       return None

#   except Exception as e:
#     return f"Unexpected error occurred: {e}"

# def gui_fetch_prayer_times():
#   city=city_entry.get()
#   country=country_entry.get() 
  
#   if city and country:
    
#     prayer_timings=fetch_prayer_times(city,country)

#     for name , time in prayer_timings.items():
      
#       result.insert(tk.END,f"{name}:{time}")
#   else :
#     messagebox.showerror("Error","unable to fetch prayer times ,please enter correct city and country names")
  


# app = tk.Tk()
# app.title("prayer Times")
# frame = ttk.Frame(app, padding="20")
# frame.grid(row=0, column=0)

# city_lable = ttk.Label(frame, text="City:")
# city_lable.grid(row=0,column=0,pady=5)
# city_entry = ttk.Entry(frame, width=20)
# city_entry.grid(row=0, column=1,pady=5)

# country_lable = ttk.Label(frame, text="Country:")
# country_lable.grid(row=1,column=0,pady=5)
# country_entry = ttk.Entry(frame, width=20)
# country_entry.grid(row=1, column=1,pady=5) 


# fetch_button =ttk.Button(frame,text="Get Prayer Times", command=gui_fetch_prayer_times) 
# fetch_button.grid(row=2,column=1,pady=5)
# result =tk.Listbox(frame,height=11,width=30)
# result.grid(row=3,columnspan=2,pady=5) 
# app.mainloop()
