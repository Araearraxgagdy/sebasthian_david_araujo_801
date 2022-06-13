def on_forever():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . # .
                . . # . .
                . . # . .
    """)
    basic.pause(100)
    basic.show_leds("""
        # . . . .
                . # . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . .
                # . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . # .
                . . # . .
                . . # . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . # .
                . . . # .
                . . # . .
                . . # . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . .
                # # . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . #
                . . . # .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . # #
                . . . . #
                . . . # .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . # . #
                . # # # .
                # # # # #
                . # # # .
                # . # . #
    """)
    basic.pause(2000)
    basic.pause(0)
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . # # .
                . . # . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . # # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . #
                . . . # #
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . # . .
                . . . # .
                . . # . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . # . #
                . # # # .
                # # # # #
                . # # # .
                # . # . #
    """)
    basic.pause(2000)
    basic.show_number(801)
    basic.pause(3000)
basic.forever(on_forever)
