"""
This library wraps pyjavaproperties to transparently store non-ascii values::

    props = Properties()
    props.load(open('messages_de.properties', 'r'))
    props.getProperty('section.key')
    ...
    props.setProperty('section.otherkey', u'unicode_data')
"""
from __future__ import unicode_literals

import codecs
import pyjavaproperties


def unicode_escape_handler(e):
    s = ''.join(u'\\u%04x' % ord(x) for x in e.object[e.start:e.end])
    return (s, e.end)


codecs.register_error('unicode_escape', unicode_escape_handler)


class Properties(pyjavaproperties.Properties):
    def getProperty(self, key, raw=None):
        value = super(Properties, self).getProperty(key)
        if raw:
            return value
        return decode_unicode(value)

    def setProperty(self, key, value, raw=None):
        if raw:
            return super(Properties, self).setProperty(key, value)
        return super(Properties, self).setProperty(key, encode_unicode(value))


def encode_unicode(value):
    if isinstance(value, str):
        return value
    return value.encode('ascii', 'unicode_escape')


def decode_unicode(value):
    return value.decode('unicode_escape')
