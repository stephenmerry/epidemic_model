#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:42:19 2020

@author: stephen
"""
import epidemic_simulation as epi_sim

# Initialise Epidemic
epidemic_list = epi_sim.create_epidemic_list(list_of_individuals,
                                             initial_exposed, exposure_rates,
                                             infectious_rates, removal_rates)

# Run Gillespie Algorithm
epidemic_events = epi_sim.execute_gillespie_algorithm(epidemic_list)

# Visualise Epidemic spread


