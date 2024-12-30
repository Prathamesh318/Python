bin_file=open("example.bin","wb")

data=b"this is a bianry data"

bin_file.write(data)

content=bin_file.read()

print(content)

bin_file.close()