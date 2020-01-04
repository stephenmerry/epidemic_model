#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:25:23 2020

@author: stephen
"""

import numpy as np

def create_weighted_adjacency_list(individual_list, weighted_adjacency_matrix):
    nonzero_indices = np.nonzero(weighted_adjacency_matrix)
    weighted_adjacency_list = [] 

    for i in range(0, len(nonzero_indices[0])):
        source_node = nonzero_indices[0][i]
        sink_node = nonzero_indices[1][i]
        weighted_adjacency_list.append([individual_list[source_node],
                        individual_list[sink_node],
                        weighted_adjacency_matrix[source_node, sink_node]])
    
    return weighted_adjacency_list
