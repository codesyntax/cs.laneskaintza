__version__ = '$Id$'

from Products.CMFPlone import utils
import DateTime
import pdb
import os
from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from Products.Five.browser import BrowserView
from Acquisition import aq_inner
class Lista(BrowserView):

			
	def laneskaintza_lista(self, situation):
		context = aq_inner(self.context)
                #import pdb;pdb.set_trace()
                laneskaintzak=context.getFolderContents({'portal_type':'laneskaintza','review_state':'published'})
                lista1=[]
                lista2=[]
                lista3=[]
		for obj in laneskaintzak:
                    if obj.getObject().getSituation() in ["zabalik","abierto"]:
                        lista1.append(obj)
                    elif obj.getObject().getSituation() in ["martxan","en-proceso"]:
                        lista2.append(obj)
                    else:
                        lista3.append(obj)
                from Products.CMFPlone import Batch
                b_start = context.REQUEST.get('b_start', 0)
                if situation==1:
                    batch = Batch(lista1, 10, int(b_start), orphan=0)
                    return batch
                elif situation==2:
                    batch = Batch(lista2, 10, int(b_start), orphan=0)
                    return batch
                else:
                    batch = Batch(lista3, 10, int(b_start), orphan=0)
                    return batch
