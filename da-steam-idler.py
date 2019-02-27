from ctypes import *
import os
from PIL import Image, ImageTk
import sys
import tkinter as tk
import wget

listPhoto = []

def checkPlatform():
    if not sys.platform.startswith('win32'):
        print("Platform "+sys.platform+" is not supported")
        sys.exit()

def getSteamApi():
    apiSteam = CDLL('steam_api.dll')
    return apiSteam
    
def setSteamAppId( appId ):
    os.environ["SteamAppId"]=appId

def createImageFolder():
    folder = os.path.dirname("./game_images/")
    try:
        os.stat(folder) 
    except: 
        os.mkdir(folder)

def createImageFolderForApp( appId):
    folder = os.path.dirname("./game_images/"+appId+"/")
    try:
        os.stat(folder) 
    except: 
        os.mkdir(folder)

def getImage( appId, imagePath):
    url = "http://cdn.akamai.steamstatic.com/steam/apps/" + appId + "/header_292x136.jpg"
    createImageFolderForApp( appId)
    if not os.path.isfile(imagePath):
        wget.download(url, out=imagePath)
        return imagePath
    return imagePath

    
    
def goWindow( appId, fenetre ):
    setSteamAppId( appId )
    gameLaunched = False
    try:
        gameLaunched = getSteamApi().SteamAPI_Init()
    except:
        print("Can't init the Steam API")
        sys.exit()
    if not gameLaunched:
        print("Game has not been 'launched'", appId)
        sys.exit()
    else:    
        imagePath = "./game_images/"+appId+"/picture.jpg"
        getImage(appId,imagePath)
        image = Image.open(imagePath)
        photo = ImageTk.PhotoImage(image)
        tk.Label(fenetre,
                 text="Jeu simulé: "+appId,
                 image=photo).pack()
        listPhoto.append(photo)
      
def main():
    checkPlatform()
    createImageFolder()
    fenetre = tk.Tk()
    fenetre.title("Idling like a boss")           

    length = len(sys.argv)
    fenetre.geometry("300x140")
    #fenetre.geometry("300x"+str(max(140, (length-1)*140)))
    if length > 1:
    #    for index in range(1,length):
    #        goWindow(sys.argv[index], fenetre)
        goWindow(sys.argv[1], fenetre)
    else:
        arg = input("Pour quel AppId?\n")
        goWindow(arg, fenetre)
     
main()
    




