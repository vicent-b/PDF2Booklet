from PyPDF2 import PdfWriter, PdfReader
import re

import os

from Mainwindow import *
from language   import *

# INDEX
# -Window class and init
# -GLOBAL VARS
# -BASIC UTIL FUNCTIONS
# -BASIC GUI FUNCTIONS
# -COMPLEX FUNCTIONS
# -GUI EVENTS (Common code)
# -GUI EVENTS
# -MAIN PROGRAM AND AUTOTEST
#


#--------------------------------------------------------------------------------------------
##Window class and init

class myQtApp_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

#--------------------------------------------------------------------------------------------

##GLOBAL VARS
DebugMode = False
AutoTestMode=False #not impelmented yet
Npages = -1 #-1 means nothing loaded
Npages_inserted = -1 #-1 means string not valid
Npages_isValid = False
LanguageID = 0

#PDF file managing
PDF_OpenedFileName = ""
PDF_OpenedFile = None
PDF_OpenedFile_as_PdfReader = None

PDF_LastSelectedFolder = ""


#window
app=QApplication()
MainWindow=myQtApp_MainWindow()


#********************************************************************************************


#--------------------------------------------------------------------------------------------
##BASIC UTIL FUNCTIONS

def DEBUG(content):
    if(not DebugMode):
        return
    print("DEBUG: ", end="")
    print(content  , end="")
    print("\n"     , end="")
 


def InsertBlankPages_Text2Array(str):
    str = str.replace(" ","")

    if(str==""):
        return []
    

    IsValidRegex=re.compile("^-?\d+(,-?\d+)*$")

    DEBUG(IsValidRegex)

    if (not bool(IsValidRegex.fullmatch(str))):
        return None
    
    
    ExtractNumberRegex=re.compile("(?<!\d)(-?\d+)(?!\d)")
    MatchList=ExtractNumberRegex.findall(str)

    out = []
    for i in range(len(MatchList)):
        out.append(int(MatchList[i]))
    
    DEBUG("InsertBlankPages_Text2Array: "+str)
    DEBUG(out)
    return out


def InsertBlankPages_Clean(positionsArr, numpages): #Convert all indexes to positive numbers (negatives indicate counting from the back) and check no out ouf bounds are ocurring
    
    arr = positionsArr.copy()

    for i in range(len(arr)):
        if(arr[i]<0):
            arr[i]=numpages-(-arr[i])+1; #count from end

    arr.sort()
    DEBUG("InsertBlankPages_Clean: ")
    DEBUG(arr)
    return arr


def getFolderFromFullPath(str):

    while(str[-1] != '\\' and str[-1] != '/' ): #remove last character until is is \ or /
        str=str[:-1]
        
    return str

def getFilenameFromFullPath(FullPath, FolderPath, extension):
    str=FullPath

    str = str[len(FolderPath):-len(extension)]
        
    return str

#--------------------------------------------------------------------------------------------
##BASIC GUI FUNCTIONS

def DisplayERROR(ErrorCode): #Errorcode 0 means leave it empty
    global LanguageID
    global ERROR_MessageTable
    global MainWindow
    MainWindow.plainTextEdit_ErrorConsole.setPlainText(ERROR_MessageTable[ErrorCode][LanguageID])
   

def updateNpages_warning(n_old, n_inserted, isvalid_bool ,languageID):
    global MainWindow

    if (n_old == -1 or n_inserted == -1):
        MainWindow.label_Valid.setText("--")
        return

    if (isvalid_bool):
        MainWindow.label_Valid.setText(strLang_Valid_Yes[languageID])
    else:
        MainWindow.label_Valid.setText(strLang_Valid_No[languageID])
    
def updateNpages_text(n_old, n_inserted, isvalid_bool, languageID):
    global MainWindow

    MainWindow.label_NpagesOriginal.setText(str(n_old) if n_old >= 0 else "--")
    MainWindow.label_NpagesInserted.setText(str(n_inserted) if n_inserted >=0 else "--")
    
    updateNpages_warning(n_old, n_inserted, isvalid_bool, languageID)


