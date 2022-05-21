a_file = gzip.open("test.txt.gz", "rb")
contents = a_file.read()

print(contents)