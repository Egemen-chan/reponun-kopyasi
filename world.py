import pygame as pg 

class World():
  def __init__(self, data, map_image):
    self.level_data = data
    self.image = map_image

  def process_data(self):
    #datayı inceleyecek olan method
    for layer in self.level_data["layers"]:
      if layer["name"] == "waypoints":
        for obj in layer["objects"]:
          waypoint_data = obj["polyline"]
          print(waypoint_data)
          
  def draw(self, surface):
    surface.blit(self.image, (0,0))
