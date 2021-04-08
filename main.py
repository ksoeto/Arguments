# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#part 1 greet
def greet(name, greeting='Hello, <name>!'):
    name = greeting.replace('<name>',name)
    return name


# part 2 force
def force(mass,body='earth'):
    gravity={'sun':274,
            'jupiter':21.9,
            'neptune':11.9,
            'saturn':10.4,
            'earth':9.8,
             'venus':8.8,
             'mars':3.7,
             'mercury':3.7,
             'moon':1.6,
             'pluto':0.6}
    force_1=round(mass*gravity[body],1)
    return force_1

# part 3 pull
def pull(m1,m2,d):
    G=6.674*(10**-11)
    f=G*((m1*m2)/d**2)
    return G*((m1*m2)/d**2)

pull(800,1500,3)






    
