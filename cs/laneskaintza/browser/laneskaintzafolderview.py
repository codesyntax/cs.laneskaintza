from Acquisition import aq_inner
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class laneskaintzaFolderView(BrowserView):
    """
    laneskaintzaFolder browser view
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

    def laneskaintza_lista(self):
        context = aq_inner(self.context)
        situation_string = self.request.get('id', None)
        if not situation_string:
            situations = self.states()
            situation_string = situations[0]
        laneskaintzak_request_form = context.getFolderContents({'portal_type':'laneskaintza','review_state':'published',
                                                    'laneskaintza_situation':situation_string,
                                                    'laneskaintza_request_form_index':(True, True)})

        return laneskaintzak_request_form

    def laneskaintza_lista_no_request_form(self):
        context = aq_inner(self.context)
        situation_string = self.request.get('id', None)
        if not situation_string:
            situations = self.states()
            situation_string = situations[0]
        laneskaintzak_request_form = context.getFolderContents({'portal_type':'laneskaintza','review_state':'published',
                                                    'laneskaintza_situation':situation_string,
                                                    'laneskaintza_request_form_index':(False, False)})


        return laneskaintzak_request_form

    def states(self):
        context = aq_inner(self.context)
        return context.getSituation_source()

    def situation_list(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        idea = context.REQUEST.get('id', None)
        states = self.states()
        state_list = []
        for state in states:
            ul_dict={}
            ul_dict['len'] = len(catalog(portal_type="laneskaintza", review_state="published",laneskaintza_situation=state))
            ul_dict['state']= state
            state_list.append(ul_dict)
        dict={}
        if idea:
           for state in states:
               if idea == state:
                   dict[state]="on"
               else:
                   dict[state]="off"
        else:
           dict[states[0]]="on"
           for state in states[1:]:
               dict[state]="off"
        return [dict, state_list]
