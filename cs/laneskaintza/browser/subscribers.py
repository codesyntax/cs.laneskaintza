from Acquisition import aq_inner, aq_parent
from Products.CMFCore.utils import getToolByName
from zope.app.annotation.interfaces import IAnnotations, IAttributeAnnotatable
from BTrees.OOBTree import OOBTree
from urllib import urlopen
def laneskaintza_created(object, event):
    
    import pdb;pdb.set_trace()
    
    if not object.getFolderContents({'portal_type':'FormFolder'}):
        aita=aq_parent(object)
        formfolder=aita.getFolderContents({'portal_type':'FormFolder'})
        if formfolder:
            copy_object=aq_parent(object).manage_copyObjects(formfolder[0].getObject().id)
            object.manage_pasteObjects(copy_object)
    
