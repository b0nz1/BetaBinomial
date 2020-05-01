The program outputs two plots:
1. Probability mass function of N samples, calculated according to Gamma equastion.
2. Histogram of generated samples according to the Beta Binomial distribution.
The two plots are supposed to look somewhat the same (with larger N the plotsare more precise)

Parameters of model:
N - number of samples
alpha - parameter of Beta
beta - parameter of Beta
************************************************************************
General:
Beta distribution is a probability distribution of probabilities. It describes how likely the
probability p is take each value: f(x;alpha,beta)=x^(alpha-1)*(1-x)^(beta-1) / B(alpha,Beta)

Prior is what we believe before conducting the experiment. For example when flipping a coin, 
if we believe that the coin is fair -> alpha=beta, and the larger these parameters are, the more certain 
we are in the fairness of the coin(it will take us more turns to show otherwise).
Uniform distribution is a special case of B when alpha=beta=1.

Bayesian update is basically updating the values of alpha and beta after each "coin" toss according
to the result we get. This is how we can analyticaly find the posterior distribution.
*************************************************************************

p.s. I hope i understood correctly what i was supposed to implement.
If not i would gladly try to fix/change it.

