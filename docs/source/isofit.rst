Isotherm fitting module (:py:mod:`pyAPEP.isofit`)
====================================================

detailed discriptions are here.


Tutorials
------------------
For this tutorial on pyIAST, enter the `/test` directory of pyIAST. While you can type this code into the Python shell, I highly recommend instead opening a `Jupyter Notebook <http://jupyter.org/>`_.

First, import pyIAST into Python after installation.

.. code-block:: python

   import pyAPEP.isofit as isofit

For our tutorial, we have the pure-component methane and ethane adsorption isotherm data for metal-organic framework IRMOF-1 in Fig 1. We seek to predict the methane and ethane uptake in the presence of a binary mixture of methane and ethane in IRMOF-1 at the same temperature. As an example for this tutorial, we seek to predict the methane and ethane uptake of IRMOF-1 in the presence a 5/95 mol % ethane/methane mixture at a total pressure of 65.0 bar and 298 K.

In this module, four main functions exist.

1. Finding best isotherm function (:py:mod:`best_isomodel`) 
2. Fitting isotherm for different temperature (:py:mod:`fit_diffT`)
3. Developing mixuture isotherm with RAST (:py:mod:`rast`)
4. Developing mixuture isotherm with IAST (:py:mod:`iast`)



1. Finding best isotherm function
----------------------------------

Function to find best isotherm model for given datast with multiple isotherm and optimizer candidates.

Pure isotherm function condidates
''''''''''''''''''''''''''''''''''

   **1-parameter model**

      * Arrh

      .. math::

         q(P) = 
            
   **2-parameters models**

      * Langmuir isotherm model

      .. math::

         q(P) = M\\frac{KP}{1+KP},

      * Freundlich isotherm model

      .. math::

         q(P) = kP^n,
         
   **3-parameters models**

      * Quadratic isotherm model

      .. math::
         
         q(P) = M \\frac{(K_a + 2 K_b P)P}{1+K_aP+K_bP^2}

      * Sips adsorption isotherm

      .. math::

         q(P) = \\frac{q_m K P^n}{1+K P^n}
         
   **4-parameters models**

      * Dual-site Langmuir (DSLangmuir) adsorption isotherm

      .. math::

         q(P) = M_1\\frac{K_1 P}{1+K_1 P} +  M_2\\frac{K_2 P}{1+K_2 P}

.. currentmodule:: pyAPEP.isofit

.. autofunction:: best_isomodel

2. Fitting isotherm for different temperature
----------------------------------------------
Using heat of adsorption, isotherm parameter fitting at different temperature.

.. math::
   a(P, T) = \\exp {\\frac{\\vartriangle H_{ads,i}}{R}(\\frac{1}{T}-\\frac{T}{T_{ref}})},

where :math:`H_{ads,i}` is heat of adsorption and :math:`T_{ref}` is reference temperature.

.. currentmodule:: pyAPEP.isofit

.. autofunction:: fit_diffT

3. Developing mixuture isotherm with RAST
----------------------------------------------
RAST : Real adsorbed solution Theory

    **Modified Raoult' law**

    .. math::
      y_i \\phi  P = x_i \\gamma_i P^{\\circ}_i,

   where  :math:`\\phi` is fugacity coefficient and :math:`\\gamma_i` is activity coefficient.

.. currentmodule:: pyAPEP.isofit

.. autofunction:: rast

4. Developing mixuture isotherm with IAST
----------------------------------------------
IAST : Ideal adsorbed solution Theory

    **Raoult' law**

    .. math::
      P^{\\circ}_i = y_i \\frac{P}{x_i}

.. currentmodule:: pyAPEP.isofit

.. autofunction:: IAST
