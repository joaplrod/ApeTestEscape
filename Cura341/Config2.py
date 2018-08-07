import pyautogui as pya

width, height = pya.size()
printerAddress = '10.183.1.81'
printHead = '0'
printCoreId = '0'

kid = "043582c98c4df1282385e6e92a0f3159"
key = "73cafa9a9ce3e58caa3f7d7d62b78b216cedb8e53011f9b9952757bcdfafe64a"


LowerBed = {"x": 0, "y": 215, "z": 310}

RaiseBed ={"x": 0,  "y": 215,  "z": 10}

LVal = {
  "hue": 0,
  "saturation": 0,
  "value": 0
}

def matmaker(W,H,fW,fH,sW,sH):
  #width, height = pya.size()
  k = 0
  if W == fW:
    fW = W+1
    sW = 1
  if H == fH:
    fH = H+1
    sH = 1
  colormat = []
  for i in range(W, fW, sW):
    for j in range(H, fH, sH):
      colormat.append(pya.pixel(i, j))
      k += 1
  return colormat



def findTarget(TargetImg,a=0,b=0,c=width,d=height):
  result = None
  #print(str(TargetImg),' ',str(a),' ', str(b),' ', str(c),' ', str(d))
  while result is None:
      result = pya.locateCenterOnScreen(TargetImg,region=(a,b,c,d))
  return result