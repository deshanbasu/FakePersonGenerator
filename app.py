import faster_than_requests as req
import tkinter as tk
import json


def request_data():
    returnData = req.get2json_pretty("https://randomuser.me/api/")
    returnData = dict(json.loads(returnData))
    results = returnData['results'][0]
    # Adding results into a array
    rec(results)
    # formatting & writing data into the disk
    writedata(bindstr(arrkeys, arr))


# Global Arrays belong to rec
arrkeys = ['Gender', 'Title', 'First Name', 'Last Name', 'Address', 'City', 'State', 'Country', 'Postal Code', 'Latitude', 'Longitude', 'Time Zone', 'Description', 'Email', 'UUID', 'User name', 'Password', 'Salt', 'MD5 Version', 'Sha1', 'Sha256', 'Date', 'Age', 'Date', 'Age', 'Phone Number', 'Cell Phone Number', 'Name', 'Value', 'Large', 'Medium', 'Thumbnail', 'NAT']
arr = []


def rec(dicto):
    if isinstance(dicto, dict) is False:
        pass
    keys = list(dicto.keys())

    for k in keys:
        if isinstance(dicto[k], (list, dict)):
            rec(dicto[k])
        else:
            # only append the array of values
            arr.append(str(dicto[k]))


def bindstr(arrkeys, arr):
    # returns a dictionary
    # arguments are from global
    major = dict(zip(arrkeys, arr))
    return major


def writedata(array):
    personName = str(array['First Name']) + "_" + str(array['Last Name'])
    with open(personName, 'w+') as file:
        file.write("THIS FILE IS GENERATED BY FAKE PERSON GENERATOR\n")

        # writing array information to text file using for loop
        for key, value in array.items():
            file.write(f'{key}  ::  {value}\n')


# Created GUI Window with Tkinter
root = tk.Tk()
root.title("Fake Person Generator")     

canvas = tk.Canvas(root, height=300, width=400)
canvas.pack()

# Adding a background image to a root
background_image = tk.PhotoImage(file='src/background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


# Created button with command included
button = tk.Button(root, text="Generate Random Person", font=40, command=request_data)
button.place(relx=0.2, rely=0.3, relheight=0.10, relwidth=0.6)


root.mainloop()