def strLang_update(languageID):
    global MainWindow
    global Npages
    global Npages_inserted
    global Npages_isValid

    i=languageID
    MainWindow.pushButton_LoadFile.setText(strLang_LoadFile[i])
    MainWindow.label_InsertText.setText(strLang_InsertText[i])
    MainWindow.label_InsertInstructionText.setText(strLang_InsertInstructionText[i])
    MainWindow.label_NpagesOriginalText.setText(strLang_NpagesOriginalText[i])
    MainWindow.label_NpagesInsertedText.setText(strLang_NpagesInsertedText[i])
    MainWindow.label_ValidText.setText(strLang_ValidText[i])

    updateNpages_warning(Npages, Npages_inserted, Npages_isValid, languageID)

    MainWindow.radioButton_Save_Whole.setText(strLang_Save_Whole[i])
    MainWindow.radioButton_Save_Separately.setText(strLang_Save_Separately[i])
    MainWindow.pushButton_Convert_NoReorder.setText(strLang_Convert_NoReorder[i])
    MainWindow.pushButton_Convert.setText(strLang_Convert[i])

    #Hide/show info tabs of different languages
    MainWindow.tabWidget.setTabVisible(1,languageID==0)
    MainWindow.tabWidget.setTabVisible(2,languageID==1)
    MainWindow.tabWidget.setTabVisible(3,languageID==2)
    MainWindow.tabWidget.setTabVisible(4,languageID==3)


#--------------------------------------------------------------------------------------------
##COMPLEX FUNCTIONS

def PDF_OpenFile(filePath):
    global PDF_OpenedFile
    global PDF_OpenedFile_as_PdfReader
    global Npages
    global Npages_inserted
    global Npages_isValid

    if(PDF_OpenedFile is not None):
        PDF_OpenedFile.close()
        
    PDF_OpenedFile = open(filePath, "rb")
    PDF_OpenedFile_as_PdfReader = PdfReader(PDF_OpenedFile)

    Npages = len(PDF_OpenedFile_as_PdfReader.pages)
    Npages_isValid = Npages >= 0 and Npages_inserted>=0 and (Npages+Npages_inserted)%4==0




    

def PDF_InsertBlankPages(input_pdf, positionsArr):
    
    numpages = len(input_pdf.pages)

    #insertBlankPages_str = MainWindow.lineEdit_Insert.text()

    positionsArr = InsertBlankPages_Clean(positionsArr, numpages)

    for i in range(len(positionsArr)):
        if(positionsArr[i] < 0 or positionsArr[i] > numpages):
            DisplayERROR(4)
            return
    
    pageWidth  = input_pdf.pages[0].mediabox.width
    pageHeight = input_pdf.pages[0].mediabox.height
        
    output_pdf = PdfWriter()
    
    i=-1 #page number index
    j=0  #positionsArr index
    while (i < numpages + 1): #inser blank must execute even after last page was copied
        pagenum=i+1
        if(j < len(positionsArr) and (pagenum-1) == positionsArr[j]):
            #checks on pagenum-1 because copy page code is after andd blank page code, but blank pages must come AFTER page number
            output_pdf.add_blank_page(pageWidth, pageHeight)
            j=j+1 #execute loop again with same i and next j
        else:
            if(i>=0 and i < numpages): #insert blank must execute even before and after first and last pages were copied
                output_pdf.add_page(input_pdf.pages[i]) 
            i=i+1 #next iteration will have same j and next i
    

    return output_pdf



def PDF_ReorderFile(input_pdf):

    output_pdf = PdfWriter()
    numpages = len(input_pdf.pages)

    for page in range(round(numpages/4)):
        output_pdf.add_page(input_pdf.pages[numpages-1-page*2])
        output_pdf.add_page(input_pdf.pages[page*2])
        output_pdf.add_page(input_pdf.pages[page*2 + 1])
        output_pdf.add_page(input_pdf.pages[numpages-2-page*2])

    return output_pdf

def PDF_getCover(full_pdf):
    output_pdf = PdfWriter()

    for i in range(4):
        output_pdf.add_page(full_pdf.pages[i])
    
    return output_pdf



def PDF_getContent(full_pdf):
    output_pdf = PdfWriter()

    for i in range(len(full_pdf.pages)-4):
        j=i+4
        output_pdf.add_page(full_pdf.pages[j])
    
    return output_pdf


def PDF_SaveFile(input_pdf, filePath):
    input_pdf.write(filePath)
    return

##--------------------------------------------------------------------------------------------
##GUI EVENTS (COMMON CODE)

