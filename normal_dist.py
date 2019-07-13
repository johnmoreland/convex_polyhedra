import math
import random
import statistics
import numpy as np

#define points in spherical coordinates
# r is constant (1)
# azimuth (theta), where +X = 0deg
# elevation, ranges from -pi/2 to pi/2 (-90deg to +90deg)

def sph_random_distribution(point_qty, r):
    '''
    This function returns a list of points on a sphere
    Inputs:
        desired number of points
        radius of sphere
    Output:
        list of points
    '''

    point_list = []
    for i in range(point_qty):
        azimuth     = random.random() * 2*math.pi
        elevation   = (random.random()-.5) * math.pi
        point = (r, azimuth, elevation)
        point_list.append(point)
    return point_list


def central_angle(coord1, coord2):
    '''
    this function returns the central angle (in radians) between two points on a sphere
    the max return value is pi/2 = 180deg
    '''
    (r1, az1, el1), (r2, az2, el2) = coord1, coord2
    return np.arccos( (np.sin(az1)*np.sin(az2)) + np.cos(az1)*np.cos(az2)*np.cos(el1-el2) )


def fitness(list_of_points):
    #initialize list of central angles
    central_angle_list = []
    for coordinate in list_of_points[:-1]:
        #for each coordinate, calculate the central angle to every coordinate after it in the list and record value
        #don't compare the last coordinate in the list to anything
        #and don't compare a coordinate to itself
        for index in range(list_of_points.index(coordinate) + 1, len(list_of_points)):
            central_angle_list.append( central_angle(coordinate, list_of_points[index]) )
    #calculate values from list
    CAmin, CAmax, CAavg, CAstdev = min(central_angle_list), max(central_angle_list), sum(central_angle_list)/len(central_angle_list), statistics.stdev(central_angle_list)
    # return (CAmin, CAmax, CAavg)
    return CAstdev

def generate_population(population_size):
    #Generate pool of random distributions
    distribution_pool = []
    for i in range(population_size): distribution_pool.append(sph_random_distribution(number_of_points, unit_radius))
    return distribution_pool

def evaluate_population(distribution_pool):
    #Get fitness of each distribution and sort accordingly
    population_fitness=[]
    for distribution in distribution_pool: population_fitness.append( (fitness(distribution), distribution) )
    sorted_population = sorted(population_fitness, key=lambda x:x[0])

    # for member in sorted_population: print(member[0])
    return sorted_population


if __name__ == "__main__" :

    '''
    1) Create random distributions of points on sphere
    2) Calculate error function (standard deviation)
        for each distribution: get min, max, average central angle between points
    3) Optimize until convergence (standard deviation falls below thresh)


    '''

    number_of_points    = 4
    unit_radius         = 1
    population_size     = 10

    #initialize
    population = generate_population(population_size) #generate random population

    sorted_population = evaluate_population(population) #order population according to fitness
    print (len(sorted_population))
