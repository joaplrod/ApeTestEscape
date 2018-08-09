#Cura Benchmarkt
import time
import pyautogui as pya
import Config2 as C2


width, height = pya.size()



width, height = pya.size()  #1900x1080
print(pya.size())

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


print("Test started...")

##########################
### Step 1 - Open Cura ###
##########################
time.sleep(5)

pya.hotkey('win','d')
pya.click(width//2, height //2)

#Open Cura programe
pya.press('win')
time.sleep(0.5)

#pya.typewrite('cura 3.4.1')
pya.typewrite('cura 3.0.4')

time.sleep(0.5)
needleImage = 'CuraOpened.png'   #Image that must be search
pya.press('enter')

t0 = time.time()
C2.findTarget(needleImage,0,0,width//2,height//2)
t1 = time.time()
print("Time to open Cura is: ", (t1-t0))
tstep1 = t1-t0

pya.alert(tstep1)

pya.hotkey('win','up')
time.sleep(0.5)
pya.hotkey('win','up')
time.sleep(0.5)


#Step 2 - Drag N Drop .stl
print('Step 2 - Drag N Drop .stl')
time.sleep(1)
pya.hotkey('win','right')
time.sleep(0.5)
pya.hotkey('esc')

needleImage = r'C:\Users\System-Testing\PycharmProjects\CuraBenchmark\file_to_drag2.PNG'

file_location = C2.findTarget(needleImage, 0, 0, width//2, height//2)
print('File location found: ', file_location)


# Position the cursor over the file and drag it to Cura
pya.moveTo(file_location[0], file_location[1])
time.sleep(0.5)
pya.dragTo(width*3//5, height//2, button='left',duration=1)
pya.click()

needleImage = 'ModelLoaded.png'   #Image that must be search



t0 = time.time()
prepare_locat = C2.findTarget(needleImage, width//2, height//2,width,height)  #Image which conteins the desired image (needleImage)
t1 = time.time()
print("Time to open an .stl is: ", (t1-t0))
tstep2 = t1-t0

pya.click()
time.sleep(1)
pya.hotkey('win','up')
time.sleep(1)
pya.hotkey('win','up')
time.sleep(0.5)


pya.alert(tstep2)

#Step 3 - Slice file
print('Step 3 - Slice file')
time.sleep(1)

needleImage = 'ready2print.png'
print(prepare_locat)
pya.click(prepare_locat[0],prepare_locat[1]) #Press Prepare (To Slice)

pya.moveTo(width//2,height//2)

t0 = time.time()
C2.findTarget(needleImage,width//2, height//2,width,height)  #Image which contains the desired image (needleImage)
t1 = time.time()
print("Time to Slice the model is: ", (t1-t0))
tstep3 = t1-t0

pya.alert(tstep3)


#Step 4 - Layer view
print('Step 4 - Layer view')
time.sleep(1)

needleImage = 'viewlabel.png'
btn_locat = C2.findTarget(needleImage)
pya.click(btn_locat[0], btn_locat[1])
time.sleep(1)
pya.hotkey('down')
time.sleep(0.5)
pya.hotkey('down')
time.sleep(0.5)
pya.hotkey('down')

needleImage = 'layerview341.png'
pya.hotkey('enter')

t0 = time.time()
C2.findTarget(needleImage,width//2,height//2 ,width,height)  #Image which conteins the desired image (needleImage)
t1 = time.time()
print("Time to show Layer view is: ", (t1 - t0))
tstep4 = t1-t0


pya.click(btn_locat[0], btn_locat[1])
time.sleep(1)
pya.hotkey('down')
pya.hotkey('enter')


pya.alert(tstep4)

#Step 5 - Send printjob
print('Step 5 - Send printjob')
time.sleep(1)

needleImage = 'printjobsent.PNG'
pya.click(prepare_locat[0],prepare_locat[1])

t0 = time.time()
C2.findTarget(needleImage,0, height//2, width//2, height)
t1 = time.time()

print("Send printjob time is: ", (t1 - t0))
tstep5 = t1-t0

pya.alert(tstep5)

#Step 6 - Open G-code
print('Step 6 - Open G-code')
time.sleep(1)

#New project command
pya.hotkey('ctrl', 'n')
time.sleep(1)
pya.hotkey('enter')
time.sleep(1)

pya.moveTo(width//2, height//2)

#Load G-code
#Open File command
pya.hotkey('ctrl', 'o')
time.sleep(1)

pya.typewrite('TEST.gcode')
time.sleep(0.5)
needleImage = 'ready2print.png'
pya.hotkey('enter')

t0 = time.time()
C2.findTarget(needleImage, width//2, height//2,width,height)
t1 = time.time()
print("Time to open a gcode is: ", (t1-t0))
tstep6 = t1-t0

pya.alert(tstep6)

ppup_locat = C2.findTarget('delgcodepup.png',0, height//2, width//2, height)
pya.click(ppup_locat[0], ppup_locat[1])  #To close G-code Details popup

#Step 7 - Send printjob
print('Step 7 - Send printjob')
time.sleep(1)

needleImage = 'printjobsent.PNG'
pya.click(prepare_locat[0],prepare_locat[1])

t0 = time.time()
C2.findTarget(needleImage,0, height//2, width//2, height)
t1 = time.time()
print("Time to send gcode to print is: ", (t1 - t0))
tstep7 = t1-t0

pya.alert(tstep7)

#Step 8 - Open project file
print('Step 8 - Open project file')
time.sleep(1)

needleImage = 'ModelLoaded.png'
pya.moveTo(width//2,height//2)

#New project command
pya.hotkey('ctrl', 'n')
time.sleep(1)
pya.hotkey('enter')
time.sleep(1)
#Open File command
pya.hotkey('ctrl', 'o')
time.sleep(1)

pya.typewrite('TEST.3mf')
time.sleep(0.5)
pya.hotkey('enter')
time.sleep(0.5)
pya.hotkey('enter')
time.sleep(0.5)
pya.hotkey('enter')

t0 = time.time()
prepare_locat = C2.findTarget(needleImage, width//2, height//2,width,height)  #Image which conteins the desired image (needleImage)
t1 = time.time()
print("Time to open a project file is: ", (t1-t0))
tstep8 = t1-t0

#Step 9 - Slice file
print('Step 9 - Slice file')
time.sleep(1)


needleImage = 'ready2print.png'
pya.click(prepare_locat[0],prepare_locat[1]) #Press Prepare (To Slice)
pya.moveTo(width//2,height//2)

t0 = time.time()
C2.findTarget(needleImage,width//2, height//2,width,height)  #Image which conteins the desired image (needleImage)
t1 = time.time()
print("Time to Slice the project file model is: ", (t1-t0))
tstep9 = t1-t0

#Step 10 - Send printjob
print('Step 10 - Send printjob')
time.sleep(1)

pya.click(width // 2, height//2)
needleImage = 'printjobsent.PNG'
pya.click(prepare_locat[0],prepare_locat[1])

t0 = time.time()
C2.findTarget(needleImage,0, height//2, width//2, height)
t1 = time.time()
print("Time to send the printjob is: ", (t1-t0))
tstep10 = t1-t0


#Load info in excel file
f = open(r'C:\Users\System-Testing\PycharmProjects\CuraBenchmark\ResultsCuraBenchmark.txt','a')
f.write('Test for Cura 3.4.1 started...')
f.write('\n')
f.write("---> Time to open Cura is: " +  str((tstep1)))
f.write('\n')
f.write("---> Time to Drag n Drop is: "+ str((tstep2)))
f.write('\n')
f.write("---> Time to slice the '.stl' is: " + str((tstep3)))
f.write('\n')
f.write("---> Time to show Layer view is: " + str((tstep4)))
f.write('\n')
f.write("---> Time to send print over network is: "+ str((tstep5)))
f.write('\n')
f.write("---> Time to send print over network is: "+ str((tstep6)))
f.write('\n')
f.write("---> Time to load the gcode is: "+ str((tstep7)))
f.write('\n')
f.write("---> Time to send the gcode printjob is: "+ str((tstep8)))
f.write('\n')
f.write("---> Time to slice the project file is: "+ str((tstep9)))
f.write('\n')
f.write("---> Time to send the project printjob is: "+ str((tstep10)))
f.write('\n')
f.write('\n')

f.close()

pya.alert("Test is finished...")