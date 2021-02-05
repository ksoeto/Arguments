# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(greeting, name='Kevin'):
    return '{}, {}'.format(greeting, name)

print(greet('Hello', name='Kevin!'))



def force(mass,body='earth'):
    print(f'{mass} {body}')
    return (mass,body)


force(mass=274,body="sun")
force(mass=21.9,body="Jupiter")
force(mass=11.9, body="Neptune")
force(mass=10.4, body="Saturn")
force(mass=9.8, body="Earth")
force(mass=8.8, body="Uranus")
force(mass=8.8, body="Venus")
force(mass=3.7, body="Mars")
force(mass=3.7, body="Mercury")
force(mass=1.6, body="Moon")
force(mass=0.6, body="Pluto")

def pull(m1,m2,d):
    m1 = float(input("800:")) 
    m2 = float(input("1500KG:")) 
    d = float (input("distance:")) 
    G=6.7*(10**-11)
    f=(G*m1*m2)/(d**2)
    print("the gravitational force is: ",round(f,2),"N")
    
    return (G*m1*m2)/(d**2)

pull(m1=800,m2=1500,d=3)



    
