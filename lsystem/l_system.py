"""
Module for generating recursive L-Systems
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

import math

class LSystemFactory(object):
	"""
	Factory class for evolving L Systems onto various drawing surfaces.
	"""
	def __init__(self, 
	             start_expr, 
	             rule_expr, 
	             angle = 90, 
	             distance = 10, 
	             forward_tokens = 'F'):
		"""
		Constructor for LSystemFactory class
		"""
		self.angle, self.distance = angle, distance
		self.interpret_rules(rule_expr)
		self.expression = start_expr
		self.forward_tokens = forward_tokens
	
	def interpret_rules(self, full_rule_expr):
		"""
		Organizes the rule expression into a dictionary for easy lookup
		the replacement expressions are mapped to the token
		"""
		self.rules = {}
		rule_expressions = full_rule_expr.strip().split(',') #each rule in the rule expression is separated by a comma
		
		for rule_expr in rule_expressions:
			sides = rule_expr.strip().split('>')
			self.rules[sides[0].strip()] = sides[1].strip()
		
		print(self.rules)
	
	
	def evolve_on_surface(self, 
	                      surface_handler, 
	                      expression = None, 
	                      current_order = 0, 
	                      target_order = 5):
		"""
		Recursively evolves the LSystem onto a given surface, through a surface handler using a LIFO stack mechanism, 
		the fully expanded expression is not stored in memory.
		"""
		if expression == None:
			expression = self.expression #For the first level on the call stack no expression
			                             #should be passed, so the current expression is set to
			                             #the starting expression
		
		for token in expression.split(' '):
			if (current_order < target_order) and (token in self.rules):
				#the next rule is pushed onto the call stack with the current
				#recursion depth as long as the specified
				#target depth (or order) is not reached.
				self.evolve_on_surface(surface_handler, 
				                       self.rules[token], 
				                       current_order + 1, 
				                       target_order)
			
			elif (token in self.forward_tokens):
				print(token, end = ' ')
				surface_handler.line_forward(self.distance)
			
			elif token == "+":
				#updating the angles
				print(token, end = ' ')
				surface_handler.turn_right(self.angle)
			
			elif token == "-":
				print(token, end = ' ')
				surface_handler.turn_left(self.angle)
			
			else:
				print(token, end = ' ')
		
