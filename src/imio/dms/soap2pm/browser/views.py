## -*- coding: utf-8 -*-

import base64
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class IncomingMailSoapClientView(BrowserView):
    """ Adapts an incomingmail to prepare data to exchange within imio.pm.wsclient """

    def getMainFiles(self):
        pc = getToolByName(self.context, 'portal_catalog')
        res = []
        for brain in pc(portal_type='dmsmainfile', path='/'.join(self.context.getPhysicalPath())):
            obj = brain.getObject()
            res.append({'title': obj.title.encode('utf8'),
                        'filename': obj.file.filename.encode('utf8'),
                        'file': base64.b64encode(obj.file.data)})
        return res
