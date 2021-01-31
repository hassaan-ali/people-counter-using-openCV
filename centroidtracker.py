#import necessary packages
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class CentroidTracker():
  def __init__(self, maxDisappeared=50):
    self.nextObjectID = 0
    #counter used to assign unique ID to each object
    self.objects=OrderedDict()
    #objectID as key and centroid(x,y) coordinates as values
    self.disappeared=OrderedDict()
    #ObjectID will be the key and number of consective frames will be the value
    self.maxDisappeared = maxDisappeared
    #number of consecutive frames for a disappeared object till we deregister it

  def register(self, centroid):
    self.objects[self.nextObjectID] = centroid
    self.disappeared[self.nextObjectID] = 0
    self.nextObjectID +=1

  def deregister(self, objectID):
    del self.object(objectID)
    del self.disappeared(objectID)

 
