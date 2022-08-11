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

------------------------------------------------------

Usage
-------

1. Mixture isotherm function definition
''''''''''''''''''''''''''''''''''''''''''''''

Here, we define the mixture isotherm function with :py:mod:`pyAPEP.isofit`.

.. code-block:: python

    iso_mix = lambda P,T: isof.IAST([iso1, iso2], P, T)
    # iso1 and iso2 == Pure isotherm function of each componet.

2. Ideal column definition
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    num_comp = 2                                       # The number of components
    Column1 = simi.IdealColumn(num_comp, iso_mix, )    # Ideal column definition
    print(Column1)                                     # Chek input condition

3. Feed condition setting
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    P_feed = 8                              # Feed presure (bar)
    T_feed = 300                            # Feed temperature (K)
    y_feed = [1/4, 3/4]                     # Feed mole fraction (mol/mol)
    
    Column1.feedcond(P_feed, T_feed, y_feed)
    print(Column1) 

4. Operating condition setting
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    P_high = 8                          # High pressure (bar)
    P_low  = 1                          # Low pressure (bar)
    
    Column1.opercond(P_high, P_low)
    print(Column1)

5. Simulation run
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    x_ext = Column1.runideal()
    print(x_ext)                        #return tail gas composition of each gas

----------------------------------------

Class documentation
----------------------------------
.. automodule:: pyAPEP.simide
    :special-members:
    :members:


---------------------------------

Theory
-------

(공정 그림 있으면 설명하기 쉬울듯 with notation)

Ideal PSA 의 주요 assumption 은 아래와 같다.

    *	Extremely fast mass & heat transfer between gas and solid phases
    *	The operation of the ideal PSA process is isothermal by perfectly controlling temperature.
    *	The operation cycle consists of two steps: adsorption and desorption steps.
    *	During the adsorption step, 100% of raffinate gas is produced and the capacity of the adsorbent bed is fully used with perfectly controlled step time.
    *	During the desorption step, the detrimental influence of the void fraction on the tail gas purity is ignored.
    *	Uniform pressure distribution is assumed all along the adsorbent bed of the PSA process.

Ideal PSA simulation 을 통해 tail gas 에서의 조성을 도출할 수 있으며, :math:`x_{guess}` 와 계산된 :math:`x` 와의 mismatch 를 최소화 하는 방향으로 solution 이 도출된다.

.. math::

    \min_{x_{guess}} ||x_i-x_{guess}||^2_2

such that

    .. math::

        x = \frac{\vartriangle q_1}{\vartriangle q_1 + \vartriangle q_2}

    .. math::

        \vartriangle q_1 = q_{1,high} - q_{1,low}

    .. math::

        \vartriangle q_2 = q_{2,high} - q_{2,low}

    .. math::

        q_{1,high}, q_{2,high} = f_{IAST} \left(P_{high}, T, y \right )

    .. math::

        q_{1,low}, q_{2,low} = f_{IAST} \left(P_{low}, T, x_{guess} \right )

where :math:`y` is the mole fraction in gas phase during the adsorption step.


--------------------------------