Isotherm fitting module (:py:mod:`pyAPEP.isofit`)
====================================================

This module enables to develop pure and mixture isotherm functions from pressure and uptake data samples.

First, import isofit into Python after installation.

.. code-block:: python

   import pyAPEP.isofit as isofit

In this module, four main functions exist.

   1. Finding best isotherm function (:py:mod:`isofit.best_isomodel`) 
   2. Fitting isotherm for different temperature (:py:mod:`isofit.fit_diffT`)
   3. Developing mixuture isotherm with RAST (:py:mod:`isofit.rast`)
   4. Developing mixuture isotherm with IAST (:py:mod:`isofit.iast`)

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


4. Developing mixuture isotherm with RAST
'''''''''''''''''''''''''''''''''''''''''''
RAST : Real adsorbed solution Theory

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

----------------------------------------

Function structures
---------------------

.. currentmodule:: pyAPEP.isofit

.. autofunction:: best_isomodel

.. currentmodule:: pyAPEP.isofit

.. autofunction:: fit_diffT

.. currentmodule:: pyAPEP.isofit

.. autofunction:: rast

.. currentmodule:: pyAPEP.isofit

.. autofunction:: IAST

------------------------------------------------

Theory
--------

Finding best isotherm function algorithm
''''''''''''''''''''''''''''''''''''''''''

이 알고리즘은 일반적으로 사용되는 5개의 isotherm function candidates 와 python optimizer candidate 로부터 주어진 data 에 가장 적절한 isothem function 과 그 parameter 를 도출한다. 알고리즘의 전반적인 내용은 아래 그림과 같다.

.. image:: images/Best_isotherm.png
  :width: 800
  :alt: Isotherm fitting algorithm
  :align: center



5개의 isotherm function 은 Arrh, Langmuir (Lang), Freundlich (Freu), Quadratic (Quad), Sips, Dual-site Langmuir (DSLang) 이며 각 수식은 아래와 같다. 

+-----------+--------+-----------------------------------------------------------------------+
| # of      | Name   | Equation                                                              |
|parameters |        |                                                                       |
+===========+========+=======================================================================+
|     1     | Arrh   | :math:`q(P) =`                                                        |
+-----------+--------+-----------------------------------------------------------------------+
|     2     | Lang   | :math:`q(P) = M\frac{KP}{1+KP}`                                       |
+           +--------+-----------------------------------------------------------------------+
|           | Freu   | :math:`q(P) = kP^n`                                                   |
+-----------+--------+-----------------------------------------------------------------------+
|     3     | Quad   | :math:`q(P) = M \frac{(K_a + 2 K_b P)P}{1+K_aP+K_bP^2}`               |
+           +--------+-----------------------------------------------------------------------+
|           | Sips   | :math:`q(P) =\frac{q_m K P^n}{1+K P^n}`                               |
+-----------+--------+-----------------------------------------------------------------------+
|     4     | DSLang | :math:`q(P) = M_1 \frac{K_1 P}{1+K_1 P} +  M_2 \frac{K_2 P}{1+K_2 P}` |
+-----------+--------+-----------------------------------------------------------------------+


.. note::
   사용자는 candidates 로 사용하고자 하는 모델의 parameter 개수를 고려하여 data sample 을 제공해야한다. 예를 들어 Dual site Langmuir 함수를 candidates 에 포함하고자 한다면 사용자는 3 개 이상의 data sample 이 필요하다.


Adosption at different temperature (using heat of adsorption)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. math::
   a(P, T) = \exp { \frac { \vartriangle H_{ads,i}}{R}\left( \frac{1}{T}-\frac{1}{T_{ref}}\right)},

where :math:`H_{ads,i}` is heat of adsorption and :math:`T_{ref}` is reference temperature.
   

Ideal adsorbed solution theory (IAST)
''''''''''''''''''''''''''''''''''''''''

IAST 는 component 간의 경쟁적인 흡착을 고려하여 pure isothrm function 으로부터 mixture isotherm function 을 도출한다.
IAST 는 아래 사항을 가정한다.

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


Real adsorbed solution theory (RAST)
''''''''''''''''''''''''''''''''''''''''

In the real adsorbed solution theory, the pressure is calculated with modified Raoults' law to consider the actual behavior with activity coefficient. Other equations and algorithm is the same with IAST.

**Modified Raoult' law**

.. math::
   y_i \phi  P = x_i \gamma_i P^{\circ}_i,

where  :math:`\phi` is fugacity coefficient and :math:`\gamma_i` is activity coefficient.

----------------------------------------
