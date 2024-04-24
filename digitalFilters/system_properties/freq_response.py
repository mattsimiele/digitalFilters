#!/usr/bin/env python
################################################################################                                                       
# Name:          Matthew Simiele                                                  
# Date:          04-19-2024                                                       
# Filename:      freq_response.py
# Developed for: Use during EC ENGR 212A                                                
# Purpose:       Plots the frequency response of a digital filter                                                                                                                                      
################################################################################

from scipy.signal import freqz, freqs
from matplotlib import pyplot as plt
import numpy as np

def plot_single_freq_response(w ,h, xlims = (0,1), ylims = None):
    """
    Plot digital frequency response for frequency (w)
    and magnitude (h)
    
    Args:
        w (list/array): frequency in radians/second from 0 to pi
        h (list/array): magnitude of the frequency response in abs
        xlims (tuple): limits of x in normalized raians/sec
        ylims (tuple): limits of y in dB
        
    Returns:
        Plot of Digital frequency response
    """ 
    fig = plt.figure()
    plt.title('Digital filter frequency response')
    plt.plot(w/np.pi, 20 * np.log10(abs(h)), 'b')
    plt.ylabel('Amplitude [dB]', color='b')
    plt.xlabel('Frequency [rad/sample]')
    plt.xlim(xlims)
    if ylims is not None:
        plt.ylim(ylims)
    plt.grid(which = "major")
    plt.grid(which = "minor", linestyle='dashed')
    plt.minorticks_on()
    plt.show()
    
def plot_filt_transform_freq_response(w1 ,h1, w2, h2, xlims = (0,1), ylims = None):
    """
    Plot digital frequency response for frequency (w)
    and magnitude (h)
    
    Args:
        w1 (list/array): frequency in radians/second from 0 to pi (first/origional)
        h1 (list/array): magnitude of the frequency response in abs (first/origional)
        w2 (list/array): frequency in radians/second from 0 to pi (new/transform)
        h2 (list/array): magnitude of the frequency response in abs (new/transform)
        xlims (tuple): limits of x in normalized raians/sec
        ylims (tuple): limits of y in dB
        
    Returns:
        Plot of Digital frequency response
    """ 
    fig = plt.figure()
    plt.title('Digital filter frequency response')
    plt.plot(w1/np.pi, 20 * np.log10(abs(h1)), 'b', label='Orig')
    plt.plot(w2/np.pi, 20 * np.log10(abs(h2)), 'r', label='Filt. Transformation')
    plt.ylabel('Amplitude [dB]', color='b')
    plt.xlabel('Normalized Frequency [* \pi rad/sample]')
    plt.xlim(xlims)
    if ylims is not None:
        plt.ylim(ylims)
    plt.legend()
    plt.grid(which = "major")
    plt.grid(which = "minor", linestyle='dashed')
    plt.minorticks_on()
    plt.show()
    
def get_freq_response_digital(num, den, numSamples = 512, whole = False):
    """
    Gets the digital frequency response for a filter defined by 
    numerator and denominator coefficients
    
    Numerator and denominator has order len(X) - 1
    
    H(z) = (num)    (num[0] + num[1]*z^{-1} + ... + num[i]*z^{-i}) \n
           ----- =  ---------------------------------------------- \n
           (den)    (den[0] + den[1]*z^{-1} + ... + den[i]*z^{-i})
    
    Args:
        num (list/array): Coefficients of the transfer function in the numerator
        den (list/array): Coefficients of the transfer function in the denominator
        numSamples (int): limits of x in normalized raians/sec
        whole (bool): limits of y in dB
        
    Returns:
        w (list/array): frequency in radians/second from 0 to pi
        h (list/array): magnitude of the frequency response in abs 
    """
    w, h= freqz(num, den, numSamples, whole)
    return w, h 

def plot_analog_freq_response(w, h, xlims = None, ylims = None):
    """
    Plot analog frequency response for frequency (w)
    and magnitude (h)
    
    Args:
        w (list/array): frequency in radians/second from 0 to pi
        h (list/array): magnitude of the frequency response in abs
        xlims (tuple): limits of x in normalized raians/sec
        ylims (tuple): limits of y in dB
        
    Returns:
        Plot of Analog frequency response
    """ 
    fig = plt.figure()
    plt.title('Analog filter frequency response')
    plt.semilogx(w, 20 * np.log10(abs(h)), 'b')
    plt.ylabel('Amplitude [dB]', color='b')
    plt.xlabel('Frequency rads/sec')
    if xlims is not None: 
        plt.xlim(xlims)
    if ylims is not None:
        plt.ylim(ylims)
    plt.legend()
    plt.grid(which = "major")
    plt.grid(which = "minor", linestyle='dashed')
    plt.minorticks_on()
    plt.show()
    
def get_freq_response_analog(num, den, freq_lims = None, numSamples = 512):
    """
    Gets the analog frequency response for a filter defined by 
    numerator and denominator coefficients
    
    Numerator and denominator has order len(X) - 1
    
    H(z) = (num)    (num[0]*s^{N-1} + num[1]*s^{N-2} + ... + num[i] \n
           ----- =  ----------------------------------------------  \n
           (den)    (den[0]*s^{N-1} + den[1]*s^{N-2} + ... + den[i]
    
    Args:
        num (list/array): Coefficients of the transfer function in the numerator
        den (list/array): Coefficients of the transfer function in the denominator
        freq_lims (tuple): Frequency limits in to be placed in the logspace funtion
            i.e. -1 -> 10^{-1} or 2 -> 10^{2}
        numSamples (bool): number of samples to compute the frequency log axis in 
        
    Returns:
        w (list/array): frequency in radians/second from 0 to pi
        h (list/array): magnitude of the frequency response in abs 
    """
    if freq_lims is not None:
        worN = np.logspace(freq_lims[0], freq_lims[1], numSamples)
    else: 
        worN = 512
    w, h = freqs(num, den, worN)
    return w, h