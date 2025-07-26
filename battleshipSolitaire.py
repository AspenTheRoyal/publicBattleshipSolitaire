import pyautogui
import pyscreeze
import time
print("MAKE SURE YOU'RE A DOZEN CLICKS DOWN OR THIS WILL NOT WORK")
time.sleep(0.5)
pyautogui.click(200,200)

def numberFinder(x, y):
    zeroImage = "C:/Users/User/Downloads/imagerecognitiontest/0image.png"
    oneImage = "C:/Users/User/Downloads/imagerecognitiontest/1image.png"
    twoImage = "C:/Users/User/Downloads/imagerecognitiontest/2image.png"
    threeImage = "C:/Users/User/Downloads/imagerecognitiontest/3image.png"
    fourImage = "C:/Users/User/Downloads/imagerecognitiontest/4image.png"
    fiveImage = "C:/Users/User/Downloads/imagerecognitiontest/5image.png"
    sixImage = "C:/Users/User/Downloads/imagerecognitiontest/6image.png"
    try:
        pyautogui.locateOnScreen(zeroImage, region=(x,y,35,35), confidence=0.8, grayscale=True)
        return 0
    except pyautogui.ImageNotFoundException:
        print("its not a zero")
    try:
        pyautogui.locateOnScreen(oneImage, region=(x,y,35,35), confidence=0.8, grayscale=True)
        return 1
    except pyautogui.ImageNotFoundException:
        print("its not a one")
    try:
        pyautogui.locateOnScreen(twoImage, region=(x,y,35,35),confidence=0.8,grayscale=True)
        return 2
    except pyautogui.ImageNotFoundException:
        print("its not a two")
    try:
        pyautogui.locateOnScreen(threeImage,region=(x,y,35,35),confidence=0.8,grayscale=True)
        return 3
    except pyautogui.ImageNotFoundException:
        print("its not a three")
    try:
        pyautogui.locateOnScreen(fourImage, region=(x,y,35,35),confidence=0.8,grayscale=True)
        return 4
    except pyautogui.ImageNotFoundException:
        print("its not a four")
    try:
        pyautogui.locateOnScreen(fiveImage,region=(x,y,35,35),confidence=0.8,grayscale=True)
        return 5
    except pyautogui.ImageNotFoundException:
        print("its not a five")
    try:
        pyautogui.locateOnScreen(sixImage,region=(x,y,35,35),confidence=0.7,grayscale=True)
        return 6
    except pyautogui.ImageNotFoundException:
        print("its not a six so you messed up somewhere")
        return False

oneAcross = numberFinder(550,199)
twoAcross = numberFinder(590,199)
threeAcross = numberFinder(620,199)
fourAcross = numberFinder(655,199)
fiveAcross = numberFinder(685,199)
sixAcross = numberFinder(715,199)
sevenAcross = numberFinder(745,199)
eightAcross = numberFinder(777,199)
oneDown = numberFinder(527,230)
twoDown = numberFinder(527,260)
threeDown = numberFinder(527,292)
fourDown = numberFinder(527,325)
fiveDown = numberFinder(527,355)
sixDown = numberFinder(527,385)
sevenDown = numberFinder(527,417)
eightDown = numberFinder(527,450)

def findShape(mainX, mainY, top, left):
    if pyscreeze.pixelMatchesColor(mainX,mainY, (46,46,46), tolerance=5):
        circleImage = "C:/Users/User/Downloads/imagerecognitiontest/circle.png"
        squareImage = "C:/Users/User/Downloads/imagerecognitiontest/square.png"
        rightFacingImage = "C:/Users/User/Downloads/imagerecognitiontest/rightfacing.png"
        leftFacingImage = "C:/Users/User/Downloads/imagerecognitiontest/leftfacing.png"
        topFacingImage = "C:/Users/User/Downloads/imagerecognitiontest/topfacing.png"
        bottomFacingImage = "C:/Users/User/Downloads/imagerecognitiontest/bottomfacing.png"
        try:
            pyautogui.locateOnScreen(circleImage, region=(top,left,33,33),confidence=0.8,grayscale=True)
            return "circle"
        except pyautogui.ImageNotFoundException:
            print("not a circle")
        try:
            pyautogui.locateOnScreen(rightFacingImage, region=(top,left,33,33),confidence=0.8,grayscale=True)
            return "right-facing"
        except pyautogui.ImageNotFoundException:
            print("not a right facing")
        try:
            pyautogui.locateOnScreen(leftFacingImage, region=(top,left,33,33),confidence=0.8,grayscale=True)
            return "left-facing"
        except pyautogui.ImageNotFoundException:
            print("not a left facing")
        try:
            pyautogui.locateOnScreen(topFacingImage, region=(top,left,33,33),confidence=0.8,grayscale=True)
            return "top-facing"
        except pyautogui.ImageNotFoundException:
            print("not a top facing")
        try:
            pyautogui.locateOnScreen(bottomFacingImage, region=(top,left,33,33),confidence=0.8,grayscale=True)
            return "bottom-facing"
        except pyautogui.ImageNotFoundException:
            print("not a bottom facing")
        try:
            pyautogui.locateOnScreen(squareImage, region=(top,left,33,33),confidence=0.4,grayscale=True)
            return "square"
        except pyautogui.ImageNotFoundException:
            print("not a square, somethin is up")
    return "blank"

