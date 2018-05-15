import os

def load(name):
    # todo: populate from storage if file already exists.
    return []


def save(name, data):
    filename = os.join('./journals/', name)
    file = open(filename,'w')

    for entry in data:
        file.write(entry)

    file.close()

def add_entry(entry, data):
    data.append(entry)
