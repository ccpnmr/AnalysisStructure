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
from ccpn.ui.gui.widgets.FileDialog import FileDialog

class Structure(Assign):
  """Root class for Structure application"""

  def __init__(self, applicationName, applicationVersion, commandLineArguments):
    Assign.__init__(self, applicationName, applicationVersion, commandLineArguments)

  def setupMenus(self):
    super(Structure, self).setupMenus()
    menuSpec = ('Structure', [
                              ("Load PDB", self.loadPDB, [('shortcut', 'lp')]),
                              ("Load NEF", self.loadNEF, [('shortcut', 'ln')]),
                              (),
                              ("Structure Table", self.showStructureTable, [('shortcut', 'st')]),
                              ("Match to Molecule", self.matchToMolecule, [('shortcut', 'mm'), ('enabled', False)]),
                              ("Chain(s) from Structure", self.chainsFromStructure, [('shortcut', 'cs'), ('enabled', False)]),
                              (),
                              ("Find Consensus...", self.findConsensus, [('shortcut', 'fc'), ('enabled', False)]),
                              ("Superpose", self.superpose, [('shortcut', 'sp'), ('enabled', False)]),
                              (),
                              ("Validate Restraints", self.validateRestraints, [('shortcut', 'vr'), ('enabled', False)]),
                              (),
                              ("Submit to wwPDB", self.submitToWWPDB, [('shortcut', 'sw'), ('enabled', False)]),
    ])
    self.addApplicationMenuSpec(menuSpec, position=4)

  def loadData(self, paths=None, text=None, filter=None):
    if paths is None:
      #TODO:LIST-AS-ISSUE: This fails for native file dialogs on OSX when trying to select a project (i.e. a directory)
      # NBNB TBD I assume here that path is either a string or a list lf string paths.
      # NBNB #FIXME if incorrect
      dialog = FileDialog(parent=self.ui.mainWindow, fileMode=FileDialog.AnyFile, text=text
                          , acceptMode=FileDialog.AcceptOpen
                          , preferences=self.preferences.general
                          , filter=filter)
      path = dialog.selectedFile()
      if not path:
        return
      paths = [path]

    elif isinstance(paths, str):
      paths = [paths]

    for path in paths:
      self.project.loadData(path)

  def loadPDB(self):
    self.loadData(text='Load PDB File', filter='*.pdb')

  def loadNEF(self):
    self.loadData(text='Load NEF File', filter='*.nef')

  def showStructureTable(self, position='bottom', relativeTo=None, structureEnsemble=None):
    """Displays Structure Table"""
    from ccpn.ui.gui.modules.StructureTable import StructureTableModule

    mainWindow = self.ui.mainWindow

    #FIXME:ED - sometimes crashes
    if not relativeTo:
      relativeTo = mainWindow.moduleArea      # ejb
    self.structureTableModule = StructureTableModule(mainWindow=mainWindow
                                                , structureEnsemble=structureEnsemble)

    # self.project.newModule(moduleType=self.structureTableModule.className
    #                        , title=None
    #                        , window=mainWindow
    #                        , comment='')

    mainWindow.moduleArea.addModule(self.structureTableModule, position=position, relativeTo=relativeTo)

    mainWindow.pythonConsole.writeConsoleCommand("application.showStructureTable()\n")
    getLogger().info("application.showStructureTable()")
    return self.structureTableModule

  def matchToMolecule(self):
    pass

  def chainsFromStructure(self):
    pass

  def findConsensus(self):
    pass

  def superpose(self):
    pass

  def validateRestraints(self):
    pass

  def submitToWWPDB(self):
    pass