square1_1 = {"shape": (findShape(570,240,554,225)), "location": ([570,240]), "cornered":(False), "rowH":(oneDown),"rowV":(oneAcross), "squared":(False)}
square2_1 = {"shape": (findShape(601,240,586,225)), "location": ([600,240]), "cornered":(False), "rowH":(twoDown),"rowV":(oneAcross), "squared":(False)}
square3_1 = {"shape": (findShape(632,240,617,225)), "location": ([630,240]), "cornered":(False), "rowH":(threeDown),"rowV":(oneAcross), "squared":(False)}
square4_1 = {"shape": (findShape(663,240,648,225)), "location": ([660,240]), "cornered":(False), "rowH":(fourDown),"rowV":(oneAcross), "squared":(False)}
square5_1 = {"shape": (findShape(694,240,679,225)), "location": ([690,240]), "cornered":(False), "rowH":(fiveDown),"rowV":(oneAcross), "squared":(False)}
square6_1 = {"shape": (findShape(725,240,710,225)), "location": ([720,240]), "cornered":(False), "rowH":(sixDown),"rowV":(oneAcross), "squared":(False)}
square7_1 = {"shape": (findShape(756,240,741,225)), "location": ([750,240]), "cornered":(False), "rowH":(sevenDown),"rowV":(oneAcross), "squared":(False)}
square8_1 = {"shape": (findShape(787,240,772,225)), "location": ([780,240]), "cornered":(False), "rowH":(eightDown),"rowV":(oneAcross), "squared":(False)}
square1_2 = {"shape": (findShape(570,271,554,256)), "location": ([570,270]), "cornered":(False), "rowH":(oneDown),"rowV":(twoAcross), "squared":(False)}
square2_2 = {"shape": (findShape(601,271,586,256)), "location": ([600,270]), "cornered":(False), "rowH":(twoDown),"rowV":(twoAcross), "squared":(False)}
square3_2 = {"shape": (findShape(632,271,617,256)), "location": ([630,270]), "cornered":(False), "rowH":(threeDown),"rowV":(twoAcross), "squared":(False)}
square4_2 = {"shape": (findShape(663,271,648,256)), "location": ([660,270]), "cornered":(False), "rowH":(fourDown),"rowV":(twoAcross), "squared":(False)}
square5_2 = {"shape": (findShape(694,271,679,256)), "location": ([690,270]), "cornered":(False), "rowH":(fiveDown),"rowV":(twoAcross), "squared":(False)}
square6_2 = {"shape": (findShape(725,271,710,256)), "location": ([720,270]), "cornered":(False), "rowH":(sixDown),"rowV":(twoAcross), "squared":(False)}
square7_2 = {"shape": (findShape(756,271,741,256)), "location": ([750,270]), "cornered":(False), "rowH":(sevenDown),"rowV":(twoAcross), "squared":(False)}
square8_2 = {"shape": (findShape(787,271,772,256)), "location": ([780,270]), "cornered":(False), "rowH":(eightDown),"rowV":(twoAcross), "squared":(False)}
square1_3 = {"shape": (findShape(570,302,554,287)), "location": ([570,300]), "cornered":(False), "rowH":(oneDown),"rowV":(threeAcross), "squared":(False)}
square2_3 = {"shape": (findShape(601,302,586,287)), "location": ([600,300]), "cornered":(False), "rowH":(twoDown),"rowV":(threeAcross), "squared":(False)}
square3_3 = {"shape": (findShape(632,302,617,287)), "location": ([630,300]), "cornered":(False), "rowH":(threeDown),"rowV":(threeAcross), "squared":(False)}
square4_3 = {"shape": (findShape(663,302,648,287)), "location": ([660,300]), "cornered":(False), "rowH":(fourDown),"rowV":(threeAcross), "squared":(False)}
square5_3 = {"shape": (findShape(694,302,679,287)), "location": ([690,300]), "cornered":(False), "rowH":(fiveDown),"rowV":(threeAcross), "squared":(False)}
square6_3 = {"shape": (findShape(725,302,710,287)), "location": ([720,300]), "cornered":(False), "rowH":(sixDown),"rowV":(threeAcross), "squared":(False)}
square7_3 = {"shape": (findShape(756,302,741,287)), "location": ([750,300]), "cornered":(False), "rowH":(sevenDown),"rowV":(threeAcross), "squared":(False)}
square8_3 = {"shape": (findShape(787,302,772,287)), "location": ([780,300]), "cornered":(False), "rowH":(eightDown),"rowV":(threeAcross), "squared":(False)}
square1_4 = {"shape": (findShape(570,333,554,318)), "location": ([570,330]), "cornered":(False), "rowH":(oneDown),"rowV":(fourAcross), "squared":(False)}
square2_4 = {"shape": (findShape(601,333,586,318)), "location": ([600,330]), "cornered":(False), "rowH":(twoDown),"rowV":(fourAcross), "squared":(False)}
square3_4 = {"shape": (findShape(632,333,617,318)), "location": ([630,330]), "cornered":(False), "rowH":(threeDown),"rowV":(fourAcross), "squared":(False)}
square4_4 = {"shape": (findShape(663,333,648,318)), "location": ([660,330]), "cornered":(False), "rowH":(fourDown),"rowV":(fourAcross), "squared":(False)}
square5_4 = {"shape": (findShape(694,333,679,318)), "location": ([690,330]), "cornered":(False), "rowH":(fiveDown),"rowV":(fourAcross), "squared":(False)}
square6_4 = {"shape": (findShape(725,333,710,318)), "location": ([720,330]), "cornered":(False), "rowH":(sixDown),"rowV":(fourAcross), "squared":(False)}
square7_4 = {"shape": (findShape(756,333,741,318)), "location": ([750,330]), "cornered":(False), "rowH":(sevenDown),"rowV":(fourAcross), "squared":(False)}
square8_4 = {"shape": (findShape(787,333,771,318)), "location": ([780,330]), "cornered":(False), "rowH":(eightDown),"rowV":(fourAcross), "squared":(False)}
square1_5 = {"shape": (findShape(570,364,554,349)), "location": ([570,360]), "cornered":(False), "rowH":(oneDown),"rowV":(fiveAcross), "squared":(False)}
square2_5 = {"shape": (findShape(601,364,586,349)), "location": ([600,360]), "cornered":(False), "rowH":(twoDown),"rowV":(fiveAcross), "squared":(False)}
square3_5 = {"shape": (findShape(632,364,617,349)), "location": ([630,360]), "cornered":(False), "rowH":(threeDown),"rowV":(fiveAcross), "squared":(False)}
square4_5 = {"shape": (findShape(663,364,648,349)), "location": ([660,360]), "cornered":(False), "rowH":(fourDown),"rowV":(fiveAcross), "squared":(False)}
square5_5 = {"shape": (findShape(694,364,679,349)), "location": ([690,360]), "cornered":(False), "rowH":(fiveDown),"rowV":(fiveAcross), "squared":(False)}
square6_5 = {"shape": (findShape(725,364,710,349)), "location": ([720,360]), "cornered":(False), "rowH":(sixDown),"rowV":(fiveAcross), "squared":(False)}
square7_5 = {"shape": (findShape(756,364,741,349)), "location": ([750,360]), "cornered":(False), "rowH":(sevenDown),"rowV":(fiveAcross), "squared":(False)}
square8_5 = {"shape": (findShape(787,364,772,349)), "location": ([780,360]), "cornered":(False), "rowH":(eightDown),"rowV":(fiveAcross), "squared":(False)}
square1_6 = {"shape": (findShape(570,395,554,380)), "location": ([570,390]), "cornered":(False), "rowH":(oneDown),"rowV":(sixAcross), "squared":(False)}
square2_6 = {"shape": (findShape(601,395,586,380)), "location": ([600,390]), "cornered":(False), "rowH":(twoDown),"rowV":(sixAcross), "squared":(False)}
square3_6 = {"shape": (findShape(632,395,617,380)), "location": ([630,390]), "cornered":(False), "rowH":(threeDown),"rowV":(sixAcross), "squared":(False)}
square4_6 = {"shape": (findShape(663,395,648,380)), "location": ([660,390]), "cornered":(False), "rowH":(fourDown),"rowV":(sixAcross), "squared":(False)}
square5_6 = {"shape": (findShape(694,395,679,380)), "location": ([690,390]), "cornered":(False), "rowH":(fiveDown),"rowV":(sixAcross), "squared":(False)}
square6_6 = {"shape": (findShape(725,395,710,380)), "location": ([720,390]), "cornered":(False), "rowH":(sixDown),"rowV":(sixAcross), "squared":(False)}
square7_6 = {"shape": (findShape(756,395,741,380)), "location": ([750,390]), "cornered":(False), "rowH":(sevenDown),"rowV":(sixAcross), "squared":(False)}
square8_6 = {"shape": (findShape(787,395,772,380)), "location": ([780,390]), "cornered":(False), "rowH":(eightDown),"rowV":(sixAcross), "squared":(False)}
square1_7 = {"shape": (findShape(570,426,554,411)), "location": ([570,420]), "cornered":(False), "rowH":(oneDown),"rowV":(sevenAcross), "squared":(False)}
square2_7 = {"shape": (findShape(601,426,586,411)), "location": ([600,420]), "cornered":(False), "rowH":(twoDown),"rowV":(sevenAcross), "squared":(False)}
square3_7 = {"shape": (findShape(632,426,617,411)), "location": ([630,420]), "cornered":(False), "rowH":(threeDown),"rowV":(sevenAcross), "squared":(False)}
square4_7 = {"shape": (findShape(663,426,648,411)), "location": ([660,420]), "cornered":(False), "rowH":(fourDown),"rowV":(sevenAcross), "squared":(False)}
square5_7 = {"shape": (findShape(694,426,679,411)), "location": ([690,420]), "cornered":(False), "rowH":(fiveDown),"rowV":(sevenAcross), "squared":(False)}
square6_7 = {"shape": (findShape(725,426,710,411)), "location": ([720,420]), "cornered":(False), "rowH":(sixDown),"rowV":(sevenAcross), "squared":(False)}
square7_7 = {"shape": (findShape(756,426,741,411)), "location": ([750,420]), "cornered":(False), "rowH":(sevenDown),"rowV":(sevenAcross), "squared":(False)}
square8_7 = {"shape": (findShape(787,426,772,411)), "location": ([780,420]), "cornered":(False), "rowH":(eightDown),"rowV":(sevenAcross), "squared":(False)}
square1_8 = {"shape": (findShape(570,457,554,442)), "location": ([570,450]), "cornered":(False), "rowH":(oneDown),"rowV":(eightAcross), "squared":(False)}
square2_8 = {"shape": (findShape(601,457,586,442)), "location": ([600,450]), "cornered":(False), "rowH":(twoDown),"rowV":(eightAcross), "squared":(False)}
square3_8 = {"shape": (findShape(632,457,617,442)), "location": ([630,450]), "cornered":(False), "rowH":(threeDown),"rowV":(eightAcross), "squared":(False)}
square4_8 = {"shape": (findShape(663,457,648,442)), "location": ([660,450]), "cornered":(False), "rowH":(fourDown),"rowV":(eightAcross), "squared":(False)}
square5_8 = {"shape": (findShape(694,457,679,442)), "location": ([690,450]), "cornered":(False), "rowH":(fiveDown),"rowV":(eightAcross), "squared":(False)}
square6_8 = {"shape": (findShape(725,457,710,442)), "location": ([720,450]), "cornered":(False), "rowH":(sixDown),"rowV":(eightAcross), "squared":(False)}
square7_8 = {"shape": (findShape(756,457,741,442)), "location": ([750,450]), "cornered":(False), "rowH":(sevenDown),"rowV":(eightAcross), "squared":(False)}
square8_8 = {"shape": (findShape(787,457,772,442)), "location": ([780,450]), "cornered":(False), "rowH":(eightDown),"rowV":(eightAcross), "squared":(False)}

