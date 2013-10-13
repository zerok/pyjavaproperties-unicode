This is a tiny wrapper around the pyjavaproperties package that does
unicode en- and decoding transparently.

The problem I tried to solve here is that Java Properties files only
support ISO-8859-1 content. If you need unicode, you have to use
something like `native2ascii`_ or `propedit`_ for Eclipse which
converts content from unicode to ascii and stores it into the 
respective file. In Python, obviously, you want the actual unicode
data and not the encoded version of the prop value and this is
exactly what this here does.

To use it simply import the ``Properties`` class from the
``pyjavapropertiesu`` module instead of ``pyjavaproperties`` and use
the ``getProperty`` method as before.

Please note, though, that the data within the internal dict in the Properties
class is still encoded.

.. _`native2ascii`: http://docs.oracle.com/javase/7/docs/technotes/tools/windows/native2ascii.html
.. _`propedit`: http://propedit.sourceforge.jp/index_en.html
