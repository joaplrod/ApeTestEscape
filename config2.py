import pyautogui as pya
import time, os

width, height = pya.size()

#       ###################
#       #### VARIABLES ####
#       ###################


# Quadrants locations
Q1 = [width // 2, 0, width // 2, height // 2]
Q2 = [0, 0, width // 2, height // 2]
Q3 = [0, height // 2, width // 2, height]
Q4 = [width // 2, height // 2, width, height]
Q5 = [width // 3, 0, width * 2 // 3, height // 2]
Q6 = [width // 3, height // 2, width * 2 // 3, height]
Q7 = [width // 2, height // 3, width, height * 2 // 3]
Q8 = [0, height // 3, width // 2, height * 2 // 3]


#       ###################
#       #### FUNCTIONS ####
#       ###################


def LoadVariables(version, extension = '.png'):
    """ Function to load the proper images and variables depending on the
     Cura version and the image extension (.png by default) """
    version_str = version.replace(".", "")
    global imgIsCuraOpened, imgPreparebtn, imgReady2print, imgLayerView, imgPrintjobsent, \
        imgViewLabel, imgcleanBP, imgobjectpos, imgfile2drag

    imgIsCuraOpened = r'./Pictures/' + version_str + '/' + 'CuraOpened'+ extension
    imgPreparebtn = r'./Pictures/' + version_str + '/' + 'Preparebtn'+ extension
    imgReady2print = r'./Pictures/' + version_str + '/' + 'Ready2print'+ extension
    imgLayerView = r'./Pictures/' + version_str + '/' + 'Layerview'+ extension
    imgPrintjobsent = r'./Pictures/' + version_str + '/' + 'Printjobsent'+ extension
    imgViewLabel = r'./Pictures/' + version_str + '/' + 'Viewlabel'+ extension
    imgcleanBP = r'./Pictures/' + version_str + '/' + 'CleanBP' + extension

    imgfile2drag = r'./Pictures/' + version_str + '/' + 'file_to_drag' + extension

def LoadAdvanceVariables(version, extension = '.png'):
    """ Function to load the proper images and variables depending on the
    Cura version and the image extension (.png by default)"""
    version_str = version.replace(".", "")

    global imgIsCuraOpened, imgPreparebtn, imgReady2print, imgobjectpos, imgrotatebtn, \
        imgrotateline, imgmirrorbtn, imgmirrorline, imgmovebtn, imgmoveline, imgDnD3

    imgIsCuraOpened = r'./Pictures/' + version_str + '/' + 'CuraOpened' + extension
    imgPreparebtn = r'./Pictures/' + version_str + '/' + 'Preparebtn' + extension
    imgReady2print = r'./Pictures/' + version_str + '/' + 'Ready2print' + extension
    imgobjectpos = r'./Pictures/' + version_str + '/' + 'objectpos' + extension
    imgrotatebtn = r'./Pictures/' + version_str + '/' + 'rotatebtn' + extension
    imgrotateline = r'./Pictures/' + version_str + '/' + 'rotateline' + extension
    imgmirrorbtn = r'./Pictures/' + version_str + '/' + 'mirrorbtn' + extension
    imgmirrorline = r'./Pictures/' + version_str + '/' + 'mirrorline' + extension
    imgmovebtn = r'./Pictures/' + version_str + '/' + 'movebtn' + extension
    imgmoveline = r'./Pictures/' + version_str + '/' + 'moveline' + extension
    imgDnD3 = r'./Pictures/' + version_str + '/' + 'DnD3' + extension

def LoadExpertVariables(version, extension = '.png'):
    """ Function to load the proper images and variables depending on the
    Cura version and the image extension (.png by default)"""
    version_str = version.replace(".", "")

    global imgIsCuraOpened, imgPreparebtn, imgReady2print, imgexptest, \
        imgcustombtn, imgallsetbtn, imgfuzsk, imgtextbx, imgViewLabel, \
        imgLayerView, imgresetcustomsett, imgrecombtn

    imgIsCuraOpened = r'./Pictures/' + version_str + '/' + 'CuraOpened' + extension
    imgPreparebtn = r'./Pictures/' + version_str + '/' + 'Preparebtn' + extension
    imgReady2print = r'./Pictures/' + version_str + '/' + 'Ready2print' + extension
    imgViewLabel = r'./Pictures/' + version_str + '/' + 'ViewLabel' + extension
    imgLayerView = r'./Pictures/' + version_str + '/' + 'Layerview' + extension
    imgexptest = r'./Pictures/' + version_str + '/' + 'ExpTest' + extension
    imgcustombtn = r'./Pictures/' + version_str + '/' + 'custombtn' + extension
    imgallsetbtn = r'./Pictures/' + version_str + '/' + 'allsetbtn' + extension
    imgfuzsk = r'./Pictures/' + version_str + '/' + 'fuzsk' + extension
    imgtextbx = r'./Pictures/' + version_str + '/' + 'textbox' + extension
    imgresetcustomsett = r'./Pictures/' + version_str + '/' + 'resetcustomsett' + extension
    imgrecombtn = r'./Pictures/' + version_str + '/' + 'recombtn' + extension

def OpenCura(version):
    """ Funtion which opens the corresponding (and installed) Cura version """
    pya.press('win')
    time.sleep(1)
    pya.typewrite("cura " + version)
    time.sleep(1.5)
    pya.press('enter')


def findTarget(TargetImg, Q=(0, 0, width, height)):
    """ Find the picture and measure the time it takes """
    tinit = time.time()
    Locat_n_Time = None
    print('entered in the loop')
    while (Locat_n_Time is None):
        Locat_n_Time = pya.locateCenterOnScreen(TargetImg, region=(Q))
    Locat_n_Time += ((time.time() - tinit),)
    return Locat_n_Time


def layerviewOnOff(mode):
    """ Switches LayerView ON or OFF depending on the parameter"""
    layerview = findTarget(imgViewLabel, Q2)
    pya.click(layerview[0], layerview[1])
    time.sleep(1)

    pya.hotkey('down')
    time.sleep(0.5)
    if(mode.lower() == "on"):
        for i in range(0, 2, 1):
            pya.hotkey('down')
            time.sleep(0.5)
    pya.hotkey('enter')

def cleanBP():
    """ Cleans the build plate of any model and moves the cursor to the midle of the screen """
    pya.hotkey('ctrl', 'n')
    pya.locateCenterOnScreen(imgcleanBP)
    pya.hotkey('enter')
    time.sleep(1)
    pya.moveTo(width // 2, height // 2)


def OpenFile(name):
    """ To open a project file / gcode already located in the default open folder (Downloads in this case) """
    pya.hotkey('ctrl', 'o')
    time.sleep(1)
    pya.typewrite(name)
    time.sleep(1.5)
    pya.hotkey('enter')

    if name.endswith('.3mf'):
        pya.hotkey('enter')
        time.sleep(1)
        pya.hotkey('enter')


def MaxScreen():
    """ Maximizes the front window """
    for i in range(0, 2, 1):
        pya.hotkey('win', 'up')
        time.sleep(1)


def MultiModel(n):
    """ Multiplies the current model 'n' times """
    pya.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pya.hotkey('ctrl', 'm')
    time.sleep(0.5)
    pya.typewrite(str(n))
    time.sleep(0.5)
    pya.hotkey('enter')


def Chose6Models(object_pos):
    """ It choses 6 objects of the 20 multiplied objects (model dependent) """
    pya.keyDown('shift')
    pya.click((object_pos[0] - 0), (object_pos[1] - 0))
    time.sleep(0.8)
    pya.click((object_pos[0] - 50), (object_pos[1] - 0))
    time.sleep(0.8)
    pya.click((object_pos[0] - 50), (object_pos[1] - 15))
    time.sleep(0.8)
    pya.click((object_pos[0] - 50), (object_pos[1] - 30))
    time.sleep(0.8)
    pya.click((object_pos[0] - 100), (object_pos[1] - 0))
    time.sleep(0.8)
    pya.click((object_pos[0] - 100), (object_pos[1] - 15))
    pya.keyUp('shift')

def ClearTextBox(btn_locat):
    pya.click(btn_locat[0] - 200, btn_locat[1])
    time.sleep(1)
    pya.hotkey('ctrl', 'a')
    time.sleep(1)

def TypeTextinTextBox(sentence, btn_locat):
    pya.typewrite(sentence[0], interval=0.8)
    time.sleep(1)
    pya.click(btn_locat[0] - 200, btn_locat[1])
    time.sleep(1)
    pya.typewrite(sentence[1:], interval=0.5)
    
def ResetExtraset():
    custombtn = findTarget(imgcustombtn, (width *2 // 3, 0, width, height))
    #custombtn = findTarget(imgcustombtn)
    pya.click(custombtn[0], custombtn[1])
    profilebtn = findTarget(imgresetcustomsett, (width *2 // 3, 0, width, height))
    pya.click(profilebtn[0], profilebtn[1])
    time.sleep(1)
    pya.hotkey('d')

    # recombtn = findTarget(imgrecombtn,Q7)
    # pya.click(recombtn[0], recombtn[1])

def CloseCura():
    pya.hotkey('alt','F4')
    pya.hotkey('enter')