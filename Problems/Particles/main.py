spin = input()
charge = input()

if spin == '1/2':
    if charge == '-1/3':
        print('Strange Quark')
    elif charge == '2/3':
        print('Charm Quark')
    elif charge == '-1':
        print('Electron Lepton')
    else:
        print('Neutrino Lepton')
else:
    print('Photon Boson')

# Another solution 1
if spin == '1':
    print('Photon Boson')
else:
    particles = {'-1/3': 'Strange Quark',
                 '2/3': 'Charm Quark',
                 '-1': 'Electron Lepton',
                 '0': 'Neutrino Lepton'
                 }
    print(particles[charge])

# Another solution 2
particle_class = {('1/2', '-1/3'): 'Strange Quark',
                  ('1/2', '2/3'): 'Charm Quark',
                  ('1/2', '-1'): 'Electron Lepton',
                  ('1/2', '0'): 'Neutrino Lepton',
                  ('1', '0'): 'Photon Boson'}
spin, electric_charge = input(), input()
print(particle_class[(spin, electric_charge)])

# Another solution 3
if len(input()) == 1:
    print('Photon Boson')
else:
    print(['Neutrino Lepton', 'Electron Lepton', 'Charm Quark', 'Strange Quark'][len(input()) - 1])