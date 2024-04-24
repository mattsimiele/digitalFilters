#!/usr/bin/env python
################################################################################                                                       
# Name:          Matthew Simiele                                                  
# Date:          04-18-2024                                                       
# Filename:      filter_transformations.py
# Developed for: Use during EC ENGR 212A                                                
# Purpose:       Contain necessary functions to compute filter transformations 
#                coefficient computations for:
#                   - Lowpass to Lowpass          
#                   - Lowpass to Highpass          
#                   - Lowpass to Bandpass          
#                   - Lowpass to Bandstop                                                                                                                                       
################################################################################

import math

def lp2lpCoeff(wc: float , wc_hat: float) -> float:
    """
    Compute low-pass to low-pass filter frequency mapping coefficients. Both inputs 
    (wc and wc_hat) must correspond to either the passband or stop band edge.
    
    Args:
        wc (float): Passband or stopband edge of origional filter in radians
        wc_hat (float): Passband or stopband edge of desired filter in radians
        
    Returns:
        float: Frequency mapping coefficient
    """
    c1 = math.sin((wc - wc_hat) / 2) / math.sin((wc + wc_hat) / 2)
    return c1

def lp2hpCoeff(wc: float , wc_hat: float) -> float:
    """
    Compute low-pass to low-pass filter frequency mapping coefficients. Both inputs 
    (wc and wc_hat) must correspond to either the passband or stop band edge.
    
    Args:
        wc (float): Passband or stopband edge of origional filter in radians
        wc_hat (float): Passband or stopband edge of desired filter in radians
        
    Returns:
        float: Frequency mapping coefficient
    """
    c1 = -1 * math.cos((wc + wc_hat) / 2) / math.cos((wc - wc_hat) / 2)
    return c1

def lp2bpCoeff(wc: float , wc1_hat: float , wc2_hat: float) -> tuple[float, float]:
    """
    Compute low-pass to band-pass filter frequecny mapping coefficients. All inputs 
    (wc, wc1_hat, and wc2_hat) must correspond to either the passband or stop band edge.
    
    Args:
        wc (float): Passband or stopband edge of original filter in radians
        wc1_hat (float): First Passband or stopband edge of desired filter in radians
        wc2_hat (float): Second Passband or stopband edge of desired filter in radians
        
    Returns:
        float: Frequency mapping coefficient
    """
    c1 = math.cos((wc2_hat + wc1_hat) / 2) / math.cos((wc2_hat - wc1_hat) / 2)
    c2 = math.atan2((wc2_hat - wc1_hat) / 2) * math.tan(wc / 2)
    return c1, c2

def lp2bsCoeff(wc: float , wc1_hat: float , wc2_hat: float) -> tuple[float, float]:
    """
    Compute low-pass to band-pass filter frequecny mapping coefficients. All inputs 
    (wc, wc1_hat, and wc2_hat) must correspond to either the passband or stop band edge.
    
    Args:
        wc (float): Passband or stopband edge of original filter in radians
        wc1_hat (float): First Passband or stopband edge of desired filter in radians
        wc2_hat (float): Second Passband or stopband edge of desired filter in radians
        
    Returns:
        float: Frequency mapping coefficient
    """
    c1 = math.cos((wc2_hat + wc1_hat) / 2) / math.cos((wc2_hat - wc1_hat) / 2)
    c2 = math.tan((wc2_hat - wc1_hat) / 2) * math.tan(wc / 2)
    return c1, c2