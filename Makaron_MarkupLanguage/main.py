import Makaron.makaron
import tkinter

compailer = Makaron.makaron.makaron()

# .mkn dosyamızı seçiyoruz
compailer.addFile("main.mkn")
#Compaileri çalışır hale getiriyoruz
compailer.main()

def setTitle():
    compailer.setElementTitle("textid","text","Merhaba Dunya")
    pass
compailer.addButtonCommand("buttonid",setTitle)


#Sayfayo Loop ediyoruz
compailer.loop()

