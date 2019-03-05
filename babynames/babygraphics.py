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
    "top horiz line"
    canvas.create_line(SPACE, SPACE, width - SPACE, SPACE, width=2, fill='black')
    "bottom horizontal line"
    canvas.create_line(SPACE, height - SPACE, width - SPACE, height - SPACE, width=2, fill='black')
    "Draw a vertical year line for each year (use len(YEARS) as the number of years"
    for i in range(len(YEARS)):
         deltax = (width - 2 * SPACE)/len(YEARS)
         "vertical line"
         canvas.create_line(SPACE + deltax * i, 0, SPACE + deltax * i, height, width=2, fill='black')
         canvas.create_text(2 + SPACE + deltax * i, height - SPACE , text= YEARS[i], anchor=tkinter.NW)

    pass


def draw_names(canvas, names, lookups):
    """
    Given canvas, names dict, lookups list of name strs,
    Draw the data for the lookups on the canvas.
    """
    draw_fixed(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    a = (height - 2 * SPACE) / 999
    b = SPACE - a
    deltax = (width - 2 * SPACE)/len(YEARS)
    "pour chaque nom recherché"

    for i in range(len(lookups)):
        name = lookups[i]
        k = i % len(COLORS)
        color = COLORS[k]
        "pour chaque decade"
        for j in range(len(YEARS) - 1):

            year1 = YEARS[j]
            year2 = YEARS[j + 1]
            x1 = SPACE + deltax * j
            x2 = x1 + deltax


            for key, value in names.items():
                    if name.lower() == key.lower() :
                        print(value)
                        "year present in archive"
                        if str(year1) in value.keys():
                            rank1 = int(value[str(year1)])

                        else:
                            rank1 = 1000
                            "year present in archive"
                        if str(year2) in value.keys():
                            rank2 = int(value[str(year2)])

                        else:
                            rank2 = 1000
                        y1 = a * rank1  + b
                        y2 = a * rank2  + b
                        if name.lower() == key.lower() :
                            canvas.create_line(x1, y1, x2, y2, width=2, fill=color)
                            name = name.capitalize()
                            msg = name + " " + str(rank1)
                            canvas.create_text(2 + x1, y1 - 2 , text= msg ,fill = color, anchor=tkinter.SW)

    # your code here
    """for i in range(len(lookups)):

            name = lookups[i]
            for key, value in names.items():
                for j in range(len(YEARS) - 1):
                    if name.lower() == key.lower() :

                            if  YEARS[j] in names[key].values():
                                rank1 = names[key][YEARS[j]]
                                "y1 = height - SPACE + 1000 - rank1;"

                            else:
                                y1 = height - SPACE;
                                rank1 = 1000
                            if YEARS[j + 1] in names[key].values():
                                rank2 = names[key][YEARS[j]]
                                "y2 = height - SPACE + 1000 - rank2; "
                            else:
                                "y2 = height - SPACE;"
                                rank2 = 1000
                            x1 = SPACE * (j + 1)
                            x2 = x1 + SPACE
                            a = (height - 2 * SPACE) / 999
                            b = SPACE - a
                            y1 = a * rank1 + b
                            y2 = a * rank2 + b

                            canvas.create_line(x1, y1, x2, y2, width=2, fill="black")
                    else:
                        canvas.create_line(SPACE * (j + 1), height - SPACE, SPACE * (j + 2), height - SPACE, width=2, fill="black")
    """
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
