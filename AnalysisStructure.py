"""
AnalysisAssign Program

Please cite:  Skinner et al, J Biomol NMR (2016) 66:111–124; DOI 10.1007/s10858-016-0060-y 

"""
#=========================================================================================
# Licence, Reference and Credits
#=========================================================================================
__copyright__ = "Copyright (C) CCPN project (http://www.ccpn.ac.uk) 2014 - 2017"
__credits__ = ("Wayne Boucher, Ed Brooksbank, Rasmus H Fogh, Luca Mureddu, Timothy J Ragan"
               "Simon P Skinner & Geerten W Vuister")
__licence__ = ("CCPN licence. See http://www.ccpn.ac.uk/v3-software/downloads/license"
               "or ccpnmodel.ccpncore.memops.Credits.CcpnLicense for licence text")
__reference__ = ("For publications, please use reference from http://www.ccpn.ac.uk/v3-software/downloads/license"
               "or ccpnmodel.ccpncore.memops.Credits.CcpNmrReference")

#=========================================================================================
# Last code modification
#=========================================================================================
__modifiedBy__ = "$modifiedBy: Ed Brooksbank $"
__dateModified__ = "$dateModified: 2017-04-07 11:40:21 +0100 (Fri, April 07, 2017) $"
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


class Structure(Assign):
  """Root class for Structure application"""

  def __init__(self, applicationName, applicationVersion, commandLineArguments):
    Assign.__init__(self, applicationName, applicationVersion, commandLineArguments)


  def setupMenus(self):
    super().setupMenus()
    menuSpec = ('Structure', [(),
                             ])
    self.addApplicationMenuSpec(menuSpec, position=4)
