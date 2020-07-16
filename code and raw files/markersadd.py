from PIL import Image, ImageDraw, ImageFont

file_array = ["black", "blue", "brown", "cyan", "green", "indigo", "limegreen", "magenta", "navy", "olive", "orange", "purple", "red", "teal", "turquoise", "yellow", "grey"]

for x in file_array:
	'''
	for num in range(0, 10):
		img = Image.open(r"raw files\new markers\%s.png" % x)
		width1, height1 = img.size
		print(width1, height1)
		fnt = ImageFont.truetype(r'Montserrat-Bold.ttf', 30)
		d = ImageDraw.Draw(img)
		converted_num = str(num)
		d.text((16,8), converted_num, font=fnt, fill="black")
		img.thumbnail((width1/2, height1/2))
		img.save("D:\zalt\Google Maps Markers\images\marker_%(s1)s%(s2)s.png" %{'s1': x, 's2': num }, "png")

	for num in range(10, 20):
		img = Image.open(r"raw files\new markers\%s.png" % x)
		width, height = img.size
		print(width, height)
		fnt = ImageFont.truetype(r'Montserrat-Bold.ttf', 30)
		d = ImageDraw.Draw(img)
		converted_num = str(num)
		d.text((9,8), converted_num, font=fnt, fill="black")
		img.thumbnail((width1/2, height1/2))
		img.save("D:\zalt\Google Maps Markers\images\marker_%(s1)s%(s2)s.png" %{'s1': x, 's2': num }, "png")


	for num in range(11, 12):
		img = Image.open(r"raw files\new markers\%s.png" % x)
		width, height = img.size
		print(width, height)
		fnt = ImageFont.truetype(r'Montserrat-Bold.ttf', 30)
		d = ImageDraw.Draw(img)
		converted_num = str(num)
		d.text((12,8), converted_num, font=fnt, fill="black")
		img.thumbnail((width1/2, height1/2))
		img.save("D:\zalt\Google Maps Markers\images\marker_%(s1)s%(s2)s.png" %{'s1': x, 's2': num }, "png")

	for num in range(20, 100):
		img = Image.open(r"raw files\new markers\%s.png" % x)
		width, height = img.size
		print(width, height)
		fnt = ImageFont.truetype(r'Montserrat-Bold.ttf', 30)
		d = ImageDraw.Draw(img)
		converted_num = str(num)
		d.text((6,8), converted_num, font=fnt, fill="black")
		img.thumbnail((width1/2, height1/2))
		img.save("D:\zalt\Google Maps Markers\images\marker_%(s1)s%(s2)s.png" %{'s1': x, 's2': num }, "png")


	for num in range(21, 22):
		img = Image.open(r"raw files\new markers\%s.png" % x)
		width, height = img.size
		print(width, height)
		fnt = ImageFont.truetype(r'Montserrat-Bold.ttf', 30)
		d = ImageDraw.Draw(img)
		converted_num = str(num)
		d.text((9.5,8), converted_num, font=fnt, fill="black")
		img.thumbnail((width1/2, height1/2))
		img.save("D:\zalt\Google Maps Markers\images\marker_%(s1)s%(s2)s.png" %{'s1': x, 's2': num }, "png")


	alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	for num in alphabets:
		img = Image.open(r"raw files\new markers\%s.png" % x)
		width1, height1 = img.size
		print(width1, height1)
		fnt = ImageFont.truetype(r'Montserrat-Bold.ttf', 30)
		d = ImageDraw.Draw(img)
		converted_num = str(num)
		d.text((14,7), converted_num, font=fnt, fill="black")
		img.thumbnail((width1/2, height1/2))
		img.save("D:\zalt\Google Maps Markers\images\marker_%(s1)s%(s2)s.png" %{'s1': x, 's2': num }, "png")

	'''

	for num in range(0,1):
		img = Image.open(r"raw files\new markers\%s.png" % x)
		width1, height1 = img.size
		print(width1/10, height1/10)
		img.thumbnail((width1/2, height1/2))
		back_im = img.copy()

		img2 = Image.open(r"bikeimg.jpg")
		width2, height2 = img2.size
		print(width2/10, height2/10)
		img2.thumbnail((width2/100, height2/100))
		back_im.paste(img2)
		img.save("bike\marker_bike_%(s1)s.png" %{'s1': x}, "png")
