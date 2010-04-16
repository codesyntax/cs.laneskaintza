from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from cs.laneskaintza import laneskaintzaMessageFactory as _


class laneskaintzaView(BrowserView):
    """
    laneskaintza browser view
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def request_form(self):
        #import pdb;pdb.set_trace()
        
        if self.context.getRequest_form() and self.context.getFolderContents({'portal_type':'FormFolder'}) and not self.context.getFolderContents({'portal_type':'csvfinder'}):
            return True
        else:
            return False