def its80Click():
    x, y = pyautogui.position()
    if pyscreeze.pixelMatchesColor(x, y,(80,80,80),tolerance=5):
        pyautogui.click()
        
def not47DoubleClick():
    x, y = pyautogui.position()
    if pyscreeze.pixelMatchesColor(x, y, (80,80,80),tolerance=5):
        pyautogui.doubleClick()

def moveNothing(direction,amount,click):
    if direction == "across":
        pyautogui.move(0,amount)
    if direction == "down":
        pyautogui.move(amount,0)
    if click == "click":
        pyautogui.click()
    if click == "doubleClick":
        pyautogui.doubleClick()
    if click == "check47":
        not47DoubleClick()
    if click == "80Click":
        its80Click()

def clickAll():
    pyautogui.click(788,210)
    for i in range(8):
        moveNothing("down",-31,"click")
    for i in range(8):
        moveNothing("across",31,"click")

def startingMini(variable,dominant,minority,one,two,three,four):
    its80Click()
    for i in range(3):
        moveNothing(dominant,one,"80Click")
    for i in range(2):
        moveNothing(minority,two,"80Click")
    for i in range(3):
        moveNothing(dominant,three,"80Click")
    pyautogui.moveTo(variable["location"])
    moveNothing(dominant,four,"check47")

