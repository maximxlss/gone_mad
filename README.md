# GONE MAD (GO Number E MADfuscator)

Inspired by the [Go language specification](https://go.dev/ref/spec).

Ever thought that your magic numbers aren't magic enough? Well, Go's got you covered; there is plenty of number literal syntax to make your numbers ever more unhinged and mystical!

Examples:
- `+0X0.P-0` - Glorious and consise zero
- `+0XCcCcccccCccC_D.p-_54` - 0.2 (it's good that you can see it's imprecision)
- `+0X1_ec7_DF3b645_A1d.P-46` - is obviously 123.123
- `+0x5F3_759Df.p-0` - Magic invsqrt number
- `+0X68_747470733a2f2F_77777_72e796_F7_5747_562652E636F6_D2F776_17_463_683_f763D645177_34_773957_675863_51.P-0` - rickroll
- `+0X_1.p-1-0X1.P-1i` - 0.5-0.5i
- `+0x11A658_04A3_D3a_F.P-47+0x116F_4D69aA_bE_85.P-4_5i` - a certain place in Japan
- [too long](./main.gonumber) - source code of the script itself

Just run `python main.py`, no dependencies.

Note: floats will lose precision and stuff probably