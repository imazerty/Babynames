import sys, os


def add_name(names, year, rank, name):
    """
    Adds the given data: int year, int rank, str name
    to the given names dict which is returned.
    MORE TESTS TBD
    >>> sorted(add_name({}, 2000, 10, 'abe').items())
    [('abe', {2000: 10})]
    """
    if not (name in names):
        names[name] = {}
        names[name][year] = rank
    elif year not in names[name]:
        names[name][year] = rank
    elif rank < names[name][year]:
        names[name][year] = rank

    return names
    pass

def read_files(filenames):
    """
    Given list of filenames, build and return a names dict
    of all their data.
    """
    names = {}
    for filename in filenames:
        with open(filename, 'r') as f:
            i = 0

            for line in f:
                if i == 0:
                    word = line.strip().split()
                    year = word[0].strip()

                else:
                    splittedLine = line.strip().split(',')
                    rank = splittedLine[0].strip()


                    nameMale = splittedLine[1].strip()
                    nameFemale = splittedLine[2].strip()
                    names = add_name(names, year, rank, nameMale)
                    names = add_name(names, year, rank, nameFemale)

                i = i + 1
    return names
    pass
def search_names(names, target):
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    (TESTS TBD)
    """
    nameStrings = []
    for key, value in names.items():
        if target.lower() in key.lower() :
            nameStrings.append(key)
    return sorted(nameStrings)
    pass

def print_names(names):
    """
    (provided)
    Given names dict, print out all its data, one name perline.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Establish if we have a search-target or not
    # Remove it from args if present
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        args.pop(0)
        target = args.pop(0)

    # Read in all the files: baby-1990.txt, baby-2000.txt, ...
    # Handily, args is just a list of filenames at this point.

    names = read_files(args)
    "print(names)"
    # Either we do a search or just print everything.
    if target:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:

        print_names(names)



if __name__ == '__main__':

    main()
