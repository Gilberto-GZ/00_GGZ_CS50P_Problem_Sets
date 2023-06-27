file_name = input("File Name: ").strip().casefold()

suffix = (".gif",".jpg", "jpeg", ".png", "pdf", "txt", "zip")

if file_name.endswith(suffix[0]):
    print("image/gif")

elif file_name.endswith(suffix[1]):
    print("image/jpeg")

elif file_name.endswith(suffix[2]):
    print("image/jpeg")

elif file_name.endswith(suffix[3]):
    print("image/png")

elif file_name.endswith(suffix[4]):
    print("application/pdf")

elif file_name.endswith(suffix[5]):
    print("text/plain")

elif file_name.endswith(suffix[6]):
    print("application/zip")



else:
    print("application/octet-stream")