#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:36:43 2020

@author: stephen
"""

import numpy as np
    
def create_identical_rate_arrays(array_length, EXPOSURE_RATE, 
                                    INFECTIOUS_RATE, REMOVAL_RATE):
    """Creates arrays detailing the exposure, infectious and removal rates for
        the epidemic. Will only be used when the epidemic rates are assumed to 
        be identical for each individual.
    """
    exposure_rates = np.ones(array_length) * EXPOSURE_RATE
    infectious_rates = np.ones(array_length) * INFECTIOUS_RATE
    removal_rates = np.ones(array_length) * REMOVAL_RATE
    return exposure_rates, infectious_rates, removal_rates

def create_epidemic_list(list_of_individuals, initial_exposed, exposure_rates,
                         infectious_rates, removal_rates):
    """
    Creates a list of lists. Each list contains the name, state and epidemic
    rates of the individual
    """
    epidemic_list = []
    state_list = ["Susceptible"] * len(list_of_individuals)
    for i in initial_exposed:
        state_list[list_of_individuals.index(i)] = "Exposed"
    for i in range(0, len(list_of_individuals)):
        individual_list = [list_of_individuals[i], state_list[i], 
                           exposure_rates[i], infectious_rates[i], 
                           removal_rates[i]]
        epidemic_list.append(individual_list)
    return epidemic_list

"""
def initialise_epidemic(list_of_individuals, initial_exposed, EXPOSURE_RATE, 
                        INFECTIOUS_RATE, REMOVAL_RATE):
    exposure_rates, infectious_rates, removal_rates = create_rate_arrays(
            len(list_of_individuals), EXPOSURE_RATE, INFECTIOUS_RATE, 
            REMOVAL_RATE)
    epidemic_list = create_epidemic_list(list_of_individuals, initial_exposed,
                                         exposure_rates, infectious_rates,
                                         removal_rates)
    return epidemic_list
"""

def check_current_state(epidemic_list):
    exposed_condition = any(i[1] == "Exposed" for i in epidemic_list)
    infectious_condition = any(i[1] == "Infectious" for i in epidemic_list)
    return (exposed_condition) or (infectious_condition)

def create_state_dict(epidemic_dict):
    individual_states = {}
    for i in epidemic_dict:
        individual_states[i] = epidemic_dict[i].get('state')
    state_dict = invert_dict(individual_states)
    return state_dict

def determine_possible_events(epidemic_dict):
    state_dict = create_state_dict(epidemic_dict)
    
    return possible_events

def advance_algorithm(epidemic_dict, epidemic_events):
    possible_events = determine_possible_events(epidemic_dict)
    calculate_time_step
    choose_event
    update_epidemic_dict
    return epidemic_dict, epidemic_events

def execute_gillespie_algorithm(epidemic_list, exposure_rates, 
                                infectious_rates, removal_rates):
    epidemic_events = []
    while check_current_state(epidemic_list):
        epidemic_list, epidemic_events = advance_algorithm(epidemic_list,
                                                            epidemic_events)
    return epidemic_events












def determine_exposure_events():
    return

def determine_transition_events(inverted_state, token):
    if token in inverted_state:
        transition_events = ['Individual {} transitions to {}'.format(i, token) 
                                for i in inverted_state['Exposed']]
    else:
        transition_events = []
    return transition_events

def determine_infectious_events(inverted_state):
    if 'Exposed' in inverted_state:
        infectious_events = ['Individual {} becomes infectios'.format(i) 
                                for i in inverted_state['Exposed']]
    else:
        infectious_events = []
    return infectious_events

def determine_removal_events(inverted_state):
    if 'Removed' in inverted_state:
        removal_events = ['Individual {} is removed'.format(i) 
                            for i in inverted_state['Removed']]
    else:
        removal_events = []
    return removal_events




    
