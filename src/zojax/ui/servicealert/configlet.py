##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
$Id$
"""
import datetime

from zope import component
from zope.component import getUtility
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from zojax.cache.view import cache
from zojax.cache.tag import SiteTag
from zojax.resourcepackage.library import includeInplaceSource

from interfaces import IServiceAlert

try:
    from hashlib import md5
except ImportError:
    from md5 import new as md5

ServiceAlertTag = SiteTag('ui.servicealert')

htmlcode = '<div class="alert %s"><div class="message"><b>X</b>%s</div></div>' # sa-closed
jssource = '<script type="text/javascript">var service_alert = "%s";</script>'


class ServiceAlertPageElement(object):

    def update(self):
        self.configlet = getUtility(IServiceAlert)

    def render(self):
        if not self.request.has_key(self.configlet.cookie) and self.isAvailable():
            includeInplaceSource(jssource%self.configlet.cookie)
            return htmlcode % (self.configlet.color, self.configlet.message)
        return ''

    def isAvailable(self):
        return self.configlet.enabled and self.configlet.message

    @cache('pageelement:portal.ui.servicealert', ServiceAlertTag)
    def updateAndRender(self):
        return super(ServiceAlertPageElement, self).updateAndRender()


@component.adapter(IServiceAlert, IObjectModifiedEvent)
def configletChangeHandler(configlet, ev):

    # NOTE: set cookie id
    cookie = "__zojax_alert_%s" % md5(datetime.datetime.now().isoformat()).hexdigest()
    configlet.cookie = cookie.decode('utf-8')

    ServiceAlertTag.update()
