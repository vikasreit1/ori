#!/usr/bin/env python
"""
  This program is used to flatten out a list
"""

def flatten_list(list_name):
    for each_item in list_name:
        if isinstance(each_item, list):
            flatten_list(each_item)
        else:
            print each_item
"""
def expand_list(list_name):
     for each_item in list_name:
         if isinstance(each_item,list):
            expand_list(each_item)
         else:
            print each_item
"""

movies=['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

flatten_list(movies)



