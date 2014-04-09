from Acquisition import aq_inner, aq_parent

def laneskaintza_created(object, event):
    
    
    
    #if not object.getFolderContents({'portal_type':'FormFolder'}):
    context = aq_inner(object)
    aita=aq_parent(context)
    
    formfolder=aita.getFolderContents({'portal_type':'FormFolder'})
    #import pdb;pdb.set_trace()
    
    if formfolder:
        form_title=context.Title() + '-form'
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
        #import pdb;pdb.set_trace()
        for i in barrukoak:
            lista.append(i.id)
        copy_object=formfolder[0].getObject().manage_copyObjects(ids=lista)
        formularioa.manage_pasteObjects(copy_object)
        
        bidaltzailea=formularioa.getFolderContents({'portal_type':'XMLMailerAdapter'})[0]
        #import pdb;pdb.set_trace()
        
        if context.REQUEST.LANGUAGE == "eu":
            bidaltzailea.getObject().setMsg_subject("Lan Eskaintzan alta: " + context.Title())
        else:
            bidaltzailea.getObject().setMsg_subject("Alta oferta de empleo: " + context.Title())
        formularioa.setActionAdapter(bidaltzailea.id)
        
        eskertze_orria=formularioa.getFolderContents({'portal_type':'CodeFormThanksPage'})[0].id
        formularioa.setThanksPage(eskertze_orria)
        #import pdb;pdb.set_trace()
        
        if context.REQUEST.LANGUAGE=="es":
            formularioa.setSubmitLabel('enviar')
        else:
            formularioa.setSubmitLabel('bidali')
            
        formularioa._renameAfterCreation()
        formularioa.setTitle(context.Title())
