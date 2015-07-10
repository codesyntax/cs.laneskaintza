"""Definition of the laneskaintzaFolder content type
"""

from zope.interface import implements, directlyProvides

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from cs.laneskaintza import laneskaintzaMessageFactory as _
from cs.laneskaintza.interfaces import IlaneskaintzaFolder
from cs.laneskaintza.config import PROJECTNAME

laneskaintzaFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.TextField('contact_information',
                        required=False,
                        searchable=True,
			storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'contact_information'),
                                                description=_(u'Description of contact_information'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
   atapi.LinesField(
        name='situation_source',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.LinesWidget(
            label=_(u"situation_source"),
            description=_(u"Description of situation_source"),
        ),
    ),

   atapi.TextField('text',
                        required=False,
                        searchable=True,
            storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'text'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

laneskaintzaFolderSchema['title'].storage = atapi.AnnotationStorage()
laneskaintzaFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    laneskaintzaFolderSchema,
    folderish=True,
    moveDiscussion=False
)

class laneskaintzaFolder(folder.ATFolder):
    """Description of the Example Type"""
    implements(IlaneskaintzaFolder)

    meta_type = "laneskaintzaFolder"
    schema = laneskaintzaFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(laneskaintzaFolder, PROJECTNAME)