def pseudoevent_AnyPDFSaveButtonPressed(str_windowtitle, str_SUFFIX, bool_reorder, bool_separateCover, autotest_folderout="", autotest_insertstring=""):
    #this pseudoevent function is a generalisation of multiple button events

    global Npages_inserted
    global Npages_isValid
    global PDF_OpenedFile_as_PdfReader
    global PDF_LastSelectedFolder
    global AutoTestMode

    if(PDF_OpenedFile is None):
        DisplayERROR(1)
        return
    
    if(Npages_inserted==-1):
        DisplayERROR(2)
        return

    if (bool_reorder and not Npages_isValid):
        DisplayERROR(3)
        return
    
    DisplayERROR(0)

    if(AutoTestMode): #if automatic test running, forces a blank page insert pattern
        positionsArr = InsertBlankPages_Text2Array(autotest_insertstring)
    else:
        positionsArr = InsertBlankPages_Text2Array(MainWindow.lineEdit_Insert.text())
    
    PDFinserted  = PDF_InsertBlankPages(PDF_OpenedFile_as_PdfReader, positionsArr)

    if(bool_reorder):
        PDFreordered = PDF_ReorderFile(PDFinserted)
        PDFsave = PDFreordered
    else:
        PDFsave = PDFinserted

    #if output full file
    if(not bool_separateCover):
        if(AutoTestMode): #if automatic test running, forces a path for autotest
            filename = autotest_folderout + PDF_OpenedFileName + str_SUFFIX + ".pdf"
        else:
            fname = QFileDialog.getSaveFileName(None, str_windowtitle, PDF_LastSelectedFolder + PDF_OpenedFileName + str_SUFFIX + ".pdf","PDF files (*.pdf)")
            filename = fname[0]

        if(filename == ""):
            return
        PDF_LastSelectedFolder = getFolderFromFullPath(filename) #remember folder
        PDF_SaveFile(PDFsave, filename)

    #if separate cover
    else: 
        if(AutoTestMode): #if automatic test running, forces a path for autotest
            filename = autotest_folderout + PDF_OpenedFileName + str_SUFFIX + "-COVER" + ".pdf"
        else:
            fname = QFileDialog.getSaveFileName(None, str_windowtitle + ": COVER", PDF_LastSelectedFolder + PDF_OpenedFileName + str_SUFFIX + "-COVER" + ".pdf","PDF files (*.pdf)")
            filename = fname[0]

        if(filename == ""):
            return
        PDF_LastSelectedFolder = getFolderFromFullPath(filename) #remember folder

        PDF_SaveFile(PDF_getCover(PDFsave), filename)

        if(AutoTestMode): #if automatic test running, forces a path for autotest
            filename = autotest_folderout + PDF_OpenedFileName + str_SUFFIX + "-CONTENT" + ".pdf"
        else:
            fname = QFileDialog.getSaveFileName(None, str_windowtitle + ": CONTENT", PDF_LastSelectedFolder + PDF_OpenedFileName + str_SUFFIX + "-CONTENT" + ".pdf","PDF files (*.pdf)")
            filename = fname[0]

        
        if(filename == ""):
            return
        PDF_LastSelectedFolder = getFolderFromFullPath(filename) #remember folder

        PDF_SaveFile(PDF_getContent(PDFsave), filename)
    

#--------------------------------------------------------------------------------------------
##GUI EVENTS

def event_radioButtonLanguage(RadioButtonObject, languageID):
    global LanguageID

    DEBUG("radioButtonLanguage: "+str(languageID));
    if(RadioButtonObject.isChecked()):
        LanguageID=languageID
        strLang_update(LanguageID)
        DEBUG("radioButtonLanguage: UPDATED");


def emulate_event_pushButtonLoadFile(filename):
    #Remember update warning and numpages
    global MainWindow
    global PDF_LastSelectedFolder
    global PDF_OpenedFileName
    global Npages
    global Npages_inserted
    global Npages_isValid
    global LanguageID

    if(filename != ""):    
        PDF_LastSelectedFolder = getFolderFromFullPath(filename) #remember folder
        PDF_OpenedFileName = getFilenameFromFullPath(filename, PDF_LastSelectedFolder, ".pdf")

        PDF_OpenFile(filename)
        updateNpages_text(Npages, Npages_inserted, Npages_isValid, LanguageID)

        MainWindow.lineEdit_OpenFile.setText(filename) #Write location up
    
    DEBUG("PDF_LastSelectedFolder: " + PDF_LastSelectedFolder)
    DEBUG("PDF_OpenedFileName: " + PDF_OpenedFileName)

    


def event_pushButtonLoadFile(): #Open PDF file
    #Remember update warning and numpages

    DEBUG("pushButtonLoad: pressed");
    fname = QFileDialog.getOpenFileName(None, 'Open file', "" ,"PDF files (*.pdf)")

    filename = fname[0]
    
    DEBUG("fname:")
    DEBUG(fname)
    DEBUG(fname[0])

    emulate_event_pushButtonLoadFile(filename)
    



def event_pushButtonConvert_NoReorder(): #Convert PDF with inserted pages but without reordering for printing
    DEBUG("pushButtonConvertNoReorder: pressed");
    pseudoevent_AnyPDFSaveButtonPressed("Save PDF", "-PDF2BOOKLET_NOREORDER", False, False)

    

def event_pushButtonConvert(): #Convert PDF with inserted pages and page reordering afterwards
    global MainWindow
    DEBUG("pushButtonConvert: pressed")
    pseudoevent_AnyPDFSaveButtonPressed("Save PDF", "-PDF2BOOKLET", True, MainWindow.radioButton_Save_Separately.isChecked())


    

