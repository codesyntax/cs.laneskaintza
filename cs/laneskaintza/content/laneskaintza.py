"""Definition of the laneskaintza content type
"""

from zope.interface import implements, directlyProvides
try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from cs.laneskaintza import laneskaintzaMessageFactory as _
from cs.laneskaintza.interfaces import Ilaneskaintza
from cs.laneskaintza.config import PROJECTNAME
from Acquisition import aq_inner, aq_parent
laneskaintzaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField('information',
                        required=False,
                        searchable=True,
            storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'information'),
                                                description=_(u'Description of information'),
                                                rows=3,
                                                allow_file_upload=False),
                        ),

   atapi.FileField('modelo_instancia',
                  searchable=0,
          languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u"modelo_instancia"),
                     description=_(u"Description of modelo_instancia"),
                     ),
                  ),

   atapi.FileField('temario',
                  searchable=0,
          languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u"temario"),
                     description=_(u"Description of temario"),
                     ),
                  ),

   atapi.DateTimeField(
        name='start_data',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"start_data"),
            description=_(u"Description of start_data"),
        ),
    ),

    atapi.DateTimeField(
        name='start_data_bog',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"start_data_bog"),
            description=_(u"Description of start_data_bog"),
        ),
    ),
    atapi.FileField('file_information',
                  searchable=0,
          languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u"file_information"),
                     description=_(u"Description of file_information"),
                     ),
                  ),

    atapi.DateTimeField(
        name='prensa_data',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"prensa_data"),
            description=_(u"Description of prensa_data"),
        ),
    ),
    atapi.FileField('file_prensa',
                  searchable=0,
                  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u"file_prensa"),
                     description=_(u"Description of file_prensa"),
                     ),
                  ),

   atapi.DateTimeField(
        name='end_data',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"end_data"),
            description=_(u"Description of end_data"),
        ),
    ),


   atapi.DateTimeField(
        name='file_enrolled_data',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"file_enrolled_data"),
            description=_(u"Description of file_enrolled_data"),
        ),
    ),

   atapi.FileField('file_enrolled',
                  searchable=0,
          languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u"file_enrolled"),
                     description=_(u"Description of file_enrolled"),
                     ),
                  ),

   atapi.DateTimeField(
        name='final_file_enrolled_data',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"final_file_enrolled_data"),
            description=_(u"Description of final_file_enrolled_data"),
        ),
    ),

   atapi.FileField('final_file_enrolled',
                  searchable=0,
          languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u"final_file_enrolled"),
                     description=_(u"Description of final_file_enrolled"),
                     ),
                  ),

   atapi.TextField('information_examenes',
                        required=False,
                        searchable=True,
            storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'information_examenes'),
                                                description=_(u'Description of information_examenes'),
                                                rows=3,
                                                allow_file_upload=False),
                        ),
   atapi.DateTimeField(
        name='file_exercise_results_data',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"file_exercise_results_data"),
            description=_(u"Description of file_exercise_results_data"),
        ),
    ),
   atapi.FileField('file_exercise_results',
                  searchable=0,
          languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u"file_exercise_results"),
                     description=_(u"Description of file_exercise_results"),
                     ),
                  ),

   atapi.StringField('situation',
                  searchable=1,
          languageIndependent=0,
          vocabulary='whichsituation',
                  widget=atapi.SelectionWidget(
                     label=_(u"situation"),
                     description=_(u"Description of situation"),

                     ),
                  ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

laneskaintzaSchema['title'].storage = atapi.AnnotationStorage()
laneskaintzaSchema['description'].storage = atapi.AnnotationStorage()
laneskaintzaSchema['description'].storage = atapi.AnnotationStorage()
laneskaintzaSchema['description'].widget.visible = {'edit':'hidden','view':'hidden'}
schemata.finalizeATCTSchema(
    laneskaintzaSchema,
    folderish=True,
    moveDiscussion=False
)

class laneskaintza(folder.ATFolder):
    """Description of the Example Type"""
    implements(Ilaneskaintza)

    meta_type = "laneskaintza"
    schema = laneskaintzaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    def whichsituation(self):
            #import pdb;pdb.set_trace()
            situation_list=aq_parent(self).getSituation_source()

            return situation_list
atapi.registerType(laneskaintza, PROJECTNAME)
