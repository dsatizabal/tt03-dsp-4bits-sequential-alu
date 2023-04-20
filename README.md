![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg)

# 4-bits sequential ALU

This ALU takes 4-bits wide operators and operation sequentially trhough the 4 MSBs of io_in (please refer to TinyTapeout specs for details)

Supported operations are:

- Sum (opcode = 0)
- Substracion (opcode = 1)
- Logical AND (opcode = 2)
- Logical OR (opcode = 3)
- Logical NOT (opcode = 4)
- Logical NAND (opcode = 5)
- Logical NOR (opcode = 6)

## pins

All pins follow positive logic so active state is a high voltage level or "1"

_inputs_
- io_in[0] = external clock
- io_in[1] = reset
- io_in[2] = enabled
- io_in[3] = unused
- io_in[7:4] = data in

_outputs_
- io_out[3:0] = result
- io_in[4] = done flag
- io_in[5] = carry flag
- io_in[6] = zero flag
- io_in[7] = sign flag


## Operation

When reset input is set to high for a clock cycle, the result and al flags are set to 0 as default values

If clock continues but enabled input is low then ALU does not operates

When enabled input is set to high the ALI will fetch sequentially operand1, operand2 and operation on every positive edge of the clock, it takes an additional clock to calculate and output results.

It is important to note that:

- If no clock signal is given the ALU won't operate properly
- For operations that require a single operand, like Logical NOT, it's still required to provide the second operand and the corresponding clock to fetch that, the value of this second operand is ignored to perform such operations.

If the result of the operation is 0 the the zero flag will be activated.
It is verified that the result involves sign and carry for SUM and SUB opreations and the corresponding flag is set to high if applicable.
On the 4th clock cycle of eveery operation the calculations are performed, result placed for output and DONE flag is set to high.

## Acknowldgements

This project was made as part of the [Zero2ASIC](https://zerotoasiccourse.com/) course using the Tiny Tapeout project (more info below) which I absolutely recommend the reader to checkout and enroll. Special thanks to Matt Venn and all the Zero2ASIC community for the constant support and knowledge sharing.

## What is Tiny Tapeout?

TinyTapeout is an educational project that aims to make it easier and cheaper than ever to get your digital designs manufactured on a real chip!

Go to https://tinytapeout.com for instructions!

### How to change the Wokwi project

Edit the [info.yaml](info.yaml) and change the wokwi_id to match your project.

### How to enable the GitHub actions to build the ASIC files

Please see the instructions for:

* [Enabling GitHub Actions](https://tinytapeout.com/faq/#when-i-commit-my-change-the-gds-action-isnt-running)
* [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

### How does it work?

When you edit the info.yaml to choose a different ID, the [GitHub Action](.github/workflows/gds.yaml) will fetch the digital netlist of your design from Wokwi.

After that, the action uses the open source ASIC tool called [OpenLane](https://www.zerotoasiccourse.com/terminology/openlane/) to build the files needed to fabricate an ASIC.

### Resources

* [FAQ](https://tinytapeout.com/faq/)
* [Digital design lessons](https://tinytapeout.com/digital_design/)
* [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
* [Join the community](https://discord.gg/rPK2nSjxy8)

### What next?

* Share your GDS on Twitter, tag it [#tinytapeout](https://twitter.com/hashtag/tinytapeout?src=hashtag_click) and [link me](https://twitter.com/matthewvenn)!
