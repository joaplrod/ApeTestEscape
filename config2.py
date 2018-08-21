import pyautogui as pya
import time

width, height = pya.size()

#       ###################
#       #### VARIABLES ####
#       ###################


# Quadrants locations
Q1 = [width // 2, 0, width // 2, height // 2]
Q2 = [0, 0, width // 2, height //2]
Q3 = [0, height // 2, width // 2, height]
Q4 = [width // 2, height // 2, width, height]
Q5 = [ width // 3, 0, width * 2 // 3, height // 2]
Q6 = [ width // 3, height // 2, width * 2 // 3, height]
Q7 = [width // 2, height // 3, width, height * 2 // 3]
Q8 = [0, height // 3, width // 2, height * 2 // 3]


# Images variables
imgIsCuraOpened = None
imgPreparebtn = None
imgReady2print = None
imgLayerView = None
imgPrintjobsent = None
imgViewLabel = None
imgcleanBP = None

#Same DragnDrop img for all versions
Img_file2drag = r'C:\Users\System-Testing\PycharmProjects\CuraBenchmark\file_to_drag2.PNG'



#       ###################
#       #### FUNCTIONS ####
#       ###################


def LoadVariables(version):
  """ Function to load the proper images and variables depending on the Cura version """
  version_str = version.replace(".","")
  global imgIsCuraOpened, imgPreparebtn, imgReady2print, imgLayerView, imgPrintjobsent, imgViewLabel, imgcleanBP, imgobjectpos

  imgIsCuraOpened = r'./Pictures/' + version_str + '/' + 'CuraOpened.png'
  imgPreparebtn = r'./Pictures/' + version_str + '/' + 'Preparebtn.png'
  imgReady2print = r'./Pictures/' + version_str + '/' + 'Ready2print.png'
  imgLayerView = r'./Pictures/' + version_str + '/' + 'Layerview.png'
  imgPrintjobsent = r'./Pictures/' + version_str + '/' + 'Printjobsent.png'
  imgViewLabel = r'./Pictures/' + version_str + '/' + 'Viewlabel.png'
  imgcleanBP = r'./Pictures/' + version_str + '/' + 'CleanBP.png'
  return

def LoadAdvanceVariables(version):
  """ Function to load the proper images and variables depending on the Cura version """
  version_str = version.replace(".","")

  global imgIsCuraOpened, imgPreparebtn, imgReady2print, imgobjectpos, imgrotatebtn, imgrotateline, imgmirrorbtn, imgmirrorline, imgmovebtn, imgmoveline

  imgIsCuraOpened = r'./Pictures/' + version_str + '/' + 'CuraOpened.png'
  imgPreparebtn = r'./Pictures/' + version_str + '/' + 'Preparebtn.png'
  imgReady2print = r'./Pictures/' + version_str + '/' + 'Ready2print.png'
  imgobjectpos = r'./Pictures/' + version_str + '/' + 'objectpos.png'
  imgrotatebtn = r'./Pictures/' + version_str + '/' + 'rotatebtn.png'
  imgrotateline = r'./Pictures/' + version_str + '/' + 'rotateline.png'
  imgmirrorbtn = r'./Pictures/' + version_str + '/' + 'mirrorbtn.png'
  imgmirrorline = r'./Pictures/' + version_str + '/' + 'mirrorline.png'
  imgmovebtn = r'./Pictures/' + version_str + '/' + 'movebtn.png'
  imgmoveline = r'./Pictures/' + version_str + '/' + 'moveline.png'
  return


def OpenCura(version):
  """ Funtion which opens the corresponding (and installed) Cura version """
  pya.press('win')
  time.sleep(1)
  pya.typewrite("cura " + version)
  time.sleep(1.5)
  pya.press('enter')
  return


def findTarget(TargetImg,Q = (0, 0, width, height)):
  """ Find the picture and measure the time it takes """
  tinit = time.time()
  Locat_n_Time = None
  while(Locat_n_Time is None):
    Locat_n_Time = pya.locateCenterOnScreen(TargetImg,region=(Q))
  Locat_n_Time += ((time.time() - tinit),)
  return Locat_n_Time


def cleanBP():
  """ Cleans the build plate of any model and moves the cursor to the midle of the screen """
  pya.hotkey('ctrl', 'n')
  pya.locateCenterOnScreen(imgcleanBP)
  pya.hotkey('enter')
  time.sleep(1)
  pya.moveTo(width // 2, height // 2)
  return


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
    return

def MaxScreen():
    """ Maximizes the front window """
    for i in range(0, 2, 1):
        pya.hotkey('win', 'up')
        time.sleep(1)
    return

def MultiModel(n):
    """ Multiplies the current model 'n' times """
    pya.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pya.hotkey('ctrl', 'm')
    time.sleep(0.5)
    pya.typewrite(str(n))
    time.sleep(0.5)
    pya.hotkey('enter')
    return




def Chose6Models(object_pos):
    """ It choses 6 objects of the 20 multiplied objects (model dependent) """
    pya.keyDown('shift')
    pya.click((object_pos[0] - 0), (object_pos[1] - 0))
    time.sleep(0.5)
    pya.click((object_pos[0] - 50), (object_pos[1] - 0))
    time.sleep(0.5)
    pya.click((object_pos[0] - 50), (object_pos[1] - 15))
    time.sleep(0.5)
    pya.click((object_pos[0] - 50), (object_pos[1] - 30))
    time.sleep(0.5)
    pya.click((object_pos[0] - 100), (object_pos[1] - 0))
    time.sleep(0.5)
    pya.click((object_pos[0] - 100), (object_pos[1] - 15))
    pya.keyUp('shift')
    return