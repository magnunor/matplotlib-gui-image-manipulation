from matplotlib.widgets import  RectangleSelector
import matplotlib.pyplot as plt
import numpy as np

class RectangleBuilder:
  def __init__(self, data):
    self.data = data

    mainFig = plt.figure(figsize=(5,9))
    mainFig.canvas.set_window_title('Original image') 
    mainFig.suptitle("Use the mouse to drag a box around the area.\nThis area will be shown in the template figure.\nWhen you're happy with the subimage,\n close the two figures to continue the program.\nTo zoom, use the magnifying-glass button.\nTo go back to selection mode, press it again.")
    ax = mainFig.add_subplot(111)
    ax.imshow(self.data)
    self.rectSelc = RectangleSelector(ax, self.onselect, drawtype='box')

    self.x1 = None
    self.x2 = None
    self.y1 = None
    self.y2 = None
    self.template = None

    self.templateFig = plt.figure()
    self.templateFig.canvas.set_window_title('Subimage') 
    self.templatePlot = self.templateFig.add_subplot(111)
    plt.tight_layout()
    plt.show()

    plt.close()

  def onselect(self, eclick, erelease):
    self.y1, self.y2 = int(eclick.xdata), int(erelease.xdata)
    self.x1, self.x2 = int(eclick.ydata), int(erelease.ydata)
    self.template = self.data[
      self.x1:self.x2,
      self.y1:self.y2]
    self.templatePlot.imshow(self.template) 
    self.templateFig.canvas.draw()

def getSubImage(data):
  getTemplate = RectangleBuilder(data)
  template = getTemplate.template
  pos1 = getTemplate.x1, getTemplate.y1
  pos2 = getTemplate.x2, getTemplate.y2
  return(template, pos1, pos2)
