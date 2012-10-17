from matplotlib.widgets import  RectangleSelector
import matplotlib.pyplot as plt
import numpy as np
class PointsBuilder:
  def __init__(self, data):
    fig = plt.figure()
    self.ax = fig.add_subplot(111)
    self.ax.imshow(data)
    self.xs = []
    self.ys = []
    self.cid = self.ax.figure.canvas.mpl_connect('button_press_event', self)
    plt.show()
    plt.close()

  def __call__(self, event):
    if event.inaxes!=self.ax.axes: return
    self.xs.append(event.xdata)
    self.ys.append(event.ydata)
    xlim = self.ax.get_xlim()
    ylim = self.ax.get_ylim()
    for xpoint,ypoint in zip(self.xs,self.ys):
      self.ax.plot(
          [xpoint],
          [ypoint],
          marker='o',
          mfc='None')
    self.ax.set_xlim(xlim)
    self.ax.set_ylim(ylim)
    self.ax.figure.canvas.draw()

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
    self.subimage = None

    self.templateFig = plt.figure()
    self.templateFig.canvas.set_window_title('Subimage') 
    self.templatePlot = self.templateFig.add_subplot(111)
    plt.show()

    plt.close()

  def onselect(self, eclick, erelease):
    #Matplotlib and numpy defines x and y orthogonal
    #to eachother. Prompting this switch.
    self.y1, self.y2 = int(eclick.xdata), int(erelease.xdata)
    self.x1, self.x2 = int(eclick.ydata), int(erelease.ydata)
    self.subimage = self.data[
      self.x1:self.x2,
      self.y1:self.y2]
    self.templatePlot.imshow(self.subimage) 
    self.templateFig.canvas.draw()

def getSubImage(data):
  tempSubImage = RectangleBuilder(data)
  subImage = tempSubImage.subimage
  pos1 = tempSubImage.x1, tempSubImage.y1
  pos2 = tempSubImage.x2, tempSubImage.y2
  return(subImage, pos1, pos2)

def getPoints(data):
  tempPoints = PointsBuilder(data)
  #Matplotlib and numpy defines x and y orthogonal
  #to eachother. Prompting this switch.
  xpoints = tempPoints.ys
  ypoints = tempPoints.xs
  return(xpoints, ypoints)