def event_textline_InsertBlankPages_textEdited(): #Any edit
    global MainWindow
    global Npages
    global Npages_inserted
    global Npages_isValid
    global LanguageID
    DEBUG("event_textline_InsertBlankPages_textEdited");
    
    str= MainWindow.lineEdit_Insert.text()

    ArrPages=InsertBlankPages_Text2Array(str)

    DEBUG(ArrPages)
  
    Npages_inserted = -1 if ArrPages is None else len(ArrPages)     

    Npages_isValid = Npages >= 0 and Npages_inserted>=0 and (Npages+Npages_inserted)%4==0

    updateNpages_text(Npages, Npages_inserted, Npages_isValid, LanguageID)
    #str = textLineObject

def event_textline_InsertBlankPages(): #After clicking outside
    #Remember update warning and numpages
    return



#---------------------------------------------------------------------------------------------

def AutoTest():
    #generate expected outputs from TEST FILES
    print("***INIT AUTOTEST***")
    currentFolder = os.path.realpath(__file__)
    print(currentFolder)
    currentFolder=getFolderFromFullPath(currentFolder)
    print(currentFolder)

    if(not os.path.exists(currentFolder+"\\PDF2Booklet.py")): 
        print("SAFETY CHECK FAILED!!!")
        return #safety check

    testFolder=currentFolder+"TESTFILES\\"
    testoutFolder=currentFolder+"TESTFILES\\TESTOUT\\"

    print(testFolder)
    print(testoutFolder)

    #testfilelist= [for f in os.listdir(testFolder) if isfile(join(testFolder,f))]

    testfileList_NoInsert = ["TESTFILE 4.pdf", "TESTFILE 8.pdf", "TESTFILE 16.pdf"]

    for f in testfileList_NoInsert:
        f = testFolder + "\\" + f
        emulate_event_pushButtonLoadFile(f)
        pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET", True , False, testoutFolder)
        pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET", True , True , testoutFolder)
        print(f + " EMULATED!")
    
    emulate_event_pushButtonLoadFile(testFolder+"TESTFILE 5.pdf")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET-NOREORDER", False, False, testoutFolder, "0,1,-1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET-NOREORDER", False, True , testoutFolder, "0,1,-1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET",           True , False, testoutFolder, "0,1,-1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET",           True , True , testoutFolder, "0,1,-1")

    emulate_event_pushButtonLoadFile(testFolder+"TESTFILE 7.pdf")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET-NOREORDER", False, False, testoutFolder, "1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET-NOREORDER", False, True , testoutFolder, "1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET",           True , False, testoutFolder, "1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET",           True , True , testoutFolder, "1")

    emulate_event_pushButtonLoadFile(testFolder+"TESTFILE 15.pdf")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET-NOREORDER", False, False, testoutFolder, "1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET-NOREORDER", False, True , testoutFolder, "1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET",           True , False, testoutFolder, "1")
    pseudoevent_AnyPDFSaveButtonPressed("", "-PDF2BOOKLET",           True , True , testoutFolder, "1")



    

def Init():
    global MainWindow

    #Precalculate global variables
    
    #Disable GUI elements
    MainWindow.radioButton_Language_Xertoli.setVisible(False)
    MainWindow.radioButton_Language_Xertoli.setDisabled(True)

    #Set events
    MainWindow.radioButton_Language_Catala.toggled.connect(lambda: event_radioButtonLanguage(MainWindow.radioButton_Language_Catala, 0))
    MainWindow.radioButton_Language_Castellano.toggled.connect(lambda: event_radioButtonLanguage(MainWindow.radioButton_Language_Castellano, 1))
    MainWindow.radioButton_Language_English.toggled.connect(lambda: event_radioButtonLanguage(MainWindow.radioButton_Language_English, 2))

    MainWindow.pushButton_LoadFile.clicked.connect(event_pushButtonLoadFile)
    MainWindow.pushButton_Convert_NoReorder.clicked.connect(event_pushButtonConvert_NoReorder)
    MainWindow.pushButton_Convert.clicked.connect(event_pushButtonConvert)
    
    MainWindow.lineEdit_Insert.textEdited.connect(event_textline_InsertBlankPages_textEdited)

    #TriggerEvents
    ##Set LanguageID and correctly set all text
    event_radioButtonLanguage(MainWindow.radioButton_Language_Catala, 0)
    event_radioButtonLanguage(MainWindow.radioButton_Language_Castellano, 1)
    event_radioButtonLanguage(MainWindow.radioButton_Language_English, 2)

    event_textline_InsertBlankPages_textEdited()


    if(AutoTestMode):
        AutoTest()
        return


    DEBUG("A")
    #SHOW WINDOW
    MainWindow.show()
    app.exec()
    DEBUG("B")


#=============================================================================================

Init()

