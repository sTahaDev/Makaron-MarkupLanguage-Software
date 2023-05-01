from tkinter import *
import re
class makaron():
    def __init__(self) -> None:
        # create a tkinter window
        self.__root = Tk()			

        # Open window having dimension 100x100
        self.__root.geometry('500x500')

        #Creating Tokens
        self.Tokens = {
            "text": {"enter":"<Text","params1":"title=","params2":"id="},
            "button": {"enter":"<Button","params1":"title=","params2":"id="},
            "entry": {"enter":"<Entry","params1":"title=","params2":"id="},
            
        }
        self.labels = list()
        self.buttons = list()
        self.entrys = list()
        
        

        
        pass
    
    def __createText(self,title,id):
        
        if(id == None):
            id = "text"
        self.labels.append({"label":Label(self.__root,text=title,bd=5),"id":id})
        for i in self.labels:
            i["label"].pack()
        

        pass
    def __createEntry(self,title,id):
        
        if(id == None):
            id = "entry"
        self.entrys.append({"entry":Entry(self.__root,text=title,bd=5),"id":id})
        for i in self.entrys:
            i["entry"].pack()
        

        pass
    def __createButton(self,title,id,command):
        if(id == None):
            id = "btn"
        self.buttons.append({"button":Button(self.__root, text = title, bd=5,command=command),"id":id})
        
        for i in self.buttons:
            i["button"].pack()
            pass
        
        pass
    def addFile(self,path):
        #Choosing file
        self.path = path
        pass
    def __readingFile(self):
        #Reading file
        with open(self.path) as dosya:
            read = dosya.readlines()
            reads = ""
            for i in read:
                reads += i
                pass
            reads = reads.split()
            reads = "".join(reads)
            reads = reads.split(";")
            
            
        return reads
    
    def makeListToString(self,list):
        text  =""
        for x in list:
            text += x
            pass
        return text
    
    def splitTokens(self,file,tokenMain,param1):
        allParams = list()
        for elements in file:
            if tokenMain["enter"] in elements:
                findedTokens = elements.split(",")
                for params in findedTokens:
                    if tokenMain[param1] in params:
                        newParams = params.replace(tokenMain[param1],"")
                        newParams = list(newParams)
                        newParams[0] = ""
                        newParams.pop()
                        newParams = self.makeListToString(newParams)
                        allParams.append(newParams)
                        
                        
                        
                    pass
                
                pass
        return allParams
        
    
    def main(self):
        #main method
        #print(self.readingFile())
        readFile = self.__readingFile()
        #Creating elements with tokens
        self.__elements = {
            "text": {
                "title" : self.splitTokens(readFile,self.Tokens["text"],"params1"),
                "id": self.splitTokens(readFile,self.Tokens["text"],"params2")
            },
            "button": {
                "title" : self.splitTokens(readFile,self.Tokens["button"],"params1"),
                "id":self.splitTokens(readFile,self.Tokens["button"],"params2"),
            },
            "entry": {
                "title" : self.splitTokens(readFile,self.Tokens["entry"],"params1"),
                "id": self.splitTokens(readFile,self.Tokens["entry"],"params2")
            },
        }
        self.uploadWindow()
        
        
        
    def uploadWindow(self):
        tV = 0
        bV= 0
        eV = 0
        
        for i in self.getElement()["text"]["title"]:
            self.__createText(i,self.__elements["text"]["id"][tV])
            tV += 1
            pass
        for i in self.getElement()["entry"]["title"]:
            self.__createEntry(i,self.__elements["entry"]["id"][eV])
            eV += 1
            pass
        for i in self.getElement()["button"]["title"]:
            self.__createButton(i,self.__elements["button"]["id"][bV],"sads")
            bV += 1
            pass
        pass
     
    def getElement(self):
        return self.__elements
    
    def setElementTitle(self,id,type,title):
        if type == "text":
            for i in self.labels:
                if i["id"] == id:
                    i["label"].config(text=title)
                    pass
                pass
        elif type == "button":
            for i in self.buttons:
                if i["id"] == id:
                    i["button"].config(text=title)
            pass
        
    def addButtonCommand(self,id,func):
        for i in self.buttons:
            if i["id"] == id:
                i["button"].config(command=func)
        pass
    def getEntryValue(self,id):
       
        for i in self.entrys:
            if i["id"] == id:
                value = i["entry"].get()
        return value
        pass
    
    def setWindowSize(self,width,height):
        self.__root.geometry(f"{width}x{height}")
        
        pass
    def windowResizeAble(self,resize):
        if resize == False:
            self.__root.resizable(0, 0)
        else:
            self.__root.resizable(1, 1)
    def setWindowTitle(self,title):
        self.__root.title(title)
        pass
    
        
                    


    def loop(self):
        
        
        
        self.__root.mainloop()

    
