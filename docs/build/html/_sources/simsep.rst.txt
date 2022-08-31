Real PSA simulation module (:py:mod:`pyAPEP.simsep`)
=======================================================
This module enables ideal PSA simulation using isotherm function and operating conditions.

First, import simsep into Python after installation.

.. code-block:: python

   import pyAPEP.simsep as simsep

Then users need to 10-steps to simulate.
    1. Extended Langmuir isotherm
    2. Ideal column definition
    3. Adsorbent information
    4. Gas property information 
    5. Mass transfer information
    6. Thermal information 
    7. Boundary condition setting
    8. Initial condition setting
    9. Simulation run
    10. Graph

In next section, detailed steps are explained.

------------------------------------------------------
Usage
-------

1. Extended Langmuir isotherm
''''''''''''''''''''''''''''''''''''''''''''''

.. math::

    q_{i} = \frac{q_{m,i}b_{i}P_{i}}{1+\sum^{n}_{j=1}b_{j}P_{j}}

First, we need to import some libraries.

.. code-block:: python

    import numpy as np 
    import matplotlib.pyplot as plt

Then, define some parameters of the extended Langmuir isotherm.

.. code-block:: python

    qm1 = 1
    qm2 = 0.1
    b1 = 0.5
    b2 = 0.05

The extended Langmuir isotherm is defined as follows.
    
.. code-block:: python

    def extLang(P, T):
        P1 = P[0]
        P2 = P[1]
        deno = 1 + b1*P1 + b2*P2
        q1 = qm1*b1*P1 / deno
        q2 = qm2*b2*P2 / deno
        return q1, q2

2. Ideal column definition
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    col_len         = 1                                          # Length of the column (m)
    cross_sect_area = 0.0314                                     # Cross sectional area (m^2)
    num_comp        = 2                                          # The number of components
    Column1 = simsep.column(col_len, cross_sect_area, num_comp)  # Ideal column definition                               
    print(Column1)                                               # Check 

3. Adsorbent information
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    voidfrac = 0.4                                          # Void fraction
    rho      = 1100                                         # Solid density (kg/m^2)
    Column1.adsorbent_info(extLang, voidfrac, rho_s = rho)  # Adsorbent information
    print(Column1)                                          # Check 

4. Gas property information 
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    Mmol = [0.032, 0.044]   # Molecular weights of gases (kg/mol)                    
    visc = [0.01, 0.01]     # Viscosities of gases (Pa sec)
    
    Column1.gas_prop_info(Mmol, visc) # Gas property information
    print(Column1)                    # Check 

5. Mass transfer information 
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    MTC = [0.05, 0.05]      # Mass transfer coefficients                    
    a_surf = 400            # Volumatric specific surface area (m2/m3)
    
    Column1.mass_trans_info(MTC, a_surf) # Mass transfer information
    print(Column1)                       # Check

6. Thermal information 
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    dH_ads = [1000,1000]    # Heat of adsorption (J/mol)                    
    Cp_s = 5                # Solid heat capacity (J/kg K)
    Cp_g = [10,10]          # Gas heat capacity (J/mol K)
    h_heat = 10             # Heat transfer coefficient between solid and gas (J/m^2 K s)
    
    Column1.thermal_info(dH_ads, Cp_s, Cp_g, h_heat) # Mass transfer information
    print(Column1)                       # Check

7. Boundary condition setting 
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    P_inlet  = 9              # Inlet pressure  (bar)                 
    P_outlet = 8.0            # Outlet pressure (bar)
    T_feed   = 300            # Feed in temperature (K)
    y_feed = [0.5,0.5]        # Feed composition (mol/mol)
    
    Column1.boundaryC_info(P_outlet, P_inlet, T_feed, y_feed) # Boundary condition
    print(Column1)                                            # Check

8. Initial condition setting 
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    P_init = 8*np.ones(11)                       # Initial pressure (bar)                
    y_init = [0.2*np.ones(11), 0.8*np.ones(11)]  # Gas phase mol fraction (mol/mol)
    Tg_init = 300*np.ones(11)                    # Initial gas temperature (K)
    Ts_init = 300*np.ones(11)                    # Initial solid temperature (K)
    
    P_partial = [P_init*y_init[0], P_init*y_init[1]] # Partial pressure (bar)
    q_init = extLang(P_partial, Ts_init)             # Solid phase uptake (mol/kg)
    
    Column1.initialC_info(P_init, Tg_init, Ts_init, y_init, q_init) # Initial condition
    print(Column1)                                                  # Check


9. Simulation run
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    y,z, t = Column1.run_mamoen(2000, n_sec=10, CPUtime_print=True)
    
10. Graph
''''''''''''''''''''''''''''''''''''''''''''''

.. code-block:: python

    Column1.Graph_P(200)                                                                            # Graph 1
    Column1.Graph(200, 0, yaxis_label='Gas Concentration (mol/m$^3$)', loc = [0.9, 0.95])           # Graph 2
    Column1.Graph(200, 2, yaxis_label='Soild concentration (uptake) (mol/kg)', loc = [0.9, 0.95])   # Graph 3

The results are shown in Fig. 1,2, and 3.

.. image:: images/simsep_graph_1.png
  :width: 400
  :alt: simsep graph 1
  :align: center

   Fig. 1. Simsep graph 1
   
.. image:: images/simsep_graph_1.png
  :width: 400
  :alt: simsep graph 2
  :align: center

   Fig. 2. Simsep graph 2

.. image:: images/simsep_graph_3.png
  :width: 400
  :alt: simsep graph 3
  :align: center

   Fig. 3. Simsep graph 3
   
----------------------------------------

Class documentation
----------------------------------
.. automodule:: pyAPEP.simsep
    :special-members:
    :members:


---------------------------------

Theory
-------

`Ergun equation <http://dns2.asia.edu.tw/~ysho/YSHO-English/2000%20Engineering/PDF/Che%20Eng%20Pro48,%2089.pdf>`_ 

The Ergun equation, shown below, is used to describe the flow.

.. math::

    \frac{\vartriangle P}{L} = \frac{180 \mu }{d_{p}^2 } \frac{(1 - \epsilon)^2}{\epsilon^3} u + \frac{7}{4} \frac{\rho_{f}}{d_{P}} \frac{1 - \epsilon}{\epsilon^3} u^2

where

    * :math:`\vartriangle P =` Pressure drop
    * :math:`L =` Height of the bed
    * :math:`\mu =` Fluid viscosity
    * :math:`\epsilon =` Void space of the bed
    * :math:`u =` Fluid superficial velocity
    * :math:`d_{P} =` Particle diameter
    * :math:`\rho_{f} =` Density of Fluid

The Ergun equation represents the relationship between pressure drop and resultant fluid flow in packed beds.
The equation was developed by Sabri Ergun and he derived it from experimental measurments and theoretical postulates.


--------------------------------