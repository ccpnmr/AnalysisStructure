"""
AnalysisAssign Program

Please cite:  Skinner et al, J Biomol NMR (2016) 66:111–124; DOI 10.1007/s10858-016-0060-y 

"""
#=========================================================================================
# Licence, Reference and Credits
#=========================================================================================
__copyright__ = "Copyright (C) CCPN project (http://www.ccpn.ac.uk) 2014 - 2017"
__credits__ = ("Wayne Boucher, Ed Brooksbank, Rasmus H Fogh, Luca Mureddu, Timothy J Ragan & Geerten W Vuister")
__licence__ = ("CCPN licence. See http://www.ccpn.ac.uk/v3-software/downloads/license",
               "or ccpnmodel.ccpncore.memops.Credits.CcpnLicense for licence text")
__reference__ = ("For publications, please use reference from http://www.ccpn.ac.uk/v3-software/downloads/license",
               "or ccpnmodel.ccpncore.memops.Credits.CcpNmrReference")
#=========================================================================================
# Last code modification
#=========================================================================================
__modifiedBy__ = "$modifiedBy: Ed Brooksbank $"
__dateModified__ = "$dateModified: 2017-05-24 16:28:25 +0100 (Wed, May 24, 2017) $"
__version__ = "$Revision: 3.0.b1 $"
#=========================================================================================
# Created
#=========================================================================================
__author__ = "$Author: CCPN $"
__date__ = "$Date: 2017-04-07 10:28:40 +0000 (Fri, April 07, 2017) $"
#=========================================================================================
# Start of code
#=========================================================================================


from ccpn.AnalysisAssign.AnalysisAssign import Assign
from ccpn.util.Logging import getLogger

class Structure(Assign):
  """Root class for Structure application"""

  def __init__(self, applicationName, applicationVersion, commandLineArguments):
    Assign.__init__(self, applicationName, applicationVersion, commandLineArguments)

  def setupMenus(self):
    super().setupMenus()
    menuSpec = ('Structure', [("Structure Table", self.showStructureTable, [('shortcut', 'st')]),
                             ])
    self.addApplicationMenuSpec(menuSpec, position=4)

  def showStructureTable(self, position='bottom', relativeTo=None, structureEnsemble=None):
    """Displays Structure Table"""
    from ccpn.ui.gui.modules.StructureTable import StructureTableModule

    mainWindow = self.ui.mainWindow

    #FIXME:ED - sometimes crashes
    if not relativeTo:
      relativeTo = mainWindow.moduleArea      # ejb
    self.structureTableModule = StructureTableModule(mainWindow=mainWindow
                                                , structureEnsemble=structureEnsemble)

    self.project.newModule(moduleType=self.structureTableModule.className
                           , title=None
                           , window=mainWindow
                           , comment='')

    mainWindow.moduleArea.addModule(self.structureTableModule, position=position, relativeTo=relativeTo)

    mainWindow.pythonConsole.writeConsoleCommand("application.showStructureTable()\n")
    getLogger().info("application.showStructureTable()")
    return self.structureTableModule

