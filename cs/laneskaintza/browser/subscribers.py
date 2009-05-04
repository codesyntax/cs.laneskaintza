from Acquisition import aq_inner, aq_parent
from Products.CMFCore.utils import getToolByName
from zope.app.annotation.interfaces import IAnnotations, IAttributeAnnotatable
from BTrees.OOBTree import OOBTree
from urllib import urlopen
def laneskaintza_created(object, event):
    
    
    
    #if not object.getFolderContents({'portal_type':'FormFolder'}):
    context = aq_inner(object)
    aita=aq_parent(context)
    
    formfolder=aita.getFolderContents({'portal_type':'FormFolder'})
    if formfolder:
        form_title=context.Title()
        form_id=context.id + '-form'
        
           
        context.invokeFactory(id=form_id, type_name='FormFolder')
            
        formularioa=getattr(context, form_id)
        formularioa.setTitle(form_title)

        formularioko_fields=formularioa.getFolderContents({'language':context.REQUEST.LANGUAGE}, full_objects=1)
        form_list=[]
        for i in formularioko_fields:
            form_list.append(i.id)
        formularioa.manage_delObjects(form_list)
        barrukoak=formfolder[0].getObject().getFolderContents({'language':object.REQUEST.LANGUAGE}, full_objects=1)
        lista=[]
        for i in barrukoak:
            lista.append(i.id)
        copy_object=formfolder[0].getObject().manage_copyObjects(ids=lista)
        formularioa.manage_pasteObjects(copy_object)
        #import pdb;pdb.set_trace()
        bidaltzailea=formularioa.getFolderContents({'portal_type':'XMLMailerAdapter'})[0].id
        formularioa.setActionAdapter(bidaltzailea)
        
        eskertze_orria=formularioa.getFolderContents({'portal_type':'CodeFormThanksPage'})[0].id
        formularioa.setThanksPage(eskertze_orria)
        #import pdb;pdb.set_trace()
        
        if context.REQUEST.LANGUAGE=="es":
            formularioa.setSubmitLabel('enviar')
        else:
            formularioa.setSubmitLabel('bidali')
        """   
        copy_object=aita.manage_copyObjects(ids=[formfolder[0].getObject().id])
        object.manage_pasteObjects(copy_object)
        formularioa=getattr(context, 'alta-eman')
        formularioa.setTitle(context.id + ' form')
        formularioa._renameAfterCreation()
        formularioa.setLanguage(context.REQUEST.LANGUAGE)
        formularioa.reindexObject()
        """
