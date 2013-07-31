"""
Module containing a handler base class for drawing surfaces
used with the LSystemFactory class.
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

import math

class SurfaceHandler(object):
	def __init__(self, coordinates = (0, 0), angle = 0):
		"""
		Sets the initial angle and coordinates
		"""
		self.x, self.y = 0, 0
		self.angle = 0 # The current angle to the horizontal axis, increases anti-clockwise.
		self.coordinate_stack = []
	
	
	def line_forward(self, distance):
		"""
		Moving forward in the direction of the current angle by a given distance
		"""
		# Saving the current coordinates
		old_x, old_y = self.x, self.y
		
		# Resolving the displacement vector
		self.x = old_x + math.cos(math.radians(angle)) * distance
		self.y = old_y - math.sin(math.radians(angle)) * distance
		
		self._draw_line(old_x, old_y, self.x, self.y)
	
	
	def _draw_line(self, start_x, start_y, end_x, end_y):
		"""
		Function for drawing a line from a start point to an end point is to be
		implemented in the child classes.
		"""
		pass
	
	
	def push(self):
		"""
		Pushing the current coordinate to the stack.
		"""
		self.coordinate_stack.append((self.x, self.y))
	
	
	def pop(self):
		"""
		Pops the last saved coordinate off the stack and
		sets it as the current coordinate.
		"""
		#TODO: handling exceptions, in case the stack is empty.
		(self.x, self.y) = self.coordinate_stack.pop()
	
	
	def turn_right(self, del_angle):
		"""
		Turning right by a given angle, assuming the x axis increases from left
		to right.
		"""
		self._turn(- del_angle)
	
	
	def turn_left(self, del_angle):
		"""
		Turning left by a given angle.
		"""
		self._turn(del_angle):
	
	
	def _turn(self, del_angle):
		"""
		Changing the angle by a given angle.
		"""
		self.angle = (self.angle + del_angle) % 360
	
