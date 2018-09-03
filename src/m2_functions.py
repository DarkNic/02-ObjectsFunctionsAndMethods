"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Nicolas Bohner.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
#
# Done: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
#
###############################################################################

import rosegraphics as rg


def main():
    """
    TESTS the functions that you will write below.
    You write the tests per the _TODO_s below.
    """
    print(hype(2, 2))
    pen1('red', 20)

###############################################################################
#
# Done: 3a.  Define a function immediately blow this _TODO_.
#   It takes two arguments that denote, for a right triangle,
#   the lengths of the two sides adjacent to its right angle,
#   and it returns the length of the hypotenuse of that triangle.
#     HINT: Apply the Pythagorean theorem.
#
#   You may name the function and its parameters whatever you wish.
#
# Done: 3b.  In main, CALL your function and print the returned value,
#   to test whether you defined the function correctly.
#
###############################################################################
def hype(height, width):
    a = height**2+width**2
    b = a**.5
    return b

###############################################################################
#
# Done: 4a.  Define a function immediately below this _TODO_.
#   It takes two arguments:
#     -- a string that represents a color (e.g. 'red')
#     -- a positive integer that represents the thickness of a Pen.
#
#   The function:
#     -- Constructs a TurtleWindow.
#     -- Constructs two SimpleTurtles, where:
#        - one has a Pen whose color is "green" and has the GIVEN thickness
#        - the other has a Pen whose color is the GIVEN color
#            and whose thickness is 5
#     -- Makes the first (green) SimpleTurtle move FORWARD 100 pixels, and
#        makes the other SimpleTurtle move BACKWARD 100 pixels.
#
#   You may name the function and its parameters whatever you wish.
#
# Done: 4b.  In main, CALL your function and print the returned value,
#   to test whether you defined the function correctly.
#
###############################################################################

def pen1(color, thickness):
    window = rg.TurtleWindow()
    green_turtle = rg.SimpleTurtle('turtle')
    thick_turtle = rg.SimpleTurtle('turtle')
    green_turtle.pen = rg.Pen('green', thickness)
    thick_turtle.pen = rg.Pen(color, 5)
    green_turtle.forward(100)
    thick_turtle.backward(100)

    window.close_on_mouse_click()

###############################################################################
#
# TODO: 5.
#   COMMIT-and-PUSH your work (after changing this TO-DO to DONE).
#
#   As a reminder, here is how you should do so:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up:
#          - HOVER over the  Commit  button
#              (in the lower-right corner of the window)
#          - CLICK on  Commit and Push.
#          - Select  Push  when asked.
#
#   COMMIT adds the changed work to the version control on your computer
#   and PUSH adds the changed work into your Github repository in the "cloud".
#
#    COMMIT-and-PUSH your work as often as you want, but at least for each
#    module after you have tested the module and believe that it is correct.
#
###############################################################################

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
