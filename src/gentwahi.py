import os
import glob
import fontforge
import multiprocessing

# make new font
font = fontforge.font()

# font info
font.fontname   = "twahi"
font.fondname   = "twahi"
font.fullname   = "twahi"
font.familyname = "twahi"
font.encoding   = "UnicodeFull"
font.version    = "1.0"

# list of character number
num16 = lambda x : int(os.path.splitext(os.path.basename(x))[0], 16)
lst = list(map(num16, glob.glob("../img/*.png")))

# list of tsuro tile number
num10 = lambda x : int(os.path.splitext(os.path.basename(x))[0], 10)
tiles = list(map(num10, glob.glob("../tile/*.svg")))

# function to generate svg
def gensvg(i):
	if os.path.exists("../img/%03x.png" % i):
		os.system("convert ../img/%03x.png %03x.bmp" % (i,i)) #png -> bmp
		os.system("potrace -s %03x.bmp" % i)                  #bmp -> svg
		os.system("rm %03x.bmp" % i)

# generate svg
p = multiprocessing.Pool()
p.map(gensvg, lst)

# register glyph
point = 0x100000 # first code point of osa
for i in lst:
	if os.path.exists("%03x.svg" % i):
		glyph = font.createMappedChar(point + i)       
		glyph.importOutlines("%03x.svg" % i) 
		os.system("rm %03x.svg" % i)

# register tsuro tile glyph
point = 0x1001D0 # first code point of tsuro tile
for i in tiles:
	if os.path.exists("../tile/%03d.svg" % i):
		glyph = font.createMappedChar(point + i)       
		glyph.importOutlines("../tile/%03d.svg" % i) 

# save twahi ttf
font.generate('twahi.ttf')

font.close()

