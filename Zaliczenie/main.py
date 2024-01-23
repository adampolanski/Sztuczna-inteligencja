import os
if not os.path.exists("data.csv"):
    import urllib.request

    dataUrl = open("Link_do_danycch.url", "r")
    for line in dataUrl.readlines():
        if line.startswith("URL="):
            dataUrl.close()
            dataUrl = line.removeprefix("URL=")
            break

    print(dataUrl)

    import urllib
    dataHandle = urllib.request.urlopen(dataUrl)
    writeFile = open("data.csv", "w")
    for line in dataHandle.readlines():
        l = line.decode("utf-8")
        writeFile.write(l)

    writeFile.close()

csvFile = open("data.csv", "r")
data = []
for line in csvFile.readlines():
    data.append(line.removesuffix("\n").split(","))
csvFile.close()

# check protocol_types
protocol_types = []
for line in data[1:]:
    if protocol_types.count(line[1]) == 0:
        protocol_types.append(line[1])
print(protocol_types)
