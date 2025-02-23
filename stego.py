import cv2
import os


img = cv2.imread(r"E:\myStego-main\myStego-main\mypic.jpg.jpg")
if img is None:
    print("Error: Image not found.")
    exit()

height, width, channels = img.shape  


msg = input("Enter secret message: ")
password = input("Enter password: ")


if len(msg) > width * height:
    print("Error: Message too long for this image.")
    exit()


d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}


n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    z = (z + 1) % 3 
    if z == 0:  
        m += 1  
        if m == width: 
            m = 0
            n += 1


cv2.imwrite("Encryptedmsg.jpg", img)
os.system("start Encryptedmsg.jpg")  


message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for decryption: ")

if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == width:
                m = 0
                n += 1
    print("Decrypted message:", message)
else:
    print("Error: Invalid password.")
