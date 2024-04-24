#!/usr/bin/env python

from digitalFilters.filter_transformations import filter_transforms as filt_trans
from digitalFilters.filter_transformations import filter_transforms_freqmap as fmap
from digitalFilters.system_properties import freq_response as fr

import math

if __name__ == "__main__":
    # Problem 8
    lambda1 = filt_trans.lp2lpCoeff(0.25 * math.pi, 0.35 * math.pi)
    lambda2 = filt_trans.lp2lpCoeff(0.69 * math.pi, 0.78 * math.pi)
    
    print("Coefficients based new filter specs:")
    print("Design on Passband: ", lambda1)
    print("Design on Stopband: ", lambda2)
    
    ws1 = fmap.lp2lpfreqmap(0.69 * math.pi, lambda1) / math.pi
    wp2 = fmap.lp2lpfreqmap(0.25 * math.pi, lambda2) / math.pi
    
    print("Opposite Pass/Stop Bands for Designed Filters:")
    print("Stopband for Filter 1: ", ws1)
    print("Passband for Filter 2: ", wp2)
    
    num1 = [0.66, 1.98, 1.98, 0.66]
    den1 = [1, -0.94, 0.5668, -0.1014]
    num2_8 = [1.33, 4, 4, 1.33]
    den2_8 = [1, -0.26, 0.34, -0.023]
    
    w1, h1 = fr.get_freq_response_digital(num1, den1)
    w2_8, h2_8 = fr.get_freq_response_digital(num2_8, den2_8)
    
    fr.plot_filt_transform_freq_response(w1, h1, w2_8, h2_8, ylims=(-50, 25))
    
    # Question 9
    
    lambda1 = filt_trans.lp2hpCoeff(0.25 * math.pi, 0.55 * math.pi)
    lambda2 = filt_trans.lp2hpCoeff(0.69 * math.pi, 0.16 * math.pi)
    
    print("Coefficients based new filter specs:")
    print("Design on Passband: ", lambda1)
    print("Design on Stopband: ", lambda2)
    
    ws1 = fmap.lp2hpfreqmap(0.69 * math.pi, lambda1) / math.pi
    wp2 = fmap.lp2hpfreqmap(0.25 * math.pi, lambda2) / math.pi
    
    print("Opposite Pass/Stop Bands for Designed Filters:")
    print("Stopband for Filter 1: ", ws1)
    print("Passband for Filter 2: ", wp2)
    
    den1 = [1, -0.94, 0.5685, -0.1018]
    num2_9 = [2.184, -6.56, 6.56, -2.184]
    den2_9 = [1, -0.346, 0.364, -0.0328]
    
    w1, h1 = fr.get_freq_response_digital(num1, den1)
    w2_9, h2_9 = fr.get_freq_response_digital(num2_9, den2_9)
    
    fr.plot_filt_transform_freq_response(w1, h1, w2_9, h2_9, ylims=(-50, 25))
    
    