def startingHelper(rangeCount,direction,amount,click):
    for i in range(rangeCount):
        moveNothing(direction,amount,click)

def squareHelper(first,second):
    moveNothing(first,-60,"80Click")
    startingHelper(4,first,30,"80Click")
    moveNothing(second,60,"80Click")
    startingHelper(4,first,-30,"80Click")

def squareChecker(variable):
    pyautogui.moveTo(variable["location"])
    pyautogui.move(-30,-30)
    its80Click()
    moveNothing("down",60,"80Click")
    moveNothing("across",60,"80Click")
    moveNothing("across",-60,"80Click")
    pyautogui.moveTo(variable["location"])
    pyautogui.move(-30,0)
    x, y = pyautogui.position()
    if (pyscreeze.pixelMatchesColor(x, y, (179,212,224),tolerance=60) or pyscreeze.pixelMatchesColor((x+60),y,(179,212,224),tolerance=60)) or (variable["rowH"] > 2) or x < 570 or (x+60) < 570:
        squareHelper("across","down")
        pyautogui.move(-30,30)
        not47DoubleClick()
        moveNothing("across",60,"check47")
        return True
    pyautogui.moveTo(variable["location"])
    pyautogui.move(0,-30)
    x, y = pyautogui.position()
    if (pyscreeze.pixelMatchesColor(x,y,(179,212,224),tolerance=60) or pyscreeze.pixelMatchesColor(x,(y+60),(179,212,224),tolerance=60)) or (variable["rowV"] > 2) or y < 240 or (y+60) < 240:
        squareHelper("down","across")
        pyautogui.move(30,-30)
        not47DoubleClick()
        moveNothing("down",60,"check47")
        return True
    return False

def startingFunction(variable):
    if not variable["shape"] == "blank":
        clickAll()
        pyautogui.moveTo(variable["location"])
    if variable["shape"] == "circle":
        moveNothing("down",-30,"80Click")
        moveNothing("across",-30,"80Click")
        startingHelper(2,"down",30,"80Click")
        startingHelper(2,"across",30,"80Click")
        startingHelper(2,"down",-30,"80Click")
    if variable["shape"] == "square":
        variable["squared"] = squareChecker(variable)
    if variable["shape"] == "top-facing":
        pyautogui.move(-30,-60)
        startingMini(variable,"across","down",30,30,-30,-30)
    if variable["shape"] == "left-facing":
        pyautogui.move(-60,30)
        startingMini(variable,"down","across",30,-30,-30,-30)
    if variable["shape"] == "right-facing":
        pyautogui.move(60,30)
        startingMini(variable,"down","across",-30,-30,30,30)
    if variable["shape"] == "bottom-facing":
        pyautogui.move(30,60)
        startingMini(variable,"across","down",-30,-30,30,30)

squares = [square1_1, square2_1, square3_1, square4_1, square5_1, square6_1, square7_1, square8_1, square1_2, square2_2, square3_2, square4_2, 
           square5_2, square6_2, square7_2, square8_2, square1_3, square2_3, square3_3, square4_3, square5_3, square6_3, square7_3, square8_3, 
           square1_4, square2_4, square3_4, square4_4, square5_4, square6_4, square7_4, square8_4, square1_5, square2_5, square3_5, square4_5,
           square5_5, square6_5, square7_5, square8_5, square1_6, square2_6, square3_6, square4_6, square5_6, square6_6, square7_6, square8_6,
           square1_7, square2_7, square3_7, square4_7, square5_7, square6_7, square7_7, square8_7, square1_8, square2_8, square3_8, square4_8,
           square5_8, square6_8, square7_8, square8_8]

for variable in squares:
    startingFunction(variable)
clickAll()
def onlySpotsLeftMini(x,y,direction,variable):
    boats = 0
    blank = 0
    pyautogui.moveTo(x,y)
    for i in range(8):
        moveNothing(direction,30,"no")
        x2, y2 = pyautogui.position()
        if pyscreeze.pixelMatchesColor(x2,y2,(47,47,47),tolerance=5):
            boats = boats + 1
        if pyscreeze.pixelMatchesColor(x2,y2,(80,80,80),tolerance=5):
            blank = blank + 1
    if variable == blank+boats:
        pyautogui.moveTo(x,y)
        startingHelper(8,direction,30,"check47")
        clickAll()
        return 0
    else:
        return variable

