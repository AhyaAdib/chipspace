# Number Systems and Binary Arithmetic

**Workspace:** ChipSpace  
**Branch:** `NOV_BW1_D2`  
**Lane:** A — Digital Foundations  
**Status:** Learning reference  
**Date:** 23 November 2026

## 1. Why number representation matters

Digital hardware represents information as bit-vectors. A bit is interpreted as either logic 0 or logic 1. The same bit pattern can represent different values depending on its interpretation, width, and signedness.

For example, the 4-bit pattern `1101` represents:
- 13 as an unsigned integer.
- -3 as a 4-bit two's-complement signed integer.

A bit-vector does not inherently know whether it represents an integer, address, instruction, or signal. The designer defines its meaning.

## 2. Binary place value

Binary is base 2. Each bit position has a weight that is a power of two.

For an unsigned n-bit vector:

`b[n-1] ... b[1] b[0]`

its value is:

`V = sum(b[i] * 2**i)` for i = 0 through n-1.

Example:

`1101₂ = 1*8 + 1*4 + 0*2 + 1*1 = 13₁₀`

To convert a positive decimal integer to binary, repeatedly divide by 2 and read the remainders from bottom to top. Alternatively, decompose the number into powers of two.

## 3. Hexadecimal

Hexadecimal is base 16. One hexadecimal digit represents exactly four bits (one nibble).

| Hex | Binary | Decimal |
|---|---|---:|
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 2 | 0010 | 2 |
| 3 | 0011 | 3 |
| 4 | 0100 | 4 |
| 5 | 0101 | 5 |
| 6 | 0110 | 6 |
| 7 | 0111 | 7 |
| 8 | 1000 | 8 |
| 9 | 1001 | 9 |
| A | 1010 | 10 |
| B | 1011 | 11 |
| C | 1100 | 12 |
| D | 1101 | 13 |
| E | 1110 | 14 |
| F | 1111 | 15 |

For binary-to-hex conversion:
1. Group bits into groups of four, starting at the right.
2. Pad the leftmost group with zeros if necessary.
3. Convert each group to one hex digit.

Example:

`1101011010₂` → `0011 0101 1010` → `0x35A`.

In Verilog, `8'h2D` means an 8-bit hexadecimal literal with bit pattern `00101101`.

## 4. Bit width and unsigned range

An n-bit vector has `2**n` distinct bit patterns.

For an unsigned n-bit integer:

`0 <= value <= 2**n - 1`

Examples:
- 4 bits: 0 to 15
- 8 bits: 0 to 255
- 16 bits: 0 to 65,535

If a result is wider than its destination, assigning only the low bits truncates the upper bits. For example, storing 270 in 8 bits retains:

`270 mod 256 = 14`

The retained pattern is `00001110`. The discarded ninth bit is 1.

## 5. Signed two's-complement representation

For n-bit two's-complement integers:

`-2**(n-1) <= value <= 2**(n-1) - 1`

For 8 bits, the range is -128 to +127.

To encode a negative value -x:
1. Write +x in the selected width.
2. Invert every bit.
3. Add 1, keeping the selected width.

Example: encode -18 in 8 bits.

```text
+18       00010010
invert    11101101
add 1     11101110
```

The result `11101110` represents -18.

For a two's-complement vector, the MSB has weight `-2**(n-1)` and the remaining bits have positive weights.

## 6. Zero extension and sign extension

When widening an unsigned value, use zero extension: add zeros on the left.

When widening a signed two's-complement value, use sign extension: replicate the original sign bit on the left.

Example, widening the 4-bit pattern `1011`:
- Unsigned 11 → `00001011` (8 bits).
- Signed -5 → `11111011` (8 bits).

Using the wrong extension changes the value.

## 7. Addition, carry-out, and overflow

For two unsigned n-bit operands, the full-precision sum may require n+1 bits.

Example:

```text
  11111010   250
+ 00010100    20
-----------
1 00001110   270 (9-bit result)
```

If only the low 8 bits are retained:
- Stored bits: `00001110`
- Stored unsigned value: 14
- Carry-out: 1

Fixed-width unsigned arithmetic wraps modulo `2**n`.

Do not confuse unsigned carry-out with signed overflow:
- Unsigned overflow is indicated by a carry beyond the most significant bit.
- Signed two's-complement overflow occurs when adding operands with the same sign produces a result with the opposite sign.

For example, in 4-bit signed arithmetic, `0111 (+7) + 0001 (+1) = 1000`, whose signed interpretation is -8. The mathematical result +8 is outside the 4-bit signed range.

## 8. Subtraction using two's complement

Subtraction can be performed as:

`A - B = A + (~B) + 1`

For a fixed-width datapath, invert B within that width and set the adder carry-in to 1.

Example, 4-bit `7 - 5`:

```text
A        0111
B        0101
~B       1010
~B + 1   1011
A + ...  1 0010
```

Discarding the carry-out leaves `0010` (2).

## 9. Connection to datapaths and AI accelerators

A multiply-accumulate unit computes:

`acc_next = acc + (x * w)`

The designer must determine:
- Whether inputs are signed or unsigned.
- Input widths.
- Full product width.
- Accumulator width.
- Whether rounding, saturation, or truncation is used.
- Fixed-point scaling and where fractional bits are located.

For two signed 8-bit operands, a 16-bit product is sufficient to represent the full product range. Accumulating many products generally requires a wider accumulator or an explicitly designed overflow policy.

## 10. Engineering checklist

Before implementing arithmetic in RTL, ask:
1. What is the width of each operand?
2. Is each operand signed or unsigned?
3. What width is required for the full mathematical result?
4. Are any bits intentionally truncated?
5. Is carry-out observable?
6. Is signed overflow possible?
7. Is the chosen behavior wraparound, saturation, or something else?

## 11. Key takeaway

Bit width and signedness are part of the hardware specification. A correct mathematical formula can still produce an incorrect hardware result if widths, extensions, or truncation are handled incorrectly.
