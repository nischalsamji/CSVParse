fileobj = open ("testfile.txt", "r")
filestring = f.read();

rows = filestring.split('\n')

full_data = []

for row in rows:
    full_data.append(row.split(","))