def onlySpotsLeftRule(): 
    pyautogui.click(200,200)
    global eightAcross
    global sevenAcross
    global sixAcross
    global fiveAcross
    global fourAcross
    global threeAcross
    global twoAcross
    global oneAcross
    global oneDown
    global twoDown
    global threeDown
    global fourDown
    global fiveDown
    global sixDown
    global sevenDown
    global eightDown
    if eightAcross != 0:
        eightAcross = onlySpotsLeftMini(788,209,"across",eightAcross)
    if sevenAcross != 0:
        sevenAcross = onlySpotsLeftMini(754,209,"across",sevenAcross)
    if sixAcross != 0:
        sixAcross = onlySpotsLeftMini(723,209,"across",sixAcross)
    if fiveAcross != 0:
        fiveAcross = onlySpotsLeftMini(691,209,"across",fiveAcross)
    if fourAcross != 0:
        fourAcross = onlySpotsLeftMini(660,209,"across",fourAcross)
    if threeAcross != 0:
        threeAcross = onlySpotsLeftMini(630,209,"across",threeAcross)
    if twoAcross != 0:
        twoAcross = onlySpotsLeftMini(600,209,"across",twoAcross)
    if oneAcross != 0:
        oneAcross = onlySpotsLeftMini(570,209,"across",oneAcross)
    if oneDown != 0:
        oneDown = onlySpotsLeftMini(535,243,"down",oneDown)
    if twoDown != 0:
        twoDown = onlySpotsLeftMini(535,273,"down",twoDown)
    if threeDown != 0:
        threeDown = onlySpotsLeftMini(535,305,"down",threeDown)
    if fourDown != 0:
        fourDown = onlySpotsLeftMini(535,335,"down",fourDown)
    if fiveDown != 0:
        fiveDown = onlySpotsLeftMini(535,365,"down",fiveDown)
    if sixDown != 0:
        sixDown = onlySpotsLeftMini(535,395,"down",sixDown)
    if sevenDown != 0:
        sevenDown = onlySpotsLeftMini(535,425,"down",sevenDown)
    if eightDown != 0:
        eightDown = onlySpotsLeftMini(535,455,"down",eightDown)

def cornerChecker(variable):
    pyautogui.moveTo(variable["location"])
    x, y = pyautogui.position()
    if pyscreeze.pixelMatchesColor(x,y,(47,47,47),tolerance=5):
        pyautogui.move(-30,-30)
        its80Click()
        moveNothing("down",60,"80Click")
        moveNothing("across",60,"80Click")
        moveNothing("down",-60,"80Click")
        return True
    if not pyscreeze.pixelMatchesColor(x,y,(80,80,80),tolerance=5):
        return True
    return False

def cornerCheckerCool():
    for variable in squares:
        if variable["cornered"] == False:
            variable["cornered"] = cornerChecker(variable)

def if47Addition(variable):
    x, y = pyautogui.position()
    variable2 = variable
    if pyscreeze.pixelMatchesColor(x,y,(47,47,47),tolerance=5):
        variable2 = variable + 1
    return variable2

def blackOrBlank():
    x, y = pyautogui.position()
    blackOrBlankVar = "blank"
    if pyscreeze.pixelMatchesColor(x,y,(47,47,47),tolerance=5):
        blackOrBlankVar = "black"
    return blackOrBlankVar

def acrossFourShipFinder(xHoHo, yHoHo, positionHoHo, direction): 
        if pyscreeze.pixelMatchesColor(602,141,(100,100,100),tolerance=5):
            return
        counterAcross = 0
        counterTempAcross = 0
        allAcrossBoats = 0
        startOfFourThing = 0
        startOfTempFourThing = 0
        pyautogui.moveTo(xHoHo,yHoHo)
        for i in range(8):
            x, y = pyautogui.position()
            if not pyscreeze.pixelMatchesColor(x,y,(127,179,197),tolerance=70):
                counterTempAcross = counterTempAcross + 1
                if counterTempAcross == 4:
                    startOfFourThing = startOfTempFourThing
                if counterTempAcross > counterAcross:
                    counterAcross = counterTempAcross
                if counterTempAcross == 1:
                    startOfTempFourThing = x,y
            else:
                counterTempAcross = 0
            moveNothing(direction,30,"no")
        if counterAcross < 4:
            return
        pyautogui.moveTo(xHoHo,yHoHo)
        for i in range(8):
            allAcrossBoats = if47Addition(allAcrossBoats)
            moveNothing(direction,30,"no")
        pyautogui.moveTo(startOfFourThing)
        selectedAcrossBoats4 = 0
        for i in range(counterAcross):
            selectedAcrossBoats4 = if47Addition(selectedAcrossBoats4)
            moveNothing(direction,30,"no")
        extraAcrossBoats = allAcrossBoats - selectedAcrossBoats4
        if (extraAcrossBoats+4) > positionHoHo:
            return
        pyautogui.moveTo(startOfFourThing)
        if counterAcross == 4: 
            moveNothing(direction,-30,"80Click")
            startingHelper(4,direction,30,"check47")
            moveNothing(direction,30,"80Click")
            return
        if counterAcross == 5:
            acrossBoat1 = blackOrBlank()
            if acrossBoat1 == "black":
                startingHelper(3,direction,30,"check47")
                moveNothing(direction,30,"80Click")
                return
            moveNothing(direction,120,"no")
            acrossBoat5 = blackOrBlank()
            pyautogui.moveTo(startOfFourThing)
            if acrossBoat5 == "black":
                pyautogui.click()
                startingHelper(3,direction,30,"check47")
                return
            startingHelper(3,direction,30,"check47")
        if counterAcross == 6:
            selectedAcrossBoats4 = 0
            for i in range(6):
                selectedAcrossBoats4 = if47Addition(selectedAcrossBoats4)
                moveNothing(direction,30,"no")
            pyautogui.moveTo(startOfFourThing)
            acrossBoat1 = blackOrBlank()
            if acrossBoat1 == "black":
                moveNothing(direction,-30,"80Click")
                startingHelper(4,direction,30,"check47")
                moveNothing(direction,30,"80Click")
                return
            moveNothing(direction,30,"no")
            acrossBoat2 = blackOrBlank()
            moveNothing(direction,90,"no")
            acrossBoat5 = blackOrBlank()
            moveNothing(direction,30,"no")
            acrossBoat6 = blackOrBlank()
            pyautogui.moveTo(startOfFourThing)
            if acrossBoat6 == "black":
                moveNothing(direction,30,"80Click")
                startingHelper(3,direction,30,"check47")
                return
            if selectedAcrossBoats4 == 2:
                if acrossBoat2 == "black" and acrossBoat5 == "black":
                    its80Click()
                    moveNothing(direction,60,"doubleClick")
                    moveNothing(direction,30,"doubleClick")
                    moveNothing(direction,60,"80Click")
                    return
            if selectedAcrossBoats4 == 1:
                if acrossBoat2 == "black":
                    moveNothing(direction,150,"80Click")
                if acrossBoat5 == "black":
                    its80Click()
            if selectedAcrossBoats4 == 4:
                its80Click()
                moveNothing(direction,150,"80Click")
                return
            pyautogui.moveTo(startOfFourThing)
            moveNothing(direction,60,"check47")
            moveNothing(direction,30,"check47")

