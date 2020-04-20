import numpy as np

"""
Loads the CSV file from a Quantum Designs SQUID system.
Returns a numpy structured array.
The units are changed from Oe to mT

data = loadSquidData(filename)

To view the names in the array:
data.dtype.names



Header from files:

Comment, Time Stamp (sec), Temperature (K), Magnetic Field (Oe), Moment (emu),
M. Std. Err. (emu), Transport Action, Averaging Time (sec), Frequency (Hz), Peak Amplitude (mm),
Center Position (mm), Lockin Signal' (V), Lockin Signal (V), Range, M. Quad. Signal (emu), 	
AC Moment (emu), AC M. Std Err. (emu), AC Phase (deg), AC Phase Std. Err. (deg), AC Susceptibility (emu/Oe),
AC Suscept. Std Err. (emu/Oe), AC X' (emu/Oe), AC X' Std Err. (emu/Oe), AC X'' (emu/Oe), AC X'' Std Err. (emu/Oe), AC Drive (Oe),					AC Frequency (Hz),		AC Averaging Time (sec),	AC Cycles,						AC Range,						AC Measure Type,
AC Signal' (V), AC Signal'' (V), AC Trim Coil Ratio, AC Trim Coil Phase, Min. Temperature (K),Max. Temperature (K),
Min. Field (Oe),Max. Field (Oe),Mass (grams),Motor Lag (deg),Pressure (Torr),Measure Count,Measurement Number,
SQUID Status (code),Motor Status (code),Measure Status (code),Motor Current (amps),Motor Temp. (C),Temp. Status (code),
Field Status (code),Chamber Status (code),Chamber Temp (K),Redirection State,Average Temp (K),Rotation Angle (deg),
Rotator state,DC Moment Fixed Ctr (emu),DC Moment Err Fixed Ctr (emu),DC Moment Free Ctr (emu),DC Moment Err Free Ctr (emu),
DC Fixed Fit,DC Free Fit,DC Calculated Center (mm),DC Calculated Center Err (mm),DC Scan Length (mm),DC Scan Time (s),
DC Number of Points,DC Squid Drift,DC Min V (V),DC Max V (V),DC Scans per Measure,Map 01,Map 02,Map 03,Map 04,Map 05,Map 06,
Map 07,Map 08,Map 09,Map 10,Map 11,Map 12,Map 13,Map 14,Map 15,Map 16

"""



names = ['comment', 'time', 'temperature', 'field', 'moment', 'moment_stderr', 'transport_action', 'averaging_time', 'frequency', 'peak_amplitude',
'center_position', 'lockin_signal_y' 'lockin_signal_x', 'range', 'm_quad_signal', 'ac_moment', 'ac_moment_stderr', 'ac_phase', 'ac_phase_stderr', 'ac_susceptibility',
'ac_susceptibility_stderr', "ac_dX", "ac_dX_stderr", "ac_d2X", "ac_d2X_stderr", 'ac_drive', 'ac_frequency',	'ac_averaging_time', 'ac_cycles', 'ac_range',
'ac_measure_type', "ac_signal'", "ac_signal''", 'ac_trim_coil_ratio', 'ac_trim_coil_phase', 'min_temperature', 'max_temperature', 'min_field', 'max_field', 'mass',
'motor_lag', 'pressure', 'measure_count', 'measurement_number', 'SQUID_status', 'motor_status', 'measure_status', 'motor_current', 'motor_remp', 'temp_status',
'field_status', 'chamber_status', 'chamber_temp', 'redirection_state', 'average_temp', 'rotation_angle', 'rotator_sstate', 'dc_moment_fixed_ctr', 'dc_moment_err_fixed_ctr',
'dc_moment_free_ctr', 'dc_moment_err_free_ctr', 'dc_fixed_fit', 'dc_free_fit', 'dc_calculated_center', 'dc_calculated_center_err', 'dc_scan_length', 'dc_scan_time',
'dc_num_points', 'dc_squid_drift', 'dc_min_v' ,'dc_max_v', 'dc_scans_per_measure',
'map_01','map_02','map_03','map_04','map_05','map_06','map_07','map_08','map_09','map_10','map_11','map_12','map_13','map_14','map_15','map_16']


def loadSquidData(filename):
    data = np.genfromtxt(filename,delimiter=',',skip_header=28, names=names)

    data['field'] = data['field'] / 10.0 # convert Oe to mT
    data['min_field'] = data['max_field'] / 10.0 # convert Oe to mT
    data['min_field'] = data['max_field'] / 10.0 # convert Oe to mT
    data['ac_drive'] = data['ac_drive'] / 10.0 # convert Oe to mT
    
    data['ac_susceptibility'] = data['ac_susceptibility'] * 10.0 # convert emu/Oe to emu/mT
    data['ac_susceptibility_stderr'] = data['ac_susceptibility_stderr'] * 10.0 # convert emu/Oe to emu/mT
    data["ac_dX"] = data["ac_dX"] * 10.0 # convert emu/Oe to emu/mT
    data["ac_dX_stderr"] = data["ac_dX_stderr"] * 10.0 # convert emu/Oe to emu/mT
    data["ac_d2X"] = data["ac_d2X"] * 10.0 # convert emu/Oe to emu/mT
    data["ac_d2X_stderr"] = data["ac_d2X_stderr"] * 10.0 # convert emu/Oe to emu/mT
    
    data['ac_susceptibility'] = data['ac_susceptibility'] * 10.0 # convert emu/Oe to emu/mT
    data['ac_susceptibility'] = data['ac_susceptibility'] * 10.0 # convert emu/Oe to emu/mT
    data['ac_susceptibility'] = data['ac_susceptibility'] * 10.0 # convert emu/Oe to emu/mT
    
    return data


