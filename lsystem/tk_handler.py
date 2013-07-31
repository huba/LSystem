"""
Implementing the SurfaceHandler class to use tk's canvas
Author: Huba Z. Nagy
Date: 31 July 2013

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

from .surface_handler import SurfaceHandler

class TKCanvasHandler(SurfaceHandler):
	def __init__(self, canvas, coordinates = (0, 0), angle = 0, color = 'white'):
		SurfaceHandler.__init__(self, coordinates, angle)
		self.canvas = canvas
		self.color = color
	
	
	def _draw_line(self, start_x, start_y, end_x, end_y):
		"""
		implementation of drawing a line on tk canvas
		"""
		self.canvas.create_line(start_x, start_y, end_x, end_y, fill=self.color)
