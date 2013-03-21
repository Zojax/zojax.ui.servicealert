##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
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
from zope import interface

from z3c.form.interfaces import HIDDEN_MODE

from zojax.layoutform import Fields, PageletEditForm
from zojax.wizard import Wizard, WizardStepForm

from ..interfaces import _, IConfigletEditWizard, IServiceAlert


class ConfigletEditWizard(Wizard):
    interface.implements(IConfigletEditWizard)

    prefix = 'configlet.'
    id = 'configlet-edit-wizard'
    label = _(u'Service Alert')

    @property
    def title(self):
        return self.context.__title__

    @property
    def description(self):
        return self.context.__description__


class ConfigletEditStep(WizardStepForm, PageletEditForm):

    name = 'configlet'
    title = _('Configlet')
    label = _('Configure configlet')

    @property
    def fields(self):
        fields = Fields(self.getContent().__schema__)
        fields['cookie'].mode = HIDDEN_MODE
        return fields