def fourShipFinder():
    if eightAcross > 3:
        acrossFourShipFinder(780,240,eightAcross,"across")
    if sevenAcross > 3:
        acrossFourShipFinder(750,240,sevenAcross,"across")
    if sixAcross > 3:
        acrossFourShipFinder(720,240,sixAcross,"across")
    if fiveAcross > 3:
        acrossFourShipFinder(690,240,fiveAcross,"across")
    if fourAcross > 3:
        acrossFourShipFinder(660,240,fourAcross,"across")
    if threeAcross > 3:
        acrossFourShipFinder(630,240,threeAcross,"across")
    if twoAcross > 3:
        acrossFourShipFinder(600,240,twoAcross,"across")
    if oneAcross > 3:
        acrossFourShipFinder(570,240,oneAcross,"across")
    if oneDown > 3:
        acrossFourShipFinder(570,240,oneDown,"down")
    if twoDown > 3:
        acrossFourShipFinder(570,270,twoDown,"down")
    if threeDown > 3:
        acrossFourShipFinder(570,300,threeDown,"down")
    if fourDown > 3:
        acrossFourShipFinder(570,330,fourDown,"down")
    if fiveDown > 3:
        acrossFourShipFinder(570,360,fiveDown,"down")
    if sixDown > 3:
        acrossFourShipFinder(570,390,sixDown,"down")
    if sevenDown > 3:
        acrossFourShipFinder(570,420,sevenDown,"down")
    if eightDown > 3:
        acrossFourShipFinder(570,450,eightDown,"down")

def acrossThreeShipFinder(xHeHe, yHeHe, positionHeHe, direction):
    if pyscreeze.pixelMatchesColor(760,141,(100,100,100),tolerance=5) and pyscreeze.pixelMatchesColor(686,135,(100,100,100),tolerance=5):
        return True
    pyautogui.moveTo(xHeHe,yHeHe)
    counterAcross = 0
    counterTempAcross = 0
    selectedAcrossBoats = 0
    startOfThreeThing = 0
    startOfTempThreeThing = 0
    for i in range(8):
        x, y = pyautogui.position()
        if not pyscreeze.pixelMatchesColor(x,y,(127,179,197),tolerance=60):
            counterTempAcross = counterTempAcross + 1
            if counterTempAcross == 3:
                startOfThreeThing = startOfTempThreeThing
            if counterTempAcross > counterAcross:
                counterAcross = counterTempAcross
            if counterTempAcross == 1:
                startOfTempThreeThing = (x,y)
        else:
            counterTempAcross = 0
        moveNothing(direction,30,"no")
    allAcrossBoats = 0
    pyautogui.moveTo(xHeHe,yHeHe)
    for i in range(8):
        allAcrossBoats = if47Addition(allAcrossBoats)
        moveNothing(direction, 30, "no")
    pyautogui.moveTo(startOfThreeThing)
    for i in range(counterAcross):
        selectedAcrossBoats = if47Addition(selectedAcrossBoats)
        moveNothing(direction,30,"no")
    extraAcrossBoats = allAcrossBoats - selectedAcrossBoats
    if ((extraAcrossBoats+3) > positionHeHe):
        return False
    if selectedAcrossBoats > 2:
        return False
    pyautogui.moveTo(startOfThreeThing)
    acrossBoat1 = blackOrBlank()
    if acrossBoat1 == "black":
        startingHelper(2,direction,30,"check47")
        moveNothing(direction,30,"80Click")
        return True
    if counterAcross == 3:
        moveNothing(direction,-30,"no")
        startingHelper(3, direction, 30, "check47")
    if counterAcross == 4:
        moveNothing(direction,90,"no")
        acrossBoat4 = blackOrBlank()
        pyautogui.moveTo(startOfThreeThing)
        if acrossBoat4 == "black":
            its80Click()
            startingHelper(2,direction,30,"check47")
            return True
        startingHelper(2,direction,30,"check47")
    if counterAcross == 5:
        moveNothing(direction,30,"no")
        acrossBoat2 = blackOrBlank()
        moveNothing(direction,60,"no")
        acrossBoat4 = blackOrBlank()
        moveNothing(direction,30,"no")
        acrossBoat5 = blackOrBlank()
        if acrossBoat5 == "black":
            pyautogui.moveTo(startOfThreeThing)
            moveNothing(direction,30,"80Click")
            startingHelper(2,direction,30,"check47")
            return True
        pyautogui.moveTo(startOfThreeThing)
        moveNothing(direction,60,"check47")
        pyautogui.moveTo(startOfThreeThing)
        if selectedAcrossBoats == 1:
            if acrossBoat2 == "black":
                moveNothing(direction,120,"80Click")
                return True
            if acrossBoat4 == "black":
                its80Click()
                return True
        if selectedAcrossBoats == 2:
            if acrossBoat2 == "black" and acrossBoat4 == "black":
                its80Click()
                moveNothing(direction,120,"80Click")
                return True
    if counterAcross == 6:
        moveNothing(direction,30,"no")
        acrossBoat2 = blackOrBlank()
        moveNothing(direction,30,"no")
        acrossBoat3 = blackOrBlank()
        moveNothing(direction,30,"no")
        acrossBoat4 = blackOrBlank()
        moveNothing(direction,30,"no")
        acrossBoat5 = blackOrBlank()
        moveNothing(direction,30,"no")
        acrossBoat6 = blackOrBlank()
        pyautogui.moveTo(startOfThreeThing)
        if acrossBoat6 == "black":
            moveNothing(direction,60,"80Click")
            startingHelper(2,direction,30,"check47")
            return True
        if selectedAcrossBoats == 1:
            if acrossBoat2 == "black":
                moveNothing(direction,60,"doubleClick")
                return True
            if acrossBoat5 == "black":
                moveNothing(direction,120,"doubleClick")
                return True
        if selectedAcrossBoats == 2:
            if acrossBoat2 == "black" and acrossBoat4 == "black":
                pyautogui.click()
                moveNothing(direction,60,"doubleClick")
                moveNothing(direction,60,"click")
                return True
            if acrossBoat3 == "black" and acrossBoat5 == "black":
                moveNothing(direction,30,"click")
                moveNothing(direction,60,"doubleClick")
                moveNothing(direction,60,"click")
                return True
    return False

