#!/usr/bin/env python

import json
import unicodedata
from ttk import Combobox
from tkinter import *
from pprint import pprint


class App(Frame):
    cities_list = None
    value_of_combo = 'X'
    location_box_value = "Marina"

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        self.cities_list = []
        self.read_data()
        self.widgets()
        self.city_label=""
        self.latitude_label=""
        self.longitude_label = ""




    def widgets(self):

        """Initialize all the widgets on the Gui"""

        # Initialize Combobox for dropdown of cities
        self.location_box_value = StringVar()
        self.city_label = Label(root, text="City")
        self.city_label.grid(columnspan=2, row=0, sticky=W)
        self.location_box = Combobox(self.master, textvariable=self.location_box_value)
        self.location_box['values'] = tuple(self.get_cities())
        self.location_box.set("Marina")
        self.location_box.bind("<<ComboboxSelected>>", self.filter)
        self.location_box.current(0)
        self.location_box.grid(column=15, row=0)

        # Initialize the Entry widgets along with Labels

        self.county_label = Label(root, text="County")
        self.county_label.pack(side=LEFT)
        self.county_label.grid(column=1, rowspan=2)
        self.county_entry = Entry(root, bd=5)
        self.county_entry.grid(column=15, row=2)
        self.county_entry.insert(0,"Monterey County")

        self.latitude_label = Label(root, text="Latitude")
        self.latitude_label.pack(side=LEFT)
        self.latitude_label.grid(column=1, row=4)
        self.latitude_entry = Entry(root, bd=5)
        self.latitude_entry.grid(column=15, row=4)
        self.latitude_entry.insert(0,36.68)

        self.longitude_label = Label(root, text="Longitude")
        self.longitude_label.pack(side=LEFT)
        self.longitude_label.grid(column=1, row=5)
        self.longitude_entry = Entry(root, bd=5)
        self.longitude_entry.grid(column=15, row=5)
        self.longitude_entry.insert(0,-121.8)

        root.config(menu=self.location_box)

    def set_text(self, record):
        self.county_entry.delete(0, END)
        self.county_entry.insert(0, record[1])
        self.latitude_entry.delete(0, END)
        self.latitude_entry.insert(0, record[2])
        self.longitude_entry.delete(0, END)
        self.longitude_entry.insert(0, record[3])

        return

    def filter(self, event):
        self.value_of_combo = self.location_box.get()
        print "Hi"+self.value_of_combo
        for record in self.cities_list:
            if record[0] == self.value_of_combo:
                self.set_text(record)

    def get_cities(self):
        cities = []
        for city_record in self.cities_list:
            cities.append(city_record[0])
        return cities

    def read_data(self):
        try:

            json_data = open("./ca.json").read()

            data = json.loads(json_data)

            self.populate_cities(data)
        except IOError:
            print "Error: can\'t find file or read data"

    def populate_cities(self, data):

        for city_record in data:
            record = []

            if city_record["county_name"] is not None:
                record.append((unicodedata.normalize('NFKD', city_record["name"]).encode('ascii', 'ignore')))
                record.append(
                    (unicodedata.normalize('NFKD', city_record["full_county_name"]).encode('ascii', 'ignore')))
                record.append(
                    (unicodedata.normalize('NFKD', city_record["primary_latitude"]).encode('ascii', 'ignore')))
                record.append(
                    (unicodedata.normalize('NFKD', city_record["primary_longitude"]).encode('ascii', 'ignore')))
                self.cities_list.append(record)


root = Tk()
root.title("City Information")
root.geometry("350x250+300+300")
app = App(root)
root.mainloop()
