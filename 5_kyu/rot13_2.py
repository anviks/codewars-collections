"""https://www.codewars.com/kata/52223df9e8f98c7aa7000062"""

rot13 = lambda s: __import__('codecs').encode(s, 'rot13')


def main():
    from util_funcs import pretty_compare

    pretty_compare(rot13("EBG13 rknzcyr."), "ROT13 example.")
    pretty_compare(rot13(
        "How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."),
        "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
    pretty_compare(rot13("123"), "123")
    pretty_compare(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"),
                   "This is actually the first kata I ever made. Thanks for finishing it! :)")
    pretty_compare(rot13("@[`{"), "@[`{")


if __name__ == '__main__':
    main()
