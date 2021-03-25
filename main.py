# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greetings='Hello'):
    print(f'{greetings}, {name}!')
    return (greetings)

greet('Kevin')



def force(mass,body='earth'):
    gravity={'sun':274,'jupiter':21.9,'neptune':11.9,'saturn':10.4,'earth':9.8,
             'venus':8.8,'mars':3.7,'mercury':3.7,'moon':1.6,'pluto':0.6}
    print('{:.1f}'.format(mass*gravity[body]))
    return (gravity)

force(274,'sun')
force(21.9,'jupiter')
force(11.9,'neptune')
force(10.4,'saturn')
force(9.8,'earth')
force(8.8,'venus')
force(3.7,'mars')
force(3.7,'mercury')
force(1.6,'moon')
force(0.6,'pluto')

def pull(m1,m2,d):
    G=6.7*(10**-11)
    f= G*((m1*m2)/d**2)
    print("the gravitational force is:",round(f,2),"N")
    return G*((m1*m2)/d**2)

pull(800,1500,3)




    
