#=========================================================================================
# Licence, Reference and Credits
#=========================================================================================
__copyright__ = "Copyright (C) CCPN project (http://www.ccpn.ac.uk) 2014 - 2019"
__credits__ = ("Ed Brooksbank, Luca Mureddu, Timothy J Ragan & Geerten W Vuister")
__licence__ = ("CCPN licence. See http://www.ccpn.ac.uk/v3-software/downloads/license")
__reference__ = ("Skinner, S.P., Fogh, R.H., Boucher, W., Ragan, T.J., Mureddu, L.G., & Vuister, G.W.",
                 "CcpNmr AnalysisAssign: a flexible platform for integrated NMR analysis",
                 "J.Biomol.Nmr (2016), 66, 111-124, http://doi.org/10.1007/s10858-016-0060-y")
#=========================================================================================
# Last code modification
#=========================================================================================
__modifiedBy__ = "$modifiedBy: CCPN $"
__dateModified__ = "$dateModified: 2017-07-07 16:32:26 +0100 (Fri, July 07, 2017) $"
__version__ = "$Revision: 3.0.0 $"
#=========================================================================================
# Created
#=========================================================================================
__author__ = "$Author: TJ Ragan$"
__date__ = "$Date: 2017-04-07 10:28:40 +0000 (Fri, April 07, 2017) $"
#=========================================================================================
# Start of code
#=========================================================================================

from ccpn.framework import Framework
from ccpn.AnalysisStructure.AnalysisStructure import Structure as Application
from ccpn.framework.Version import applicationVersion


if __name__ == '__main__':
    from ccpn.util.GitTools import getAllRepositoriesGitCommit
    applicationVersion = 'development: {AnalysisStructure:.8s}'.format(**getAllRepositoriesGitCommit())

    # argument parser
    parser = Framework.defineProgramArguments()

    # add any additional commandline argument here
    commandLineArguments = parser.parse_args()

    application = Application(Framework.AnalysisStructure, applicationVersion, commandLineArguments)
    Framework._getApplication = lambda: application

    application.start()
