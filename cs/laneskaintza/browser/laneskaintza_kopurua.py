__version__ = '$Id$'

from Products.CMFPlone import utils
import DateTime
import pdb
import os
from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from Products.Five.browser import BrowserView
from Acquisition import aq_inner
class Kopurua(BrowserView):

			
	def laneskaintza_kopurua(self, situation):
		context = aq_inner(self.context)
                #import pdb;pdb.set_trace()
                
                situations=context.getSituation_source()
                situation_string=situations[situation]

                laneskaintzak=context.getFolderContents({'portal_type':'laneskaintza','review_state':'published','laneskaintza_situation':situation_string})
                return len(laneskaintzak)
                
