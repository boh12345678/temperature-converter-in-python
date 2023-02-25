def celsius_to_fahrenheit(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

def celsius_to_kelvin(temp_c):
    temp_k = temp_c + 273.15
    return temp_k

def celsius_to_rankine(temp_c):
    temp_r = (temp_c + 273.15) * 9/5
    return temp_r

def celsius_to_reaumur(temp_c):
    temp_re = temp_c * 4/5
    return temp_re

def celsius_to_delisle(temp_c):
    temp_de = (100 - temp_c) * 3/2
    return temp_de

def celsius_to_newton(temp_c):
    temp_n = temp_c * 33/100
    return temp_n

def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

def fahrenheit_to_kelvin(temp_f):
    temp_k = (temp_f + 459.67) * 5/9
    return temp_k

def fahrenheit_to_rankine(temp_f):
    temp_r = temp_f + 459.67
    return temp_r

def fahrenheit_to_reaumur(temp_f):
    temp_re = (temp_f - 32) * 4/9
    return temp_re

def fahrenheit_to_delisle(temp_f):
    temp_de = (212 - temp_f) * 5/6
    return temp_de

def fahrenheit_to_newton(temp_f):
    temp_n = (temp_f - 32) * 11/60
    return temp_n

def kelvin_to_celsius(temp_k):
    temp_c = temp_k - 273.15
    return temp_c

def kelvin_to_fahrenheit(temp_k):
    temp_f = (temp_k * 9/5) - 459.67
    return temp_f

def kelvin_to_rankine(temp_k):
    temp_r = temp_k * 1.8
    return temp_r

def kelvin_to_reaumur(temp_k):
    temp_re = (temp_k - 273.15) * 4/5
    return temp_re

def kelvin_to_delisle(temp_k):
    temp_de = (373.15 - temp_k) * 1.5
    return temp_de

def kelvin_to_newton(temp_k):
    temp_n = (temp_k - 273.15) * 33/100
    return temp_n

def rankine_to_celsius(temp_r):
    temp_c = (temp_r - 491.67) * 5/9
    return temp_c

def rankine_to_fahrenheit(temp_r):
    temp_f = temp_r - 459.67
    return temp_f

def rankine_to_kelvin(temp_r):
    temp_k = temp_r * 5/9
    return temp_k

def rankine_to_reaumur(temp_r):
    temp_re = (temp_r - 491.67) * 4/9
    return temp_re

def rankine_to_delisle(temp_r):
    temp_de = (671.67 - temp_r) * 5/6
    return temp_de

def rankine_to_newton(temp_r):
    temp_n = (temp_r - 491.67) * 33/60
    return temp_n

def reaumur_to_celsius(temp_re):
    temp_c = temp_re * 5/4
    return temp_c

def reaumur_to_fahrenheit(temp_re):
    temp_f = (temp_re * 9/4) + 32
    return temp_f

def reaumur_to_kelvin(temp_re):
    temp_k = (temp_re * 5/4) + 273.15
    return temp_k

def reaumur_to_rankine(temp_re):
    temp_r = (temp_re * 9/4) + 491.67
    return temp_r

def reaumur_to_delisle(temp_re):
    temp_de = (80 - temp_re) * 15/8
    return temp_de

def reaumur_to_newton(temp_re):
    temp_n = temp_re * 11/32
    return temp_n

def delisle_to_celsius(temp_de):
    temp_c = 100 - (temp_de * 2/3)
    return temp_c

def delisle_to_fahrenheit(temp_de):
    temp_f = (212 - (temp_de * 6/5))
    return temp_f

def delisle_to_kelvin(temp_de):
    temp_k = 373.15 - (temp_de * 2/3)
    return temp_k

def delisle_to_rankine(temp_de):
    temp_r = 671.67 - (temp_de * 6/5)
    return temp_r

def delisle_to_reaumur(temp_de):
    temp_re = (80 - temp_de) * 8/15
    return temp_re

def delisle_to_newton(temp_de):
    temp_n = (33 - (temp_de * 22/50))
    return temp_n

def newton_to_celsius(temp_n):
    temp_c = temp_n * 100/33
    return temp_c

def newton_to_fahrenheit(temp_n):
    temp_f = (temp_n * 60/11) + 32
    return temp_f

def newton_to_kelvin(temp_n):
    temp_k = (temp_n * 100/33) + 273.15
    return temp_k

def newton_to_rankine(temp_n):
    temp_r = (temp_n * 60/11) + 491.67
    return temp_r

def newton_to_reaumur(temp_n):
    temp_re = temp_n * 80/33
    return temp_re

def newton_to_delisle(temp_n):
    temp_de = (33 - temp_n) * 50/22
    return temp_de