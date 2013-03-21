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
""" servicealert portlet interfaces

$Id$
"""
from zope import schema, interface
from zope.i18nmessageid import MessageFactory

from zojax.widget.list import SimpleList
from zojax.widget.radio.field import RadioChoice


_ = MessageFactory('zojax.ui.servicealert')


class IServiceAlertHeaders(interface.Interface):
    """ service alert headers """


class IServiceAlert(interface.Interface):
    """ configlet interface """

    enabled = schema.Bool(
        title = _(u'Enabled'),
        description = _(u'Enable service alert for this site.'),
        default = False,
        required = False)

    color = RadioChoice(
        title = _(u'Background Color'),
        description = _(u'Select background color for Service Alert.'),
        vocabulary = 'zojax.ui.servicealert.alert-colors',
        default = u'yellow',
        required = True)

    message = schema.Text(
        title = _(u'Service Alert Message'),
        description = _(u'Please, enter service alert message.'),
        default = u'',
        required = False)

    cookie = schema.TextLine(
        title=_(u'cookie Id'),
        required=False)


class IConfigletEditWizard(interface.Interface):
    """ edit wizard """
