import datetime

hora = datetime.datetime.now().hour

if (hora >= 21 or hora <= 6):
    print("Buenas noches")
elif (hora >= 12):
    print("Buenas tardes")
else:
    print("Buenos días")