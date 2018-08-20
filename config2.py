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
  # To be completed...
  imgIsCuraOpened = 'CuraOpened' + version_str + '.png'
  imgPreparebtn = 'Preparebtn' + version_str + '.png'
  imgReady2print = 'Ready2print' + version_str + '.png'
  imgLayerView = 'Layerview' + version_str + '.png'
  imgPrintjobsent = 'Printjobsent' + version_str + '.png'
  imgViewLabel = 'Viewlabel' + version_str + '.png'
  imgcleanBP + 'CleanBP' + version_str + '.png'

  return


def OpenCura(version):
  """ Funtion which opens the corresponding (and installed) Cura version """
  pya.press('win')
  time.sleep(1)
  pya.typewrite(version)
  pya.press('enter')

  return


def findTarget(TargetImg,Q = (0, 0, width, height)):
  """ Find the picture and measure the time it takes """
  tinit = time.time()
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
  """ To opena  project file / gcode already located in the default open folder (Downloads in this case) """
  pya.hotkey('ctrl', 'o')
  time.sleep(1)
  pya.typewrite(name)
  time.sleep(0.5)
  pya.hotkey('enter')

  if name.endswith('.3mf'):
      pya.hotkey('enter')
      time.sleep(0.5)
      pya.hotkey('enter')

  return

def MaxScreen():
    for i in range(0, 2, 1):
        pya.hotkey('win', 'up')
        time.sleep(0.5)
    return