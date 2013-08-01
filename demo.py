#!/usr/bin/env python3.2
"""
Demonstration of the lsystem library.
see: http://en.wikipedia.org/wiki/L-system
Author: Huba Z. Nagy
Date: 29 July 2013

Released under the MIT Licence.

Copyright (c) 2013 Huba Z. Nagy

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
"""

import lsystem
from tkinter import *



class Application(Frame):
	"""
	Simple TKInter application.
	"""
	def __init__(self, master=None):
		"""
		Constructor for the application.
		"""
		Frame.__init__(self, master)
		
		self.pack()
		self.create_widgets()
	
	
	def create_widgets(self):
		"""
		Creating a canvas widget to draw on and drawing an L System on it
		"""
		self.canvas = Canvas(self, bg = "black")
		self.canvas.config(width = 1024, height = 768)
		self.canvas.pack()
		
		#l_sys = lsystem.LSystemFactory('F - G - G', 'F > F - G + F + G - F, G > G G', angle = 120, distance = 10, forward_tokens = 'FG') #Serpinski Triangle variation 1
		#l_sys = lsystem.LSystemFactory('A', 'A > B - A - B, B > A + B + A', angle = 60, distance = 0.1, forward_tokens = 'AB') #Serpinski Triangle variation 2
		#l_sys = lsystem.LSystemFactory('F X', 'X > X + Y F, Y > F X - Y', distance = 1, angle = 45, forward_tokens='F') #Dragon Curve
		l_sys = lsystem.LSystemFactory('X', 'X > F - [ [ X ] + X ] + F [ + F X ] - X, F > F F', distance = 10, angle = 25, forward_tokens='F') #Fractal Plant
		c_handler = lsystem.TKCanvasHandler(self.canvas, coordinates = (512, 740), angle = -90)
		print("\n")
		l_sys.evolve_on_surface(c_handler, target_order = 6)
		print("\n")



if __name__ == "__main__":
	root = Tk()
	app = Application(master=root)
	app.mainloop()
	root.destroy()