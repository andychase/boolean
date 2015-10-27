booleanp
=======

Converts strings such as "true", "True", "y", "n", ... to their equivalent Boolean value.

Installation
------------

.. ::

  $ pip install booleanp

Usage
-----

.. ::

  >>> from booleanp import boolean
  >>> boolean('True')
  True
  >>> boolean('t')
  True
  >>> boolean('f')
  False
  >>> boolean('False')
  False

