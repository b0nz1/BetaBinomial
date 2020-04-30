#from scipy.special import gamma 
from scipy.special import gammaln
from scipy.special import comb
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import pymc3
import sys

"""
# return the probablity of occurence k for a beta binomial n, alpha, beta
def beta_binom_density(k, n, alpha, beta):
    dens = 1.0*gamma(n+1)*gamma(alpha+k)*gamma(n+beta-k)*gamma(alpha+beta) / (gamma(k+1)*gamma(n-k+1)*gamma(alpha+beta+n)*gamma(alpha)*gamma(beta))
    return dens 
"""

# return the probablity of occurence k for a beta binomial n, alpha, beta
# this is in the log space to prevent overflow
def beta_binom_density_ln(k, n, alpha, beta):
    num = gammaln(k + alpha) + gammaln(n - k + beta) + gammaln(alpha + beta)
    den = gammaln(n + alpha + beta) + gammaln(alpha) + gammaln(beta)
    log = np.log(comb(n,k)) + num - den
    return np.exp(log)

def plot_beta_binom_pmf(alpha,beta,N):
    distribution = [] # list that stock the probabilty
    for k in range(N+1):
        distribution.append(beta_binom_density_ln(k, N, alpha, beta))
    
    plt.plot(distribution)
    plt.title("probability mass function")
    plt.show()

def get_samples(alpha, beta, num_samples):
    with pymc3.Model() as model:
        pymc3.Beta('b', alpha=alpha, beta=beta)
        tr = pymc3.sample(num_samples)
    return tr.get_values('b')

def plot_sample_of_beta_dist(alpha, beta, N):
    samples = get_samples(alpha, beta, N)
    plt.figure(figsize=(10,5))
    ax = plt.subplot(121)
    ax.hist(samples, bins=int(np.sqrt(N)), density=True )
    ax.set_xlim(0.,1.)
    ax.set_ylim(0.,7.0)
    plt.title("Sample-Histogram Beta(%0.1f,%0.1f)"%(alpha,beta))

if __name__ == "__main__":
    #Plot the pmf
    N=100
    alpha = 1.0
    beta = 7.0
    
    plot_beta_binom_pmf(alpha,beta,N)
    plot_sample_of_beta_dist(alpha, beta, N)