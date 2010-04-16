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
                
                situations=context.getSituation_source()
                situation_string=situations[situation]

                laneskaintzak=context.getFolderContents({'portal_type':'laneskaintza','review_state':'published','laneskaintza_situation':situation_string})
                from Products.CMFPlone import Batch
                b_start = context.REQUEST.get('b_start', 0)
                batch = Batch(laneskaintzak, 30, int(b_start), orphan=0)
                return batch
                
