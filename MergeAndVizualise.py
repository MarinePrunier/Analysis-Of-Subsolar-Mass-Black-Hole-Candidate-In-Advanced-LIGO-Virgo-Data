# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:34:14 2023

@author: marin
"""
import numpy as np
import arviz as az
import h5py  
import bilby 
import corner
import ligo.skymap.plot
from matplotlib import pyplot as plt

result_list = []
#path = '/home/supeguest/Documents/LDAS_Codes/PipeBilbyO3_122sec_10cpus/outdir_GSTLAL_O3_122sec_16cpus/result/'
path = '/home/supeguest/Documents/LDAS_Codes/GW382641_16cpus/outdir_G382641_16cpus/result/'

node_nb = 15
prefix= 'G382641_16cpus_data0_1267509412-389_analysis_H1L1V1_par'
#prefix = 'GSTLAL_O3_122sec_16cpus_data0_1267726091-0234_analysis_H1L1_par'
out = 'SSMC2_FIGURES/'

for i in range(node_nb):
    print(i)
    #if (i != 0 and i!=5 and i!=6 and i!=8):
        file = prefix + '%i'%i + '_result.hdf5'
        filename = path+file
        result = bilby.core.result.read_in_result(filename=filename, outdir=None, label=None, extension='hdf5')
        result_list.append(result)

result_list = bilby.core.result.ResultList(results=result_list)

merge_results = result_list.combine()


merge_results.plot_corner(parameters = ["mass_1_source","mass_2_source"],
                          titles=True,
                          prior=False,
                          filename = 'corner_mass',
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+ out,
                          save = True,
                          labels=[
                              r"$m_1$",
                              r"$m_2$",],
                          color = 'C0',
                          range =  [(0.5,2), (0.2,0.9)],
                          quantiles=[0.16, 0.5, 0.84],
                          show_titles=True,
                          title_kwargs={"fontsize": 20},
                          )

merge_results.plot_corner(parameters = ["luminosity_distance","theta_jn"],
                          titles=True,
                          priors = True,
                          filename = 'corner_dist',
                          range =  [(10,30), (0.01,3.2)],
                          labels=[
                              r"$d_L$",
                              r"$\theta_{JN}$",],
                          color = 'C9',
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+ out,
                          quantiles=[0.16, 0.5, 0.84],
                          show_titles=True,
                          title_kwargs={"fontsize": 20},
                          )

merge_results.plot_corner(parameters = ["ra","dec"],
                          titles=True,
                          labels=[
                              r"$\alpha$",
                              r"$\delta$",],
                          color = 'C3',
                          filename = 'corner_radec',
                          priors = True,
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+ out,
                          quantiles=[0.16, 0.5, 0.84],
                          show_titles=True,
                          title_kwargs={"fontsize": 20},
                          )

merge_results.plot_marginals(parameters = ["redshift"],
                          titles=True,
                          color = 'C3',
                          quantiles=[0.16, 0.84],
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+ out,
                          )

merge_results.plot_corner(parameters = ["chi_eff","chi_p"],
                          titles=True,
                          labels=[
                              r"$\chi_{eff}$",
                              r"$\chi_{p}$",],
                          color = 'C2',
                          quantiles=[0.16, 0.5, 0.84],
                          show_titles=True,
                          filename = 'corner_chi',
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+out,
                          title_kwargs={"fontsize": 20},
                          )

merge_results.plot_corner(parameters = ["chi_eff","mass_ratio"],
                          titles=True,
                          labels=[
                              r"$\chi_{eff}$",
                              r"$q$",],
                          color = 'C3',
                          quantiles=[0.16, 0.5, 0.84],
                          show_titles=True,
                          filename = 'corner_p_chieff',
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+out,
                          title_kwargs={"fontsize": 20},
                          )

merge_results.plot_corner(parameters = ["chirp_mass_source","mass_ratio"],
                          titles=True,
                          labels=[r"$M_c$",r"$q$"],
                          color = 'C4',
                          range =  [(0.31,0.37), (0.05,1.1)],
                          quantiles=[0.16, 0.5, 0.84],
                          show_titles=True,
                          filename = 'corner_chirp',
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+out,
                          title_kwargs={"fontsize": 20},
                          )

merge_results.plot_corner(parameters = ["chirp_mass_source","mass_ratio"],
                          titles=True,
                          labels=[r"$M_c$",r"$q$"],
                          color = 'C4',
                          range =  [(0.61,0.72), (0.05,1.1)],
                          quantiles=[0.16, 0.5, 0.84],
                          show_titles=True,
                          filename = 'corner_chirp',
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+out,
                          title_kwargs={"fontsize": 20},
                          )


merge_results.plot_corner(parameters = ["H1_matched_filter_snr","L1_matched_filter_snr"],
                          outdir='/home/supeguest/Documents/LDAS_Codes/'+out,
                          titles=False,
                          labels=[
                              r"$SNR_{H1}$",
                              r"$SNR_{L1}$",],
                          color = 'C1',
                          show_titles=False,
                          filename = 'corner_snr',
                          title_kwargs={"fontsize": 20},
                          )
