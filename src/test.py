import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

# 2 - 2 = 0 with zero and done flags
# 1 + 1 = 2 with done flag
# 2 + 2 = 4 with done flag
ops1    = [2, 1, 2, 4, 5, 3]
ops2    = [2, 1, 2, 1, 4, 2]
opcodes = [1, 0, 0, 3, 2, 1]
results = [0, 2, 4, 5, 5, 0]
flags   = [5, 1, 1, 7, 1, 9] #sign_zero_carry_done

@cocotb.test()
async def test_4bits_alu(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.process.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through operations")

    for i in range(4):
        dut.process.value = 1

        dut.data.value = ops1[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes[i]
        await ClockCycles(dut.clk, 2)

        dut.process.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results[i], f'Invalid result at position {i}, expected {results[i]} got {dut.result.value}'
        assert dut.flags.value == flags[i], f'Invalid flag at position {i}, expected {flags[i]} got {dut.flags.value}'

