``encodingcontext`` --- A bad idea about the default encoding
=============================================================

    | Although practicality beats purity.
    | Errors should never pass silently.
    | Unless explicitly silenced.

    --- Zen of Python

This small module implements a bad idea: making default encoding
explicitly scoped:

.. code-block:: pycon

   >>> with encoding_context('euc-kr'):
   ...     str(u'\ud55c\uae00')
   ...
   '\xc7\xd1\xb1\xdb'

Of course it has several shortcomings, and the most critical one is:
using it within ``thread``, ``threading``, ``greenlet``, ``tasklet``, etc
probably breaks its scoping.  If Python had dynamic scoping and default
encoding was defined as dynamically scoped variable, we might have more
convenient way to code between Unicode--byte strings.
