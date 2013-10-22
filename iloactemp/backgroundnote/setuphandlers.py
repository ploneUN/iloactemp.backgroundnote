from collective.grok import gs
from iloactemp.backgroundnote import MessageFactory as _

@gs.importstep(
    name=u'iloactemp.backgroundnote', 
    title=_('iloactemp.backgroundnote import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('iloactemp.backgroundnote.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
