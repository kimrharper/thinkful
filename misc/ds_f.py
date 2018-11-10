import math
from collections import Counter
from functools import partial,reduce

# linalg

"""vector addition"""
def vector_add(v, w):
    return [v_i+w_i for v_i,w_i in zip(v,w)]

"""vector subtraction"""
def vector_subtract(v, w):
    return [v_i-w_i for v_i,w_i in zip(v,w)]

"""vector summation"""
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

"""Alternative method for vector summation"""
# vector_sum = partial(reduce, vector_add)

"""vector scaling"""
def scalar_multiply(c,v):
    return [c*v_i for v_i in v]

"""vector mean"""
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

"""dot product"""
def dot(v,w):
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    """(v_1 - w_1) ** 2 + ... + (v_n -w_n) **2"""
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return magnitude(vector_subtract(v,w))


# stats

def mean(x):
    return sum(x)/len(x)

def median(v):
    n=len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    
    if n%2 ==1:
        return sorted_v[midpoint]
    else:
        lo=midpoint-1
        hi=midpoint
        return (sorted_v[lo]+sorted_v[hi]/2)
    
def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

def mode(x):
    counts=Counter(x)
    max_count=counts.most_common(1)[0][1]
    most_common = [m[0] for m in counts.items() if m[1]==max_count]
    return [x_i for x_i in x if x_i in most_common] if (len(most_common)==1 and max_count>1) else None

def data_range(x):
    return max(x)-min(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i-x_bar for x_i in x]

def variance(x):
    n=len(x)
    deviations=de_mean(x)
    return sum_of_squares(deviations) /(n-1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x,.75)- quantile(x,.25)

def covariance(x,y):
    n=len(x)
    return (dot(de_mean(x),de_mean(y)))/(n-1)

def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x,y)/stdev_x/stdev_y
    else:
        return 0
    
    
# probability

def uniform_pdf(x_val):
    return 1 if (x_val>=0 and x_val<1) else 0

def uniform_cdf(x_val):
    if x_val<0: return 0
    elif x_val<1:return x_val
    else: return 1
    
def normal_pdf(x_val,mu=0,sigma=1):
    sqrt_two_pi = math.sqrt(2*math.pi)
    return (math.exp(-(x_val-mu)**2/2/sigma**2))/(sqrt_two_pi*sigma)

def normal_cdf(x_val,mu=0,sigma=1):
    return (1+math.erf((x_val-mu) / math.sqrt(2) / sigma))/2

def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
    # if not standard, compute standard and rescale
    if mu!= 0 or sigma !=1:
        return mu+sigma*inverse_normal_cdf(p,tolerance=tolerance)
    
    low_z = -10.0 #normal_cdf(-10) is ~0
    high_z = 10.0 #normal_cdf(10) is ~1
    while hi_z-low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 #eval midpoint
        mid_p = normal_cdf(mid_z)  #cdf value for midpoint
        if mid_p < p:
            # midpoint is still to low
            low_z=mid_z
        elif mid_p >p:
            # midpoint is too high
            high_z = mid_z
        else:
            break
    return mid_z

def bernoulli_trial(p):
    return 1 if np.random.random() < p else 0

def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))

"""make histogram with binomial probability range"""
def make_hist(p,n,num_points):
    data = [binomial(n,p) for _ in range(num_points)]
    
    histogram = Counter(data)
    plt.bar([x-.4 for x in histogram.keys()],
            [v/num_points for v in histogram.values()],
            .8,
            color='.75')
    mu=p*n
    sigma=math.sqrt(n*p*(1-p))
    
    xs = range(min(data),max(data)+1)
    ys= [normal_cdf(i+.5,mu,sigma) - normal_cdf(i-.5,mu,sigma) for i in xs]
    
    plt.plot(xs,ys)
    plt.title('Binomial Distribution vs Normal Approximation')
    plt.show()