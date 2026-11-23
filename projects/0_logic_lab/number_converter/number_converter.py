#!/usr/bin/env python3
#Small base converter
#Usages:
#    python number_converter.py 45 --from-base dec
#    python number_converter.py 101101 --from-base bin --width 8
#    python number_converter.py 0x2D
#    python number_converter.py -18 --from-base dec --signed-width 8
import argparse

def parse_integer(value: str, base: str) -> int:
    #Parse a number using the selected base.
    prefixes = {"bin": "0b", "dec": "", "hex": "0x"}
    cleaned = value.strip().replace("_", "")

    if base == "auto":
        return int(cleaned, 0)
    return int(cleaned, {"bin": 2, "dec": 10, "hex": 16}[base])

def format_unsigned(value: int, width: int | None = None) -> str:
    #Format a non-negative integer as binary, optionally zero-padded.
    if value < 0:
        raise ValueError("Unsigned formatting requires a non-negative value.")
    bits = format(value, "b")
    if width is not None:
        if width <= 0:
            raise ValueError("Width must be positive.")
        if value >= (1 << width):
            raise ValueError(f"{value} does not fit in {width} unsigned bits.")
        bits = bits.zfill(width)
    return bits

def encode_twos_complement(value: int, width: int) -> str:
    #Encode a signed integer as a fixed-width two's-complement bit string.
    if width <= 0:
        raise ValueError("Width must be positive.")
    minimum = -(1 << (width - 1))
    maximum = (1 << (width - 1)) - 1
    if not minimum <= value <= maximum:
        raise ValueError(
            f"{value} is outside the {width}-bit signed range "
            f"[{minimum}, {maximum}]."
        )
    return format(value & ((1 << width) - 1), f"0{width}b")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("value", help="Input integer, e.g. 45, 101101, or 0x2D")
    parser.add_argument(
        "--from-base",
        choices=("auto", "bin", "dec", "hex"),
        default="auto",
        help="Interpretation of the input (default: detect 0b/0x prefixes)",
    )
    parser.add_argument("--width", type=int, help="Optional unsigned binary width")
    parser.add_argument(
        "--signed-width",
        type=int,
        help="Also show fixed-width two's-complement encoding",
    )
    args = parser.parse_args()

    try:
        number = parse_integer(args.value, args.from_base)
        if args.width is not None and number < 0:
            raise ValueError("--width is for unsigned binary formatting.")

        print(f"Decimal: {number}")
        if number >= 0:
            print(f"Binary:  {format_unsigned(number, args.width)}")
            print(f"Hex:     0x{number:X}")
        else:
            print("Binary:  (use --signed-width for two's-complement encoding)")
            print(f"Hex of magnitude: 0x{abs(number):X}")

        if args.signed_width is not None:
            print(
                f"Signed {args.signed_width}-bit two's complement: "
                f"{encode_twos_complement(number, args.signed_width)}"
            )
    except (ValueError, KeyError) as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()
