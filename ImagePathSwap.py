
ImagePath = "C:\Data\PhD\Projects\FlSeaGrantHurricaneViewsheds\FieldWork\FlaglerBeach\Transect0\GOPR0211.JPG"

def ImagePathSwap(ImagePath):
    fileName = ImagePath.split("\\")[-1]
    print(fileName)
    ImagePath = f"https://github.com/jderekito/TBVs/blob/main/FlaglerBeach/Transect0/{fileName}"
    # ImagePath = f'<img src="https://github.com/jderekito/TBVs/blob/main/FlaglerBeach/Transect0/{fileName}" style="width:100px;height:100px;">'
    return ImagePath

print(ImagePath)
ImagePath = ImagePathSwap(ImagePath)
print(ImagePath)




              