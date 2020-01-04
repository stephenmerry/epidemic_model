#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:42:19 2020

@author: stephen
"""
import population_creation as pop_crtn
import epidemic_simulation as epi_sim

EXPOSURE_RATE = 3/365
INFECTIOUS_RATE = 5/365
REMOVAL_RATE = 3/365

list_of_individuals = [str(i) for i in range(0, 40)]
initial_exposed = ['0', '3', '6', '8']
weighted_adjacency_matrix = pop_crtn.create_dummy_weighted_adjacency_matrix(40) / 10

# Initialise Population
weighted_adjacency_list = pop_crtn.create_weighted_adjacency_list(
        list_of_individuals, weighted_adjacency_matrix)

# Initialise Epidemic
exposure_rates, infectious_rates, removal_rates = epi_sim.create_identical_rate_arrays(len(list_of_individuals), EXPOSURE_RATE,
                                       INFECTIOUS_RATE, REMOVAL_RATE)
epidemic_list = epi_sim.create_epidemic_list(list_of_individuals,
                                             initial_exposed, exposure_rates,
                                             infectious_rates, removal_rates)

# Run Gillespie Algorithm
epidemic_events = epi_sim.execute_gillespie_algorithm(epidemic_list,
                                                      weighted_adjacency_list)

# Visualise Epidemic spread
epi_sim.print_out_epidemic_events(epidemic_events, 0.1)