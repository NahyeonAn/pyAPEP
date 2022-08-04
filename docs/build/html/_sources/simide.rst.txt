Ideal PSA simulation module (:py:mod:`pyAPEP.simide`)
=======================================================
This module enables ideal PSA simulation using isotherm function and operating conditions.

First, import simide into Python after installation.

.. code-block:: python

   import pyAPEP.simide as simide

Then users need to 5-steps to simulate.
    1. Mixture isotherm function definition
    2. Ideal column definition
    3. Feed condition setting
    4. Operating condition setting
    5. Simulation run

In next section, detailed steps are explained.

Usage
-------

1. Mixture isotherm function definition

Here, we define the mixture isotherm function with :py:mod:`pyAPEP.isofit`.

.. code-block:: python

    iso_mix = lambda P,T: isof.IAST([iso1, iso2], P, T)
    # iso1 and iso2 == Pure isotherm function of each componet.

2. Ideal column definition

.. code-block:: python

    num_comp = 2                                       # The number of components
    Column1 = simi.IdealColumn(num_comp, iso_mix, )    # Ideal column definition
    print(Column1)                                     # Chek input condition

3. Feed condition setting

.. code-block:: python

    P_feed = 8                              # Feed presure (bar)
    T_feed = 300                            # Feed temperature (K)
    y_feed = [1/4, 3/4]                     # Feed mole fraction (mol/mol)
    
    Column1.feedcond(P_feed, T_feed, y_feed)
    print(Column1) 

4. Operating condition setting

.. code-block:: python

    P_high = 8                          # High pressure (bar)
    P_low  = 1                          # Low pressure (bar)
    
    Column1.opercond(P_high, P_low)
    print(Column1)

5. Simulation run

.. code-block:: python

    x_ext = Column1.runideal()
    print(x_ext)                        #return tail gas composition of each gas


Theory
-------
Here's theories.


Tutorials
---------


Class documentation and details
----------------------------------
.. automodule:: pyAPEP.simide
    :special-members:
    :members:


---------------------------------