#!/usr/bin/env python

from collections import Counter


class ListOperations:
    items = []

    def __init__(self):

        self.items = []

    def append_items(self, item, items_list=None):

        if items_list is None:
            try:
                self.items.append(item)
            except IndexError:
                pass
            return self.items
        else:
            try:
                items_list.append(item)
            except IndexError:
                pass
            return items_list

    def insert_item(self, item, index, items_list=None):

        if items_list is None:
            try:
                self.items.insert(index, item)
            except IndexError:
                pass
            return self.items


        else:
            try:
                items_list.insert(index, item)
            except IndexError:
                pass
            return items_list

    def get_unique_items(self, items_list=None):
        if items_list is None:

            if self.items is not None:

                items_set = set(self.items)
                unique_list = list(items_set)
                return unique_list

            else:
                print "List empty "

        else:
            items_set = set(items_list)
            unique_list = list(items_set)
            return unique_list

    def get_item_frequency(self, items_list=None):

        if items_list is None:
            frequency = Counter(self.items)

            return frequency
        else:
            frequency = Counter(items_list)
            return frequency

    def store_items_to_list(self, items_list=None):

        if items_list is None:
            print "Please pass an input list to store"

        else:

            self.items = items_list
            return self.items


