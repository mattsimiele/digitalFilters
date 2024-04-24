#!/usr/bin/env python

from digitalFilters.system_properties import freq_response as fr

from scipy.signal import bilinear

import math

if __name__ == "__main__":
    # Plot Analog Frequency Response for desired filter
    analog_num = [0.0001496]
    analog_den = [1, 0.1497, 0.0359, 0.00291, 0.0001678]
    w_analog, h_analog = fr.get_freq_response_analog(analog_num, analog_den, freq_lims=(-1, 0))
    fr.plot_analog_freq_response(w_analog, h_analog)
    
    # Get and Plot Digital LP Filter derived from Analog Filter
    [digital_lp_num, digital_lp_den] = bilinear(analog_num, analog_den, 0.5)
    
    digital_lp_num = [0.0001258, 0.00050342, 0.0007548, 0.00050342, 0.0001258]
    digital_lp_den = [1, -3.6115, 4.9881, -3.1175, 0.743]
    
    w_d_lp, h_d_lp= fr.get_freq_response_digital(digital_lp_num,digital_lp_den)
    fr.plot_single_freq_response(w_d_lp, h_d_lp, ylims=(-50, 10))
    fr.plot_single_freq_response(w_d_lp, h_d_lp)
    
    # Plot Digital BP Frequency Response 
    digital_bp_num = [0.001788, 0, -0.007152, 0, 0.01073, 0, -0.007152, 0, 0.001788]
    digital_bp_den = [1, 1.3909, 3.8002, 3.4999, 5.0795, 3.0266, 2.8495, 0.8884, 0.5517]
    
    w_d_bp, h_d_bp= fr.get_freq_response_digital(digital_bp_num,digital_bp_den)
    
    fr.plot_single_freq_response(w_d_bp, h_d_bp, ylims=(-50, 10))
    fr.plot_single_freq_response(w_d_bp, h_d_bp)
    fr.plot_filt_transform_freq_response(w_d_lp, h_d_lp, w_d_bp, h_d_bp, ylims=(-50, 10))