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

from zope.i18nmessageid import MessageFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

_ = MessageFactory('zojax.ui.servicealert')

def alertColorsVocabulary(context):
    """ returns Colors for service alert message
    """
    vocab = SimpleVocabulary([
        SimpleTerm(u'blue', 'blue', 'Blue'),
        SimpleTerm(u'green', 'green', 'Green'),
        SimpleTerm(u'yellow', 'yellow', 'Yellow'),
        SimpleTerm(u'red', 'red', 'Red')])

    #vocab.getTerm(1).description = _('Description.')

    return vocab

