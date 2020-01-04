#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:36:43 2020

@author: stephen
"""
import time
import numpy as np
import itertools
    
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

def check_current_state(epidemic_list):
    """Checks if any individuals are either exposed or infectious. If not, 
    the epidemic has ended.
    """
    exposed_condition = any(i[1] == "Exposed" for i in epidemic_list)
    infectious_condition = any(i[1] == "Infectious" for i in epidemic_list)
    return (exposed_condition) or (infectious_condition)

def produce_exposure_events(epidemic_list, weighted_adjacency_list):
    """Produces a list of the possible events where a susceptible individual
    is exposed to the epidemic by an infectious individual"""
    susceptible_inds = [item for item in epidemic_list if item[1] == "Susceptible"]
    infectious_inds = [item for item in epidemic_list if item[1] == "Infectious"]
    cartesian_product = list(itertools.product([i[0] for i in infectious_inds], 
                                   [i[0] for i in susceptible_inds]))
    exposure_events = []
    for i in cartesian_product:
        for j in weighted_adjacency_list:
            if j[0] == i:
                exposure_events.append(["Exposed", j[0][1], j[0][0], j[1]])
    return exposure_events

def produce_infectious_events(epidemic_list):
    """Produces a list of the possible events where an exposed individual
    becomes infectious"""
    exposed_inds = [item for item in epidemic_list if item[1] == "Exposed"]
    infectious_events = [["Infectious", i[0], i[3]] for i in exposed_inds]
    return infectious_events

def produce_removal_events(epidemic_list):
    """Produces a list of the possible events where an infectious individual
    is removed from the population"""
    infectious_inds = [item for item in epidemic_list if item[1] == "Infectious"]
    removal_events = [["Removed", i[0], i[3]] for i in infectious_inds]
    return removal_events

def determine_possible_events(epidemic_list, weighted_adjacency_list):
    """Creates a list of the possible events that could happen"""
    exposure_events = produce_exposure_events(epidemic_list, 
                                              weighted_adjacency_list)
    infectious_events = produce_infectious_events(epidemic_list)
    removal_events = produce_removal_events(epidemic_list)
    possible_events = exposure_events + infectious_events + removal_events
    return possible_events

def calculate_time_step(possible_events):
    """Calculate the time until the next event by taking an exponential random
    number with the sum of the event rates as the mean parameter"""
    time_step = np.random.exponential(
            scale=sum([i[-1] for i in possible_events]))     
    return time_step

def choose_event(possible_events):
    """Choose an event randomly using the event rates as a distribution"""
    rates = np.array([i[-1] for i in possible_events])
    probabilities = rates / sum(rates)
    chosen_index = np.random.choice(range(0, len(possible_events)),
                                    p=probabilities)
    chosen_event = possible_events[chosen_index][:-1]
    return chosen_event

def update_epidemic_list(epidemic_list, chosen_event):
    """Update the state of the individual who is involved in chosen_event"""
    epidemic_list[[i[0] for i in epidemic_list].index(
            chosen_event[1])][1] = chosen_event[0]
    return epidemic_list

def advance_algorithm(epidemic_list, weighted_adjacency_list, epidemic_events):
    """Advances the algorithm one step by determining the possible events, then
    choosing the next event and calculating the time until it happens. Then the
    event and any state changes are recorded."""
    possible_events = determine_possible_events(epidemic_list,
                                                weighted_adjacency_list)
    time_step = calculate_time_step(possible_events)
    chosen_event = choose_event(possible_events)
    epidemic_events.append([time_step] + chosen_event)
    epidemic_list = update_epidemic_list(epidemic_list, chosen_event) 
    return epidemic_list, epidemic_events

def execute_gillespie_algorithm(epidemic_list, weighted_adjacency_list):
    """Implements Gillespie's algorithm, as long as there are exposed or 
    infectious individuals in the population"""
    epidemic_events = []
    while check_current_state(epidemic_list):
        epidemic_list, epidemic_events = advance_algorithm(epidemic_list,
                                                           weighted_adjacency_list,
                                                           epidemic_events)
    return epidemic_events

def transform_epidemic_events(epidemic_events):
    """Changes the layout of the epidemic events for clarity and readability"""
    transformed_events = []
    for event in epidemic_events:
        if event[1] == "Exposed":
            current_event = "{} was {} to the disease by {}".format(
                    event[-2], event[1].lower(), event[-1])
        elif event[1] == "Infectious":
            current_event = "{} became {}".format(event[-1], event[1].lower())
        elif event[1] == "Removed":
            current_event = "{} was {}".format(event[-1], event[1].lower())
        transformed_events.append(current_event)
    return transformed_events

def print_out_epidemic_events(epidemic_events, time_lag=0):
    """For each event, we print out the event and take a short time_lag before 
    printing out the next event
    """
    event_times = np.cumsum([i[0] for i in epidemic_events])
    transformed_events = transform_epidemic_events(epidemic_events)
    for event in zip(event_times, transformed_events):
        print("At time {}, {}".format(event[0], event[1]))
        time.sleep(time_lag)