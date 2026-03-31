#
#  Digits on display
#

from microbit import *

display.clear()

zero = Image("99999:"
             "90009:"
             "90009:"
             "90009:"
             "99999")

display.show(zero)
sleep(500)

ten = Image("90999:"
            "90909:"
            "90909:"
            "90909:"
            "90999")

display.show(ten)
sleep(500)
