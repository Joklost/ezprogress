ezprogress
----------
Simple, easy to use progress bar for Python 3.6+.

Installation
^^^^^^^^^^^^
``$ pip3 install ezprogress``

Usage
^^^^^
.. code:: python

    >>> from ezprogress.progressbar import ProgressBar
    >>> pb = ProgressBar(total=100, title='Progress')
    >>> pb.start()
    >>> for i in range(0, 100):
    >>>     pb.update(i)
    >>>     do_stuff(i)
    >>> pb.finished()
