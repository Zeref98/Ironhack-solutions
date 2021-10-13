# Which sorcerer won the battle - Gandalf or Saruman?
import numpy as np
power = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}
gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']

G_s = []
for i in gandalf:
  G_s.append(power[i])

saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

S_s = []
for i in saruman:
  S_s.append(power[i])
  
G_t = 0
S_t = 0

for i in range(len(gandalf)):
  if G_s[i]>S_s[i]:
    G_t += 1
  elif G_s[i]<S_s[i]:
    S_t += 1
def battle():
  if G_t > S_t:
    solution1 = 'Gandalf'
  elif G_t < S_t:
    solution1 = 'Saruman'
  return solution1
  
av_s_g = np.mean(G_s)
av_s_g = round(av_s_g,1)
av_s_s = np.mean(S_s)
av_s_s = round(av_s_s,1)

#  Average of the spells in the lists? Round off your result to one decimal place.
def avg_spells():
  if G_t > S_t:
    solution2 = av_s_g
  elif G_t < S_t:
    solution2 = av_s_s
  return solution2
  
#  Standard deviation of the spells in the lists? Round off your result to one decimal place.

std_s_g = np.std(G_s)
std_s_g1 = round(std_s_g ,1)
std_s_s = np.std(S_s)
std_s_s1 = round(std_s_s ,1)

def stdev_spells():
  if G_t > S_t:
    solution3 = std_s_g1
  elif G_t < S_t:
    solution3 = std_s_s1
  return solution3
