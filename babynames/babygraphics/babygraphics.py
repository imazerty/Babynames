#!/usr/bin/env python3

"""
Stanford CS106AP BabyGraphics GUI
built on babynames data
"""

import sys
import tkinter
import babynames


# provided function to build the GUI
def make_gui(top, width, height, names):
    """
    Set up the GUI elements for Baby Names, returning the Canvas to use.
    top is TK root, width/height is canvas size, names is BabyNames dict.
    """
    # name entry field
    entry = tkinter.Entry(top, width=60, name='entry', borderwidth=2)
    entry.grid(row=0, columnspan=12, sticky='w')
    entry.focus()

    # canvas for drawing
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')
    canvas.grid(row=1, columnspan=12, sticky='w')

    space = tkinter.LabelFrame(top, width=10, height=10, borderwidth=0)
    space.grid(row=2, columnspan=12, sticky='w')

    # Search field etc. at the bottom
    label = tkinter.Label(top, text="Search:")
    label.grid(row=3, column=0, sticky='w')
    search_entry = tkinter.Entry(top, width=15, name='searchentry')
    search_entry.grid(row=3, column=1, sticky='w')
    search_out = tkinter.Text(top, height=2, width=70, name='searchout', borderwidth=2)
    search_out.grid(row=3, column=3, sticky='w')

    # When <return> key is hit in a text field .. connect to the handle_draw()
    # and handle_search() functions to do the work.
    entry.bind("<Return>", lambda event: handle_draw(entry, canvas, names))
    search_entry.bind("<Return>", lambda event: handle_search(search_entry, search_out, names))

    top.update()
    return canvas


def handle_draw(entry, canvas, names):
    """
    (provided)
    Called when <return> key hit in given entry text field.
    Gets search text from given entry, draws results
    to the given canvas.
    """
    text = entry.get()
    lookups = text.split()
    draw_names(canvas, names, lookups)


def handle_search(search_entry, search_out, names):
    """
    (provided) Called for <return> key in lower search field.
    Calls babynames.search() and displays results in GUI.
    Gets search target from given search_entry, puts results
    in given search_out text area.
    """
    target = search_entry.get().strip()
    if target:
        result = babynames.search_names(names, target)
        out = ' '.join(result)
        #searchout = top.children['searchout']  # alt strategy to access fields
        search_out.delete('1.0', tkinter.END)
        search_out.insert('1.0', out)


# provided constants
FILENAMES = ['baby-1900.txt', 'baby-1910.txt', 'baby-1920.txt', 'baby-1930.txt',
             'baby-1940.txt', 'baby-1950.txt', 'baby-1960.txt', 'baby-1970.txt',
             'baby-1980.txt', 'baby-1990.txt', 'baby-2000.txt', 'baby-2010.txt']
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
SPACE = 20
COLORS = ['red', 'purple', 'green', 'blue']


def draw_fixed(canvas):
    """
    Erases the given canvas and draws the fixed lines on it.
    """
    canvas.delete('all')
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # your code here
    pass


def draw_names(canvas, names, lookups):
    """
    Given canvas, names dict, lookups list of name strs,
    Draw the data for the lookups on the canvas.
    """
    draw_fixed(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # your code here
    pass


# main() code is provided
def main():
    args = sys.argv[1:]
    # Establish size - user can override
    width = 1000
    height = 600
    if len(args) == 2:
        width = int(args.pop(0))
        height = int(args.pop(0))

    # Load data
    names = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = make_gui(top, width, height, names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed(canvas)
    top.mainloop()


if __name__ == '__main__':
    main()
