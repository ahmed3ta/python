# # file = open("a_file.txt")
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": 9}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message}is not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise NameError("What did you do!!, just kidding")


height = float(input("Height: "))
weight = int(input("weight: "))
if height > 3:
    raise ValueError("There is no Human being whose height over 3 meters")
bmi = weight / height ** 2
