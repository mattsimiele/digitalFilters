#!/usr/bin/env python
################################################################################                                                       
# Name:          Matthew Simiele                                                  
# Date:          04-18-2024                                                       
# Filename:      filter_transformations_freqmap.py
# Developed for: Use during EC ENGR 212A                                                
# Purpose:       Contain necessary functions to generate frequency maps for the 
#                filter transformations:
#                   - Lowpass to Lowpass          
#                   - Lowpass to Highpass          
#                   - Lowpass to Bandpass          
#                   - Lowpass to Bandstop                                                                                                                                       
################################################################################

import math

def lp2lpfreqmap(w: float, c1: float) -> float:
    """
    Lowpass to Lowpass frequency map based on filter transformation.
    
    Args:
        w (float): Original frequency 
        c1 (float): Transformation coefficient
        
    Returns:
        w_hat (float): New frequency based on specified filter paramaters
    """   
    w_hat = 2 * math.atan(((1 - c1) / (1 + c1)) * math.tan(w/2))
    return abs(w_hat)

def lp2hpfreqmap(w: float, c1: float) -> float:
    """
    Lowpass to Highpass frequency map based on filter transformation.
    
    Args:
        w (float): Original frequency 
        c1 (float): Transformation coefficient
        
    Returns:
        w_hat (float): New frequency based on specified filter paramaters
    """   
    w_hat = 2 * math.atan(-1* ((1 + c1) / (1 - c1)) * cotan(w/2))
    return abs(w_hat)

def lp2bpfreqmap(w_hat: float, c1: float, c2: float) -> float:
    """
    Lowpass to Bandpass frequency map based on filter transformation.
    
    Args:
        w_hat (float): New Frequency Map for 
        c1 (float): Transformation coefficient
        c2 (float): Transformation coefficient
        
    Returns:
        w (float): Old Frequency on LP filter that the new bandpass maps to
    """   
    w = 2 * math.atan((c2 * ( c1 - math.cos(w_hat))) / math.sin(w_hat))
    return w

def lp2bpfreqmap(w_hat: float, c1: float, c2: float) -> float:
    """
    Lowpass to Bandstop frequency map based on filter transformation.
    
    Args:
        w_hat (float): New Frequency Map for 
        c1 (float): Transformation coefficient
        c2 (float): Transformation coefficient
        
    Returns:
        w (float): Old Frequency on LP filter that the new bandstop maps to
    """   
    w = 2 * math.atan((c2 * math.sin(w_hat)) / (math.cos(w_hat) - c1))
    return w

def cotan(x: float) -> float:
    """
    Calculates the cotan of x where x is in radians
    
    Args:
        x (float): angle in radians
        
    Returns:
        cotangent of the angle x in radians
    """   
    return math.cos(x) / math.sin(x)