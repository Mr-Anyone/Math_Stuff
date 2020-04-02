import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import scipy
import sympy

# This is a really important function that apply the init condition and save you a lot of time
def apply_ics(sol, ics, x, known_params):
    free_params = sol.free_symbols - set(known_params)
    eqs = [(sol.lhs.diff(x,n)-sol.rhs.diff(x,n)).subs(x,0).subs(ics) for n in range(len(ics))]
    sol_params = sympy.solve(eqs, free_params)
    return sol.subs(sol_params)

# This is defining the symbol and function
t, omega0, gamma = sympy.symbols("t, omega_0, gamma", positive= True)
x = sympy.Function('x')

ode = x(t).diff(t,2) + 2*omega0*gamma*x(t).diff(t)+omega0**2*x(t) # This is defining the init condition
ode_sol = sympy.dsolve(ode) # This functions gives a symbol solution

ics = {x(0):1, x(t).diff(t).subs(t,0):0} # This is the init condition, the second of it means the first derivative will be equal to zero at time zero
x_t_sol = apply_ics(ode_sol, ics, t, [omega0, gamma]) # For the know_parms it has to be in a bracket or else it won't work

#This would take the limit as gamma approches zero
x_t_criitcal = sympy.limit(x_t_sol.rhs, gamma, 1)

# This is will plot the function when gama is equal to one and omega equals 5
fig, ax = plt.subplots(figsize=(8,4))
tt = np.linspace(0,3,250)
w0 = 2* sympy.pi

# This would show me the solution of the differential equatio
print(x_t_sol.rhs)
for g in [0.1, 0.5, 1, 2.0, 5.0]:
    if g == 1:
        x_t = sympy.lambdify(t, x_t_criitcal.subs({omega0:w0}), 'numpy') # This turns it into a function
    else:
        x_t = sympy.lambdify(t, x_t_sol.rhs.subs({omega0:w0, gamma:g}), 'numpy') # This turns it into a function
    ax.plot(tt, x_t(tt))# This things plots the function
plt.show()

'''
    This is how you would solve a differential equal, however you just need to be careful to check for typoes
or else it would take you ten years to do it.


'''




