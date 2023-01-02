Isotherm fitting module (:py:mod:`pyAPEP.isofit`)
====================================================

This module enables to develop pure and mixture isotherm functions from pressure and uptake data samples.

First, import isofit into Python after installation.

.. code-block:: python

   import pyAPEP.isofit as isofit

In this module, three main functions exist.

   1. Finding best isotherm function (:py:mod:`isofit.best_isomodel`) 
   2. Fitting isotherm for different temperature (:py:mod:`isofit.fit_diffT`)
   3. Developing mixuture isotherm with RAST (:py:mod:`isofit.rast`)

Detailed description of each function are described in next senction.
The explanation include function usage, algorithm (or related theroy), and function structure.

---------------------

Usage
------

1. Finding best isotherm function
'''''''''''''''''''''''''''''''''''''

Function to find best isotherm model for given datast with multiple isotherm and optimizer candidates.


.. code-block:: python

   # Data import
   P = [2, 3, 4, 5]
   q = [1, 2, 3, 4]

   # Find best isotherm function
   best_isotherm, parameters, fn_type, val_err = isofit.best_isomodel(P, q)

2. Fitting isotherm for different temperature
'''''''''''''''''''''''''''''''''''''''''''''''''

Using heat of adsorption, isotherm parameter fitting at different temperature.

.. code-block:: python

   # Data import
   P = [2, 3, 4, 5]
   q = [1, 2, 3, 4]

   # Find best isotherm function
   best_isotherm, parameters, fn_type, val_err = isofit.best_isomodel(P, q)

3. Developing mixuture isotherm with IAST
'''''''''''''''''''''''''''''''''''''''''''

IAST : Ideal adsorbed solution Theory

**Option 1)** Users can define their own isotherm function for each components,

.. code-block:: python

   # Pure isotherm definition
   def iso1(P, T):
    nume =1*0.05*P
    deno = 1+0.05*P
    q = nume/deno
    return q

   def iso2(P,T):
      nume = 2*0.1*P
      deno = 1+0.1*P
      q = nume/deno
      return q

   # Develop mixture isotherm
   iso_mix = lambda P,T : isof.IAST([iso1, iso2], P, T)

**Option 2)** Or use developed isotherm function from :py:mod:`isofit.best_isomodel`

.. code-block:: python

   P = [2, 3, 4, 5]
   q_comp1 = [1, 2, 3, 4]     # Gas adsorption of component 1
   q_comp2 = [1, 5, 7, 10]    # Gas adsorption of component 2

   # Define pure isotherm of each component
   iso1, param1, fn_type1, val_err1 = isofit.best_isomodel(P, q_comp1)
   iso2, param2, fn_type2, val_err2 = isofit.best_isomodel(P, q_comp2)
   
   # Develop mixture isotherm
   iso_mix = lambda P,T : isof.IAST([iso1, iso2], P, T)

----------------------------------------

Function structures
---------------------

.. currentmodule:: pyAPEP.isofit

.. autofunction:: best_isomodel

.. currentmodule:: pyAPEP.isofit

.. autofunction:: fit_diffT

.. currentmodule:: pyAPEP.isofit

.. autofunction:: IAST

------------------------------------------------

Theory
--------

Finding best isotherm function algorithm
''''''''''''''''''''''''''''''''''''''''''
 
This module enables to automatically develop pure and mixture isotherm functions from pressure and uptake data samples. Below figure shows the schematic diagram of the algorithm to find the best isotherm function.

.. image:: images/algorithm.png
  :width: 500
  :alt: Isotherm fitting algorithm
  :align: center

Objective function of isotherm fitting
*********************************************

Estimation of the isotherm function is the same as solving an optimization problem as the following equation.

.. math::

    J = \min_{K_1, K_2, ...} \left( \sum_{i=1}^{N_{fit}} (q_i-\hat{q}_i)^2 \right )

.. math::

    \hat{q} = f(P, T, K_1, K_2, ...)

where :math:`q`, :math:`N_{fit}`, and :math:`K` refer to gas uptake, the number of data samples for isotherm fitting, and isotherm parameters, respectively. :math:`f` means the isotherm function, and :math:`\hat{q}` is the predicted uptake from :math:`f`. By solving the objective function, the isotherm parameters are derived that satisfy the minimum error between actual and predicted uptake data.

Optimization with multiple optimization methods
***************************************************

