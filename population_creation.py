#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:25:23 2020

@author: stephen
"""

import numpy as np

def create_dummy_weighted_adjacency_matrix(num_individuals):
    """Creates a symmetric dummy weighted adjacency matrix that we can use to 
    test our simulations on."""
    weighted_adjacency_matrix = (np.random.rand(num_individuals,
                                               num_individuals) * 2)
    weighted_adjacency_matrix[weighted_adjacency_matrix > 0.4] = 0
    for row in range(0, num_individuals):
        for col in range(row, num_individuals):
            if row == col:
                weighted_adjacency_matrix[row][col] = 0
                weighted_adjacency_matrix[col][row] = 0
            else:
                weighted_adjacency_matrix[col][row] = weighted_adjacency_matrix[row][col]    
    return weighted_adjacency_matrix
    
def create_weighted_adjacency_list(individual_list, weighted_adjacency_matrix):
    """From a weighted adjacency matrix, we get a list of tuples representing 
    edges and edge weights"""
    nonzero_indices = np.nonzero(weighted_adjacency_matrix)
    weighted_adjacency_list = [] 

    for i in range(0, len(nonzero_indices[0])):
        source_node = nonzero_indices[0][i]
        sink_node = nonzero_indices[1][i]
        weighted_adjacency_list.append([(individual_list[source_node],
                        individual_list[sink_node]),
                        weighted_adjacency_matrix[source_node, sink_node]])
    
    return weighted_adjacency_list


