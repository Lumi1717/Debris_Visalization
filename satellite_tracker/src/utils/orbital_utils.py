import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord, CartesianRepresentation
from astropy.time import Time

def compute_position(inclination, raan, eccentricity, arg_perigee, mean_anomaly, mean_motion, epoch):
    """
    Compute satellite position using orbital elements.
    
    Args:
        inclination (float): Orbital inclination in radians
        raan (float): Right Ascension of Ascending Node in radians
        eccentricity (float): Orbital eccentricity
        arg_perigee (float): Argument of perigee in radians
        mean_anomaly (float): Mean anomaly in radians
        mean_motion (float): Mean motion in revs/day
        epoch (str): Epoch time
        
    Returns:
        numpy.ndarray: [x, y, z] position in kilometers
    """
    # Convert mean motion to semi-major axis (a) using Kepler's third law
    mu = 3.986004418e14  # Earth's gravitational parameter (m^3/s^2)
    mean_motion_rads = mean_motion * (2 * np.pi) / (24 * 3600)  # Convert revs/day to rad/s
    semi_major_axis = (mu / (mean_motion_rads**2)) ** (1/3)  # Semi-major axis in meters

    # Convert semi-major axis to kilometers
    semi_major_axis_km = semi_major_axis / 1000

    # Compute the true anomaly (ν) from the mean anomaly (M) and eccentricity (e)
    true_anomaly = mean_anomaly + 2 * eccentricity * np.sin(mean_anomaly)

    # Convert orbital elements to Cartesian coordinates
    r = semi_major_axis_km * (1 - eccentricity**2) / (1 + eccentricity * np.cos(true_anomaly))
    x = r * (np.cos(raan) * np.cos(true_anomaly + arg_perigee) - 
             np.sin(raan) * np.sin(true_anomaly + arg_perigee) * np.cos(inclination))
    y = r * (np.sin(raan) * np.cos(true_anomaly + arg_perigee) + 
             np.cos(raan) * np.sin(true_anomaly + arg_perigee) * np.cos(inclination))
    z = r * np.sin(true_anomaly + arg_perigee) * np.sin(inclination)

    return np.array([x, y, z])

def generate_color(index, total):
    """
    Generate a unique color for visualization.
    
    Args:
        index (int): Index of the satellite
        total (int): Total number of satellites
        
    Returns:
        numpy.ndarray: RGB color array
    """
    hue = index / total
    r = int(255 * (1 - hue))
    g = int(255 * hue)
    b = int(255 * (1 - abs(2 * hue - 1)))
    return np.array([r, g, b]) 