def threeShipFinder():
    firstThreeComplete = False
    if eightAcross > 2:
        firstThreeComplete = acrossThreeShipFinder(780,240,eightAcross,"across")
    if sevenAcross > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(750,240,sevenAcross,"across")
    if sixAcross > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(720,240,sixAcross,"across")
    if fiveAcross > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(690,240,fiveAcross,"across")
    if fourAcross > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(660,240,fourAcross,"across")
    if threeAcross > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(630,240,threeAcross,"across")
    if twoAcross > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(600,240,twoAcross,"across")
    if oneAcross > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,240,oneAcross,"across")
    if oneDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,240,oneDown,"down")
    if twoDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,270,twoDown,"down")
    if threeDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,300,threeDown,"down")
    if fourDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,330,fourDown,"down")
    if fiveDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,360,fiveDown,"down")
    if sixDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,390,sixDown,"down")
    if sevenDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,420,sevenDown,"down")
    if eightDown > 2 and firstThreeComplete == False:
        firstThreeComplete = acrossThreeShipFinder(570,450,eightDown,"down")
    
def acrossFullThree(xAlpha, yAlpha, direction):
    counterBoatAcross = 0
    counterBoatTempAcross = 0
    startOfBoatTempThreeThing = 0
    startOfBoatThreeThing = 0
    pyautogui.moveTo(xAlpha, yAlpha)
    for i in range(8):
        x, y = pyautogui.position()
        if pyscreeze.pixelMatchesColor(x,y,(47,47,47),tolerance=5):
            counterBoatTempAcross = counterBoatTempAcross + 1
            if counterBoatTempAcross == 3:
                startOfBoatThreeThing = startOfBoatTempThreeThing
            if counterBoatTempAcross > counterBoatAcross:
                counterBoatAcross = counterBoatTempAcross
            if counterBoatTempAcross == 1:
                startOfBoatTempThreeThing = (x,y)
        else:
            counterBoatTempAcross = 0
        moveNothing(direction,30,"no")
    if counterBoatAcross == 3:
        pyautogui.moveTo(startOfBoatThreeThing)
        moveNothing(direction,-30,"80Click")
        moveNothing(direction,120,"80Click")

def fullThreeFinder():
    if eightAcross > 2:
        acrossFullThree(780,240,"across")
    if sevenAcross > 2:
        acrossFullThree(750,240,"across")
    if sixAcross > 2:
        acrossFullThree(720,240,"across")
    if fiveAcross > 2:
        acrossFullThree(690,240,"across")
    if fourAcross > 2:
        acrossFullThree(660,240,"across")
    if threeAcross > 2:
        acrossFullThree(630,240,"across")
    if twoAcross > 2:
        acrossFullThree(600,240,"across")
    if oneAcross > 2:
        acrossFullThree(570,240,"across")
    if oneDown > 2:
        acrossFullThree(570,240,"down")
    if twoDown > 2:
        acrossFullThree(570,270,"down")
    if threeDown > 2:
        acrossFullThree(570,300,"down")
    if fourDown > 2:
        acrossFullThree(570,330,"down")
    if fiveDown > 2:
        acrossFullThree(570,360,"down")
    if sixDown > 2:
        acrossFullThree(570,390,"down")
    if sevenDown > 2:
        acrossFullThree(570,420,"down")
    if eightDown > 2:
        acrossFullThree(570,450,"down")

def acrossTwoShipFinder(xHiHi, yHiHi, positionHiHi, direction):
    if pyscreeze.pixelMatchesColor(578,169,(100,100,100),tolerance=5) and pyscreeze.pixelMatchesColor(621,166,(100,100,100),tolerance=5) and pyscreeze.pixelMatchesColor(671,164,(100,100,100),tolerance=5):
        return False
    pyautogui.moveTo(xHiHi,yHiHi)
    counterAcross = 0
    counterTempAcross = 0
    selectedAcrossBoats = 0
    startOfTwoThing = 0
    startOfTempTwoThing = 0
    for i in range(8):
        x, y = pyautogui.position()
        if not pyscreeze.pixelMatchesColor(x,y,(127,179,197),tolerance=70):
            counterTempAcross = counterTempAcross + 1
            if counterTempAcross == 2:
                startOfTwoThing = startOfTempTwoThing
            if counterTempAcross > counterAcross:
                counterAcross = counterTempAcross
            if counterTempAcross == 1:
                startOfTempTwoThing = (x,y)
        else:
            counterTempAcross = 0
        moveNothing(direction,30,"no")
    allAcrossBoats = 0
    pyautogui.moveTo(xHiHi,yHiHi)
    for i in range(8):
        allAcrossBoats = if47Addition(allAcrossBoats)
        moveNothing(direction, 30, "no")
    pyautogui.moveTo(startOfTwoThing)
    for i in range(counterAcross):
        selectedAcrossBoats = if47Addition(selectedAcrossBoats)
        moveNothing(direction,30,"no")
    extraAcrossBoats = allAcrossBoats - selectedAcrossBoats
    if ((extraAcrossBoats+2) > positionHiHi) or (selectedAcrossBoats > 1):
        return False
    pyautogui.moveTo(startOfTwoThing)
    if counterAcross == 2:
        moveNothing(direction,-30,"no")
        startingHelper(2,direction,30,"check47")
        return True
    if counterAcross == 3:
        acrossBoat1 = blackOrBlank()
        if acrossBoat1 == "black":
            moveNothing(direction,30,"check47")
            moveNothing(direction,30,"click")
            return True
        moveNothing(direction,60,"no")
        acrossBoat3 = blackOrBlank()
        if acrossBoat3 == "black":
            pyautogui.moveTo(startOfTwoThing)
            pyautogui.click()
            moveNothing(direction,30,"check47")
            return True
        moveNothing(direction,-30,"check47")
    return False