To find the best isotherm parameters, isofit module considers five optimization solvers. Optimization solvers are given by the public python package, scipy, and those are Nelder-mead, Powell, COBYLA, shgo, and differential evolution. The solver with the minimum objective function is selected and the isotherm function is derived as the following equation.

.. math::

    f = \arg\min_{solver}(J)

Isotherm model selection
********************************

:py:mod:`isofit.best_isomodel` automatically find the best isotherm function by applying the above equations to five different isotherm functions. Five isotherm functions are described in below table. Then, the solvers and parameters could be found for each isotherm function. Among isotherm functions, a function with the smallest objective function value is selected as the best isotherm function.


+-----------+--------+--------------------------------------------------------------------------------------------+
| # of      | Name   | Equation                                                                                   |
|parameters |        |                                                                                            |
+===========+========+============================================================================================+
|     1     | Arrh   | :math:`q(P) =e^{\frac{\vartriangle H}{R} \left (\frac {1}{T}-\frac {1}{T_{ref}} \right)}`  |
+-----------+--------+--------------------------------------------------------------------------------------------+
|     2     | Lang   | :math:`q(P) = M\frac{KP}{1+KP}`                                                            |
+           +--------+--------------------------------------------------------------------------------------------+
|           | Freu   | :math:`q(P) = kP^n`                                                                        |
+-----------+--------+--------------------------------------------------------------------------------------------+
|     3     | Quad   | :math:`q(P) = M \frac{(K_a + 2 K_b P)P}{1+K_aP+K_bP^2}`                                    |
+           +--------+--------------------------------------------------------------------------------------------+
|           | Sips   | :math:`q(P) =\frac{q_m K P^n}{1+K P^n}`                                                    |
+-----------+--------+--------------------------------------------------------------------------------------------+
|     4     | DSLang | :math:`q(P) = M_1 \frac{K_1 P}{1+K_1 P} +  M_2 \frac{K_2 P}{1+K_2 P}`                      |
+-----------+--------+--------------------------------------------------------------------------------------------+


.. note::
   The user should provide a data sample in consideration of the number of parameters of the model to be used as candidates. For example, if you want to include the Dualsite Langmuir function in candates, the user needs more than three data samples.


Adosption at different temperature (using heat of adsorption)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. math::
   a(P, T) = \exp { \frac { \vartriangle H_{ads,i}}{R}\left( \frac{1}{T}-\frac{1}{T_{ref}}\right)},

where :math:`H_{ads,i}` is heat of adsorption and :math:`T_{ref}` is reference temperature.
   

Ideal adsorbed solution theory (IAST)
''''''''''''''''''''''''''''''''''''''''

IAST derives a mixture function from pure isothrm functions in consideration of competitive adsorption between components.
IAST assumes the following:

   * The temperature is fixed and the pure isotherm are measured at the same temperature.
   * The thermodynamic property of the adsorbent during the adsorption is negligible.
   * Each adsorbate has access to the same area of adsorbent surface.
   * A Gibbs dividing surface defines an adsorbed phase.

From Raoults' law, we need to find solid mole fraction :math:`x_i`, which is the uptake.

**Raoult' law**

.. math::

   P^{\circ}_i = y_i \frac{P}{x_i}

**Spreading pressure**

.. math::

   \pi_i^{\circ} = \frac{\pi_i}{R T} = \int_{0}^{P^{\circ}} \frac{f_i(P)}{P}, dP

where, :math:`\pi_i^{\circ}` is the reduced spreading pressure, :math:`f_i(P)` is the pure isotherm model.

For components :math:`i = 1, 2, ..., N`, the pure component spreading pressure :math:`\pi_i` at pressure :math:`P^{\circ}_i` are all equal to the spreading pressure of the mixture :math:`\pi`.

.. math::
   \pi = \pi_1(P^0_1) = \pi_2(P^0_2) = \cdots = \pi_N(P^0_N)

.. math::

   \min_{x_1, x_2, ... x _N} \sum_{i=1}^N \sum_{j \ne i}^{N-1} (\pi^{\circ}_i - \pi^{\circ}_j)^2

Find the spreading pressure for all components with :math:`x_{guess}`, until that spreading pressure of mixture is the same with that of each components.
check the spreading pressure from :math:`x_i` until the difference between :math:`\pi_i` and :math:`\pi_j` becomes smaller than the tolerance.

----------------------------------------
