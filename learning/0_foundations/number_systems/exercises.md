# D2 Exercise Record — Number Systems

**Workspace:** ChipSpace  
**Branch:** `NOV_BW1_D2`  
**Date:** 23 November 2026

## 1. Initial checkpoint

| Question | Topic | Recorded answer | Review |
|---|---|---|---|
| Q1 | Binary to decimal: `110101₂` | 53 | Correct |
| Q2 | Decimal to binary: `73₁₀` | `1001001` | Correct |
| Q3 | Binary to hex: `101111001₂` | `0xB9` | Incorrect; correct result is `0x179` |
| Q4 | 8-bit two's complement for -18 | `11101110` | Correct |
| Q5 | 8-bit unsigned storage of 250 + 20 | 270; `10101010`; no carry; width unknown | Partial; correct result below |

### Q5 correction

```text
  11111010   250
+ 00010100    20
-----------
1 00001110   270
```

- Mathematical result: 270
- Full result: `100001110` (9 bits)
- Carry-out: 1
- Low 8 stored bits: `00001110`
- Stored unsigned value: 14
- Minimum unsigned width for 270: 9 bits

## 2. Remediation checkpoint

| Question | Recorded answer | Review |
|---|---|---|
| A | `1101011010₂` → `0x35A` | Correct |
| B | 200 + 100 = 300; `100100010`; carry 1; stored 34 | Partial; correct full result is `100101100`, low 8 bits `00101100`, stored value 44 |
| C | 300 needs 9 bits because 8-bit max is 255 | Correct |

### B correction

```text
  11001000   200
+ 01100100   100
-----------
1 00101100   300
```

- Mathematical result: 300
- Full result: `100101100` (9 bits)
- Carry-out: 1
- Low 8 stored bits: `00101100`
- Stored unsigned value: 44

## 3. Learning assessment

Demonstrated:
- Binary-to-decimal conversion.
- Decimal-to-binary conversion.
- Two's-complement encoding for a negative number.
- Unsigned range and minimum-width reasoning.
- Basic understanding of carry-out and truncation.

Reinforcement needed:
- Grouping binary digits into four-bit nibbles without dropping a group.
- Performing binary addition carefully and checking the result.
- Distinguishing full-width results from truncated destination values.

## 4. Personal engineering procedure

For manual binary arithmetic:
1. Write operands at equal declared width.
2. Add from right to left.
3. Record each carry explicitly.
4. Preserve the carry-out separately.
5. Separate the full result from the destination-width result.
6. Convert the retained bits back to decimal as a check.

Mental arithmetic speed is not an acceptance criterion. Correct reasoning, explicit working, and verification are.

## 5. Status

**Core concepts:** demonstrated.  
**Arithmetic accuracy:** continue practicing in later adder, ALU, and MAC exercises.  
**Next use:** apply width and signedness rules in combinational RTL.