def twoShipFinder():
    twoShipComplete = False
    if eightAcross > 1:
        twoShipComplete = acrossTwoShipFinder(780,240,eightAcross,"across")
    if sevenAcross > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(750,240,sevenAcross,"across")
    if sixAcross > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(720,240,sixAcross,"across")
    if fiveAcross > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(690,240,fiveAcross,"across")
    if fourAcross > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(660,240,fourAcross,"across")
    if threeAcross > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(630,240,threeAcross,"across")
    if twoAcross > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(600,240,twoAcross,"across")
    if oneAcross > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,240,oneAcross,"across")
    if oneDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,240,oneDown,"down")
    if twoDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,270,twoDown,"down")
    if threeDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,300,threeDown,"down")
    if fourDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,330,fourDown,"down")
    if fiveDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,360,fiveDown,"down")
    if sixDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,390,sixDown,"down")
    if sevenDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,420,sevenDown,"down")
    if eightDown > 1 and twoShipComplete == False:
        twoShipComplete = acrossTwoShipFinder(570,450,eightDown,"down")

def acrossFullTwo(xBeta, yBeta, direction):
    counterBoatAcross = 0
    counterBoatTempAcross = 0
    startOfBoatTempTwoThing = 0
    startOfBoatTwoThing = 0
    pyautogui.moveTo(xBeta, yBeta)
    for i in range(8):
        x, y = pyautogui.position()
        if pyscreeze.pixelMatchesColor(x,y,(47,47,47),tolerance=5):
            counterBoatTempAcross = counterBoatTempAcross + 1
            if counterBoatTempAcross == 2:
                startOfBoatTwoThing = startOfBoatTempTwoThing
            if counterBoatTempAcross > counterBoatAcross:
                counterBoatAcross = counterBoatTempAcross
            if counterBoatTempAcross == 1:
                startOfBoatTempTwoThing = (x,y)
        else:
            counterBoatTempAcross = 0
        moveNothing(direction,30,"no")
    if counterBoatAcross == 2:
        pyautogui.moveTo(startOfBoatTwoThing)
        moveNothing(direction,-30,"80Click")
        moveNothing(direction,90,"80Click")

def fullTwoFinder():
    if eightAcross > 1:
        acrossFullTwo(780,240,"across")
    if sevenAcross > 1:
        acrossFullTwo(750,240,"across")
    if sixAcross > 1:
        acrossFullTwo(720,240,"across")
    if fiveAcross > 1:
        acrossFullTwo(690,240,"across")
    if fourAcross > 1:
        acrossFullTwo(660,240,"across")
    if threeAcross > 1:
        acrossFullTwo(630,240,"across")
    if twoAcross > 1:
        acrossFullTwo(600,240,"across")
    if oneAcross > 1:
        acrossFullTwo(570,240,"across")
    if oneDown > 1:
        acrossFullTwo(570,240,"down")
    if twoDown > 1:
        acrossFullTwo(570,270,"down")
    if threeDown > 1:
        acrossFullTwo(570,300,"down")
    if fourDown > 1:
        acrossFullTwo(570,330,"down")
    if fiveDown > 1:
        acrossFullTwo(570,360,"down")
    if sixDown > 1:
        acrossFullTwo(570,390,"down")
    if sevenDown > 1:
        acrossFullTwo(570,420,"down")
    if eightDown > 1:
        acrossFullTwo(570,450,"down")


onlySpotsLeftRule()
cornerCheckerCool()
onlySpotsLeftRule()
for variable in squares:
    if variable["squared"] == False and variable["shape"] == "square":
        variable["squared"] = squareChecker(variable)
cornerCheckerCool()
fourShipFinder()
cornerCheckerCool()
clickAll()
onlySpotsLeftRule()
onlySpotsLeftRule()
clickAll()
fourShipFinder()
fullThreeFinder()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    onlySpotsLeftRule()
    onlySpotsLeftRule()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    fullThreeFinder()
    threeShipFinder()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    clickAll()
    onlySpotsLeftRule()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    cornerCheckerCool()
    onlySpotsLeftRule()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    threeShipFinder()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    fullTwoFinder()
    clickAll()
    onlySpotsLeftRule()
    cornerCheckerCool()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    clickAll()
    fullTwoFinder()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    twoShipFinder()
    onlySpotsLeftRule()
if not pyscreeze.pixelMatchesColor(800,471,(114,255,162),tolerance=5):
    cornerCheckerCool()
    onlySpotsLeftRule()
for i in range(4):
    pyautogui.press('up')
    pyautogui.press('down')

# also, now that this is basically done, i can code 7x7 and 6x6!
# add another "is it done already" check to four ship finder and have it only do ONE
# ok so i need to make it run squarechecker again somehow. this is a very temporary fix. like do a squared or not thing. the square check is done
# i think the shapes array is just unnecessary. check to make sure nothing runs off it then replace
