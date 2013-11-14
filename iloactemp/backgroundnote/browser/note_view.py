from five import grok
from plone.directives import dexterity, form
from iloactemp.backgroundnote.content.note import INote

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(INote)
    grok.require('zope2.View')
    grok.template('note_view')
    grok.name('view')

