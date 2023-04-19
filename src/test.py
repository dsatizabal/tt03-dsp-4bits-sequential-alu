import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

ops1    = [1, 1, 2, 3]
ops2    = [2, 1, 2, 3]
opcodes = [0, 0, 0, 0]
results = [3, 2, 4, 6]
flags   = [1, 1, 1, 1]

@cocotb.test()
async def test_4bits_alu(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 10, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0

    dut._log.info("Iterate through operations")

    for i in range(4):
        dut._log.info(f"Beginning {dut.alu_state.value}")

        dut.data_in.value = ops1[i]
        await ClockCycles(dut.clk, 1)

        dut._log.info(f"After first clk {dut.alu_state.value}")

        dut.data_in.value = ops2[i]
        await ClockCycles(dut.clk, 1)

        dut._log.info(f"After second clk {dut.alu_state.value}")

        dut.data_in.value = opcodes[i]
        await ClockCycles(dut.clk, 1)

        dut._log.info(f"After third clk {dut.alu_state.value}")

        assert dut.result.value == results[i], f'Invalid result at position {i}, expected {results[i]} got {dut.result.value}, ALU state was {dut.alu_state.value}, {dut.op1.value}, {dut.op2.value}, {dut.operation.value}'
        assert dut.sign_zero_carry_done.value == flags[i], f'Invalid flag at position {i}, expected {flags[i]} got {dut.sign_zero_carry_done.value}'

        dut.reset.value = 1
        await ClockCycles(dut.clk, 1)
        dut.reset.value = 0
        dut._log.info(f"After final reset {dut.alu_state.value}")
