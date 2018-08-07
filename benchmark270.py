#Cura Benchmark Test
import time
import pyautogui as pya
import config2 as C2

pya.hotkey('win', 'd') # Minimize all windows and show desktop
width, height = pya.size()  #1900x1080
print("Screen size: ", width, "x", height)

# ###### Coordinates in screen ######
#
# 0,0       X increases -->
# +---------------------------+
# |                           | Y increases
# |                           |     |
# |   1920 x 1080 screen      |     |
# |                           |     V
# |                           |
# |                           |
# +---------------------------+ 1919, 1079



def findtarget(targetImg,a=0,b=0,c=width,d=height):
    result = None
    #print(targetImg, '',a,'',b,'',c,'',d)
    while result is None:
        #print('inaisw rwda')
        result = pya.locateCenterOnScreen(targetImg, region=(a,b,c,d))
        continue
    return result

#File creation
f = open('ResultsCuraBenchmark.txt','a')
f.write('Test for Cura 2.7 started...')
f.write('\n')


# #################################
# ###### Step 1 - Open Cura #######
# #################################
print('Test started...')

#Store shared pict as a variable
targetImg = 'Cura_logo2.PNG'  #Target Image

#Hotkeys to open cura
pya.hotkey('win')  #Press Windows button
pya.typewrite('Cura 2') #Write Cura on the search bar
pya.hotkey('enter') #Press enter to open Cura

