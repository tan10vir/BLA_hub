
.. _install:

Installation
============

``bayesvp`` is originally written and tested for Python 2.7. For Python 3.6 and above see the instructions below.

Dependencies
------------
``bayesvp`` depends on:

    - numpy_
    - scipy_
    - matplotlib_
    - pyfits_

You can install these using your favorite Python package manager such as pip_ or conda_.

It also depends on the following MCMC samplers:

    + emcee_
    + kombine_

The above samplers can be installed using pip_ :

::

    pip install emcee

    pip install –user git+git://github.com/bfarr/kombine

You might need to run this using ``sudo`` depending on your Python installation.

Using pip
---------

The easiest way to install the stable version of ``bayesvp`` is using pip_ with the ``--user`` flag:

::

    pip install bayesvp --user

To install it system-wide and you might need to add ``sudo`` in the beginning.

From source
-----------

Alternatively, you can get the source by cloning `the git repository <https://github.com/cameronliang/bayesvp.git>`_:

::

    git clone https://github.com/cameronliang/bayesvp.git

Once you've downloaded the source, you can navigate to the root directory and run:

::

    python setup.py install

For Python 3.6 and above
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users with Python 3.6 and above need to convert the downloaded source code scripts to Python 3 using the python package 2to3_.

For example to convert a file named *config.py* type:

::

  2to3 -w config.py

Once all the python scripts are converted to Python 3, run:

::

    python setup.py install

Test the installation
---------------------

If the installation went smoothly, you should run a unit tests to ensure the package works as expected. The simplest way to do this is inside a python shell:

::

    import bayesvp
    from bayesvp.tests import run_tests

The output should look something like this:

::

    The output should look something like this:

    test_config_file_exists (bayesvp.tests.test_config.TCConfigFile) ... ok
    test_default_no_continuum_params (bayesvp.tests.test_config.TCConfigFile) ... ok
    test_example_mcmc_params (bayesvp.tests.test_config.TCConfigFile) ... ok
    ...
    test_prior (bayesvp.tests.test_likelihood.TCPosterior) ... ok
    test_general_intensity (bayesvp.tests.test_model.TCSingleVP) ... ok
    test_simple_spec (bayesvp.tests.test_model.TCSingleVP) ... ok

    ----------------------------------------------------------------------
    Ran 13 tests in 3.654s

    OK

Test run result with **no error** would ensure that ``bayesvp`` is successfully installed.

.. _pip: https://pip.pypa.io/en/stable/installing/
.. _conda: http://conda.pydata.org/docs/

.. _numpy: http://www.numpy.org/
.. _scipy: https://scipy.org/
.. _matplotlib: https://matplotlib.org/
.. _pyfits: https://pythonhosted.org/pyfits/

.. _emcee: https://emcee.readthedocs.io/en/stable/
.. _kombine: https://cosmosis.readthedocs.io/en/latest/reference/samplers/kombine.html

.. _2to3: https://pypi.org/project/2to3/
