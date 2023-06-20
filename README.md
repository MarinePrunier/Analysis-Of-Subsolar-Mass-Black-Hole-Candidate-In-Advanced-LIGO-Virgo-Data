# Analysis-Of-Subsolar-Mass-Black-Hole-Candidates-In-Advanced-LIGO-Virgo-Data
Complete Bayesian parameter estimation of a gravitational wave candidate event in LIGO-Virgo data using BILBY PIPE. 

Abstract: 

Gravitational wave astronomy has opened new windows for the detection of theoretical black holes of primordial origin. Primordial Black Holes may have formed from the collapse of overdense regions in the very early Universe. The detection of such objects would have ground-breaking implications for astrophysics and fundamental physics. Unlike stellar black holes, the cosmological origin of those primordial black holes does not prevent them from existing at subsolar masses. In 2022, a search for binary black hole mergers with at least one subsolar mass component was carried out by the LIGO-Virgo-KAGRA collaboration, with several candidates discovered. In this work, we aim to analyze one of the most promising of these candidates in order to infer the masses of the two compact objects that generated the gravitational wave signal. We perform a complete Bayesian parameter estimation on the candidate and find that the signal, if originating from a compact binary coalescence, has both components subsolar with $m_1= 0.53^{+0.32}_{-0.11}$ and $m_2 = 0.29^{+0.07}_{-0.10}$ solar masses (90 \% credible interval). These masses are below the minimum mass of a neutron star, discarding the hypothesis that the signal is a binary neutron star. The significance of the candidate is also evaluated to quantify the odds that the signal results from a gravitational wave event rather than noise in the detector. However, these different tests do not yield strong evidence that the candidate is a true gravitational wave event.

Content: 

init.ini : configuration file for bilby_pipe 
gps.txt : gps time of the candidate event in the LIGO-Virgo O3b observation run.
MergeAndVizualise.py : visualize corner plots and 1D marginalized posterior distribution from the results of bilby_pipe.
PlotSkyMap.py : plot the sky map to localize the trigger.
