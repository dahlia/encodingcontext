``encodingcontext`` --- A bad idea about the default encoding
=============================================================

    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.

    --- Zen of Python

.. code-block:: pycon

   >>> with encoding_context('euc-kr'):
   ...     str(u'\ud55c\uae00')
   ...
   '\xc7\xd1\xb1\xdb'
