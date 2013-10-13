# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from os.path import join
from pyjavapropertiesu import encode_unicode, decode_unicode, Properties


def test_unicode_encode_embedded():
    generated = encode_unicode(open(join('test_data', 'test_input.txt'))
                    .read().rstrip().decode('utf-8'))
    assert generated == b'ab\\u00e4bc'


def test_unicode_encode_standalone():
    generated = encode_unicode(u'ä')
    assert generated == b'\\u00e4'


def test_unicode_encode_noop():
    """If the input isn't a unicode string, don't do anything."""
    assert encode_unicode(b'abcd') == b'abcd'


def test_unicode_decode():
    assert decode_unicode(b'\\u00e4') == u'ä'


def test_prop_decoding():
    props = Properties()
    with open(join('test_data', 'test.properties'), 'r') as fp:
        props.load(fp)
    assert props.getProperty(b'name') == u'üben'


def test_prop_encoding():
    """If you write unicode data to the properties dict, it should be encoded
    transparently to ascii."""
    props = Properties()
    props[b'name'] = u'ä'
    props.getPropertyDict()[b'name'] == b'\\u00e4'
