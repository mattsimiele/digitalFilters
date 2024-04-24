#!/usr/bin/env python
################################################################################                                                       
# Name:          Matthew Simiele                                                  
# Date:          04-18-2024                                                       
# Filename:      ver_filter_transformation.py
# Developed for: Use during EC ENGR 212A                                                
# Purpose:       Contain necessary functions to verify filter transformations
#                for the following:
#                   - Lowpass to Lowpass          
#                   - Lowpass to Highpass          
#                   - Lowpass to Bandpass          
#                   - Lowpass to Bandstop                                                                                                                                       
################################################################################

from filter_transformations.filter_transforms_freqmap import lp2lpfreqmap, lp2hpfreqmap

def lp2lpVer(wp: float , wp_hat: float, 
             ws: float , ws_hat: float,
             c1: float) -> bool:
    """
    Determine if Low-Pass to Low-Pass transformation meets frequency 
    specifications
    
    Args:
        wp (float): Passband edge of original filter in radians
        wp_hat (float): Passband or edge of desired filter in radians
        ws (float): Stopband edge of original filter in radians
        ws_hat (float): Stopband or edge of desired filter in radians
        c1 (float): Transformation coefficient
        
    Returns:
        bool: Frequency mapping coefficient
    """
    wp_achieved = lp2lpfreqmap(wp, c1)
    ws_achieved = lp2lpfreqmap(ws, c1)
    return ((wp_hat <= wp_achieved) and (ws_achieved <= ws_hat))

def lp2lpVer(wp: float , wp_hat: float, 
             ws: float , ws_hat: float,
             c1: float) -> bool:
    """
    Determine if Low-Pass to High-Pass transformation meets frequency 
    specifications
    
    Args:
        wp (float): Passband edge of original filter in radians
        wp_hat (float): Passband or edge of desired filter in radians
        ws (float): Stopband edge of original filter in radians
        ws_hat (float): Stopband or edge of desired filter in radians
        c1 (float): Transformation coefficient
        
    Returns:
        bool: Frequency mapping coefficient
    """
    wp_achieved = lp2hpfreqmap(wp, c1)
    ws_achieved = lp2hpfreqmap(ws, c1)
    return ((wp_hat >= wp_achieved) and (ws_achieved >= ws_hat))