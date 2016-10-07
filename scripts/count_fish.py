# Add up the number of creatures in a data file
import sys

def should_skip_line(line):
    """
    Skip line if it's a comment or a title line.
    """
    return line.startswith('#') or line.startswith('Date')

def get_count(line):
    """
    Extract count portion of a data record and return that number.
    """
    temp = line.strip()
    fields = temp.split(',')
    count = int(fields[2])
    return count

def get_total(source, filename):
    """
    Count the number of creatures seen in a data file.
    """
    total = 0
    for line in source:
        if should_skip_line(line):
            pass
        else:
            total += get_count(line)
    print(filename + ':', total)

all_filenames = sys.argv[1:]
for filename in all_filenames:
    reader = open(filename)
    get_total(reader, filename)
    reader.close()
