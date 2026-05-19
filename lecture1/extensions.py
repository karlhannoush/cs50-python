file = input("File name: ")

if file.lower().endswith(".gif"):
    print("image/gif")
elif file.lower().endswith(".jpg")  or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.lower().endswith(".png"):
    print("image/png")
elif file.lower().endswith(".pdf"):
    print("application/pdf")
elif file.lower().endswith(".txt"):
    print("text/plain")
elif file.lower().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")