# print("Start time: ",t0)
t0 = time.time()
findtarget(targetImg, 0,0,width//4,height//4)
t1 = time.time()
# print("End time: ",t1)
print("---> Time to open Cura is: ", (t1-t0))
f.write("---> Time to open Cura is: " +  str((t1-t0)))
f.write('\n')


pya.hotkey('alt', 'space')  #Maximize Cura window
pya.hotkey('x')

pya.alert('Disable automatic slicing and press OK to continue')
pya.alert('Connect to the printer and press OK to continue')

pya.hotkey('alt', 'space')  #Maximize Cura window
pya.hotkey('x')


time.sleep(3)
# #######################################
# ###### Step 2 - Drag N Drop .stl ######
# #######################################

pya.hotkey('win', 'right')  #Resize Cura to half and anchor to the right side of the screen
time.sleep(0.5)
pya.hotkey('esc') # Discard window suggestions for the other half of the screen

file_location = findtarget('file_to_drag2.PNG',0,height//5,width//2,height//2)
print('File location found: ', file_location)

#Store target pict as a variable
targetImg = 'prepare.png'  #Target Image
result = None

# Position the cursor over the file and drag it to Cura
pya.moveTo(file_location[0], file_location[1])
time.sleep(0.5)
pya.dragTo(width*3//5, height//2, button='left',duration=1)

# print("Start time: ",t0)
t0 = time.time()
DnD_result = findtarget('prepare.png',width*9//10,height*8//10,width,height)
t1 = time.time()
# print("End time: ",t1)
print("---> Time to Drag n Drop is: ", (t1-t0))
f.write("---> Time to Drag n Drop is: "+ str((t1-t0)))
f.write('\n')


# #################################
# ###### Step 3 - Slice file ######
# #################################
print('Step 3 - Slice file')

#pya.click(width*3//4, height//2) #Click on Cura app to set it as current window
pya.hotkey('win', 'up')
time.sleep(1)
pya.hotkey('win', 'up')
pya.click()


# Find location of prepare button and click it
prepare_location = findtarget('prepare.png', width*7//10,height*8//10,width*8//10,height*9//10)
print('Prepare button found: ', prepare_location)

# Click Prepare button
pya.click(prepare_location[0], prepare_location[1])
# print("Start time: ",t0)
t0 = time.time()
findtarget('print_over_network.png', width*7//10,height*8//10,width*8//10,height*9//10)
t1 = time.time()
#print("End time: ",t1)
print("---> Time to slice the '.stl' is: ", (t1-t0))
f.write("---> Time to slice the '.stl' is: " + str((t1-t0)))
f.write('\n')

# #################################
# ###### Step 4 - Layer view ######
# #################################
time.sleep(3)
#Select Layer view
targetImg = 'Layerview2_7.PNG'  #Target Image

pya.click(width//15,height//22)
pya.hotkey('down')
pya.hotkey('down')
pya.hotkey('down')
pya.hotkey('enter')

# print("Start time: ",t0)
t0 = time.time()
findtarget(targetImg, width//5,height//3,width//3,height)
t1 = time.time()
#print("End time: ",t1)
print("---> Time to show Layer view is: ", (t1-t0))
f.write("---> Time to show Layer view is: " + str((t1-t0)))
f.write('\n')

#Select Layer view
pya.click(width//15,height//22)
time.sleep(1)
pya.hotkey('down')
time.sleep(0.5)
pya.hotkey('enter')



# ######################################
# ###### Step 5  - Send print job ######
# ######################################

# Find location of print over network button and click it
print_netw_location = findtarget('print_over_network.png')
print('Print over network button found: ', print_netw_location)

targetImg = 'printing2_7.PNG'  # Target Image
pya.click(print_netw_location[0], print_netw_location[1])

# print("Start time: ",t0)
t0 = time.time()
findtarget(targetImg,width*9//10,height*8//10,width,height)
t1 = time.time()
#print("End time: ",t1)
print("---> Time to send print over network is: ", (t1-t0))
f.write("---> Time to send print over network is: "+ str((t1-t0)))
f.write('\n')

pya.alert('Abort current printjob and reprinting from printer and press OK to continue')



# #################################
# ######  Applying preconds #######
# #################################
print("Preparing preconditions")

#Go to BP screen
BPview_locat = findtarget('BPview.PNG',0,0,width*2//10,height*2//10)
print("BPview_locat: ", BPview_locat)
pya.moveTo(BPview_locat[0],BPview_locat[1])
pya.click(BPview_locat[0],BPview_locat[1])

#Clean buildplate
pya.hotkey('ctrl','n')
time.sleep(2)
pya.hotkey('enter')

# #Select next printer
# changeptr_locat = findtarget('ChangePtr.PNG',width * 9 // 10, 0, width, height *2 // 10)
# pya.click(changeptr_locat[0],changeptr_locat[1])
# time.sleep(1)
# pya.hotkey('down')
# time.sleep(0.5)
# pya.hotkey('down')
# time.sleep(0.5)
# pya.hotkey('enter')


# #################################
# ###### Step 6 - Open gcode ######
# #################################
print("Step 6 - Open gcode")
time.sleep(3)



pya.hotkey('ctrl', 'o')
time.sleep(2)
pya.typewrite('TEST.gcode')
time.sleep(1)
pya.hotkey('enter')


## Load g-code
# print("Start time: ",t0)
t0 = time.time()
print_locat = findtarget('gcodeloaded.PNG',width*8//10,height*8//10,width,height)
t1 = time.time()
#print("End time: ",t1)
print("---> Time to load the gcode is: ", (t1-t0))
f.write("---> Time to load the gcode is: "+ str((t1-t0)))
f.write('\n')


# #####################################
# ###### Step 7 - Send print job ######
# #####################################

targetImg = 'printing2_7.PNG'  # Target Image
pya.click(print_locat[0],print_locat[1])
t0 = time.time()
findtarget(targetImg,width*9//10,height*8//10,width,height)
t1 = time.time()
#print("End time: ",t1)
print("---> Time to send the gcode printjob is: ", (t1-t0))
f.write("---> Time to send the gcode printjob is: "+ str((t1-t0)))
f.write('\n')

pya.alert('Abort current printjob from printer and press OK to continue')


# #################################
# ######  Applying preconds #######
# #################################
print("Preparing preconditions")

#Go to BP screen
BPview_locat = findtarget('BPview.PNG',0,0,width*2//10,height*2//10)
print("BPview_locat: ", BPview_locat)
pya.moveTo(BPview_locat[0],BPview_locat[1])
pya.click(BPview_locat[0],BPview_locat[1])

#Clean buildplate
pya.hotkey('ctrl','n')
time.sleep(2)
pya.hotkey('enter')

#Select Layer view
pya.click(width//15,height//22)
time.sleep(1)
pya.hotkey('down')
time.sleep(0.5)
pya.hotkey('enter')

# #Select next printer
# pya.click(changeptr_locat[0],changeptr_locat[1])
# time.sleep(1)
# pya.hotkey('down')
# time.sleep(0.5)
# pya.hotkey('down')
# time.sleep(0.5)
# pya.hotkey('down')
# time.sleep(0.5)
# pya.hotkey('enter')

# ########################################
# ###### Step 8 - Open project file ######
# ########################################
print("Step 8 - Open project file")
time.sleep(3)

pya.moveTo(BPview_locat[0],BPview_locat[1])
pya.click(BPview_locat[0],BPview_locat[1])
pya.hotkey('ctrl','n')
time.sleep(2)
pya.hotkey('enter')
pya.hotkey('ctrl', 'o')
time.sleep(2)
pya.typewrite('TEST.3mf')
time.sleep(1)
pya.hotkey('enter')
time.sleep(1)
pya.hotkey('enter')



# #################################
# ###### Step 3 - Slice file ######
# #################################
print('Step 3 - Slice file')

# Click Prepare button
pya.click(prepare_location[0], prepare_location[1])
# print("Start time: ",t0)
t0 = time.time()
findtarget('print_over_network.png', width*7//10,height*8//10,width*8//10,height*9//10)
t1 = time.time()
#print("End time: ",t1)
print("---> Time to slice the project file is: ", (t1-t0))
f.write("---> Time to slice the project file is: "+ str((t1-t0)))
f.write('\n')


# #####################################
# ###### Step 9 - Send print job ######
# #####################################
targetImg = 'printing2_7.PNG'  # Target Image
pya.click(print_locat[0],print_locat[1])
t0 = time.time()
findtarget(targetImg,width*9//10,height*8//10,width,height)
t1 = time.time()
#print("End time: ",t1)
print("---> Time to send the project printjob is: ", (t1-t0))
f.write("---> Time to send the project printjob is: "+ str((t1-t0)))
f.write('\n')
f.write('\n')

f.close()

pya.alert("Test finished. Check CuraBenchmark.txt file for results, OK?")