# Importing library
import qrcode
  

# Enter link for the website which is represented by the QR code
input_data = input("Enter link: ")

# Creating the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Adding the link inputted
qr.add_data(input_data)
qr.make(fit=True)

# Making the QR image
img = qr.make_image(fill='black', back_color='white')

# Saving the QR code
img.save('qrcode001.png')