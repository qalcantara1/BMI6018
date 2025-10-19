class crate(object):
   def __init__(self, weight, dimensions, fill_state):
      self.weight = weight
      self.dimensions = dimensions
      self.fill_state = fill_state
      self.texture = texture
   def fill(self):
      if self.fill_state==0:
         self.fill_state=1
      else:
         return ('No room!')