from pyx import *

c = canvas.canvas()
#c.stroke(path.line(0, 0, 3, 0))
#c.stroke(path.rect(0, 1, 1, 1))

# Circle radius
rad = 0.35
rad1 = 1 - rad

# Draw the first row of circles
for base_x in range(0, 45, 9):
	for base_y in range(0, 32, 8):
	
		c.stroke(path.rect(base_x-0.5-rad,base_y+(7.5-rad),2*rad, 2*rad))
		c.stroke(path.line(base_x-0.5,base_y+0.5,base_x+7.5,base_y+0.5))
		c.stroke(path.line(base_x+7.5,base_y+0.5,base_x+7.5,base_y+7.5))
		c.stroke(path.line(base_x+(-1+2*rad),base_y+7.5,base_x+7.5,base_y+7.5))
		c.stroke(path.line(base_x-0.5,base_y+0.5,base_x-0.5,base_y+(7.5-rad)))

		for j in range(7):
			for i in range(8):
				c.stroke(path.circle(base_x + i, base_y + j + 1, rad))
				if (i < 7):
					c.stroke(path.line(base_x+i+rad, base_y+j+1, \
									   base_x+i+rad1, base_y+j+1))
				if (j < 6):
					c.stroke(path.line(base_x+i, base_y+j+1+rad,
					                   base_x+i, base_y+j+1+rad1))

c.writeEPSfile("path")
c.writePDFfile("path")