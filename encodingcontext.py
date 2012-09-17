from codecs import lookup
import sys; reload(sys)
from sys import getdefaultencoding, setdefaultencoding


class encoding_context(object):
    r"""The context manager that temporarily configures the default
    encoding for strings.

    >>> with encoding_context('euc-kr'):
    ...     str(u'\ud55c\uae00')
    ...
    '\xc7\xd1\xb1\xdb'

    """

    def __init__(self, encoding):
        self.encoding = lookup(encoding)

    def __enter__(self):
        self.previous_encoding = getdefaultencoding()
        setdefaultencoding(self.encoding.name)
        return self.encoding

    def __exit__(self, exc_type, exc_value, traceback):
        setdefaultencoding(self.previous_encoding)
