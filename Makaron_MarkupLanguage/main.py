import Makaron.makaron
import tkinter

compailer = Makaron.makaron.makaron()

# .mkn dosyamızı seçiyoruz
compailer.addFile("main.mkn")
#Compaileri çalışır hale getiriyoruz
compailer.main()

compailer.setWindowSize(400,300)
compailer.windowResizeAble(False)

def setTitle():
    compailer.setElementTitle("textid","text",compailer.getEntryValue("entry1"))
    pass
compailer.addButtonCommand("buttonid",setTitle)


#Sayfayo Loop ediyoruz
compailer.loop()

