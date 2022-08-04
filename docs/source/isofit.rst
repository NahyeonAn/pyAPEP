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

3. Developing mixuture isotherm with RAST
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

4. Developing mixuture isotherm with IAST
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

.. autofunction:: rast

.. currentmodule:: pyAPEP.isofit

.. autofunction:: IAST

------------------------------------------------

Theory
--------

Pure isotherm function condidates
''''''''''''''''''''''''''''''''''

   **1-parameter model**

      * Arrh
   
      .. math::

         q(P) = 
            
   **2-parameters models**

      * Langmuir isotherm model

      .. math::

         q(P) = M\frac{KP}{1+KP},

      * Freundlich isotherm model

      .. math::

         q(P) = kP^n,
         
   **3-parameters models**+

      * Quadratic isotherm model

      .. math::
         
         q(P) = M \frac{(K_a + 2 K_b P)P}{1+K_aP+K_bP^2}

      * Sips adsorption isotherm

      .. math::

         q(P) =\frac{q_m K P^n}{1+K P^n}
         
   **4-parameters models**

      * Dual-site Langmuir (DSLangmuir) adsorption isotherm

      .. math::

         q(P) = M_1 \frac{K_1 P}{1+K_1 P} +  M_2 \frac{K_2 P}{1+K_2 P}

blalba
'''''''

.. math::
   a(P, T) = \exp { \frac { \vartriangle H_{ads,i}}{R}\left( \frac{1}{T}-\frac{T}{T_{ref}}\right)},

where :math:`H_{ads,i}` is heat of adsorption and :math:`T_{ref}` is reference temperature.

blalba
''''''''''

    **Modified Raoult' law**

    .. math::
      y_i \phi  P = x_i \gamma_i P^{\circ}_i,

   where  :math:`\phi` is fugacity coefficient and :math:`\gamma_i` is activity coefficient.

blablaaa
''''''''''

**Raoult' law**

   .. math::

      P^{\circ}_i = y_i \frac{P}{x_i}
----------------------------------------