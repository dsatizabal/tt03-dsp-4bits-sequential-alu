import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

# 2 + 2 = 4 with only DONE flag
# 0 + 6 = 6 with only DONE flag
# 9 + 9 = 2 with CARRY and DONE flag
# 7 + 8 = 15 with only DONE flag
ops1_sum    = [2, 0, 9, 7]
ops2_sum    = [2, 6, 9, 8]
opcodes_sum = [0, 0, 0, 0]
results_sum = [4, 6, 2, 15]
flags_sum   = [1, 1, 3, 1] #sign_zero_carry_done

ops1_sub    = [2, 6, 9]
ops2_sub    = [2, 7, 5]
opcodes_sub = [1, 1, 1]
results_sub = [0, 15, 4]
flags_sub   = [5, 9, 1] #sign_zero_carry_done

ops1_and    = [2, 4, 0, 15]
ops2_and    = [2, 5, 0, 1]
opcodes_and = [2, 2, 2, 2]
results_and = [2, 4, 0, 1]
flags_and   = [1, 1, 5, 1] #sign_zero_carry_done

ops1_or    = [2, 4, 0, 15]
ops2_or    = [2, 1, 0, 1]
opcodes_or = [3, 3, 3, 3]
results_or = [2, 5, 0, 15]
flags_or   = [1, 1, 5, 1] #sign_zero_carry_done

ops1_not    = [0, 10, 15]
ops2_not    = [0, 0, 0]
opcodes_not = [4, 4, 4]
results_not = [15, 5, 0]
flags_not   = [1, 1, 5] #sign_zero_carry_done

ops1_nand    = [0, 1, 2, 15]
ops2_nand    = [0, 0, 2, 15]
opcodes_nand = [5, 5, 5, 5]
results_nand = [15, 15, 13, 0]
flags_nand   = [1, 1, 1, 5] #sign_zero_carry_done

ops1_nor    = [0, 1, 2, 15]
ops2_nor    = [0, 0, 2, 15]
opcodes_nor = [6, 6, 6, 6]
results_nor = [15, 14, 13, 0]
flags_nor   = [1, 1, 1, 5] #sign_zero_carry_done

ops1_rl    = [0, 1, 8, 15]
ops2_rl    = [0, 0, 0, 15]
opcodes_rl = [7, 7, 7, 7]
results_rl = [0, 2, 1, 15]
flags_rl   = [5, 1, 1, 1] #sign_zero_carry_done

ops1_rr    = [0, 1, 8, 15]
ops2_rr    = [0, 0, 0, 15]
opcodes_rr = [8, 8, 8, 8]
results_rr = [0, 8, 4, 15]
flags_rr   = [5, 1, 1, 1] #sign_zero_carry_done

ops1_swap    = [0, 1, 8, 15]
ops2_swap    = [0, 0, 0, 15]
opcodes_swap = [9, 9, 9, 9]
results_swap = [0, 4, 2, 15]
flags_swap   = [5, 1, 1, 1] #sign_zero_carry_done

ops1_cmp    = [0, 4, 5, 10]
ops2_cmp    = [0, 4, 9, 2]
opcodes_cmp = [10, 10, 10, 10]
results_cmp = [1, 1, 2, 4]
flags_cmp   = [1, 1, 1, 1] #sign_zero_carry_done

@cocotb.test()
async def tests_sum(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through SUM operations")

    for i in range(len(ops1_sum)):
        dut.enabled.value = 1

        dut.data.value = ops1_sum[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_sum[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_sum[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_sum[i], f'Invalid result at position {i}, expected {results_sum[i]} got {dut.result.value}'
        assert dut.flags.value == flags_sum[i], f'Invalid flag at position {i}, expected {flags_sum[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_sub(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through SUB operations")

    for i in range(len(ops1_sub)):
        dut.enabled.value = 1

        dut.data.value = ops1_sub[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_sub[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_sub[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_sub[i], f'Invalid result at position {i}, expected {results_sub[i]} got {dut.result.value}'
        assert dut.flags.value == flags_sub[i], f'Invalid flag at position {i}, expected {flags_sub[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_and(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through AND operations")

    for i in range(len(ops1_and)):
        dut.enabled.value = 1

        dut.data.value = ops1_and[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_and[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_and[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_and[i], f'Invalid result at position {i}, expected {results_and[i]} got {dut.result.value}'
        assert dut.flags.value == flags_and[i], f'Invalid flag at position {i}, expected {flags_and[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_or(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through OR operations")

    for i in range(len(ops1_or)):
        dut.enabled.value = 1

        dut.data.value = ops1_or[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_or[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_or[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_or[i], f'Invalid result at position {i}, expected {results_or[i]} got {dut.result.value}'
        assert dut.flags.value == flags_or[i], f'Invalid flag at position {i}, expected {flags_or[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_not(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through NOT operations")

    for i in range(len(ops1_not)):
        dut.enabled.value = 1

        dut.data.value = ops1_not[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_not[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_not[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_not[i], f'Invalid result at position {i}, expected {results_not[i]} got {dut.result.value}'
        assert dut.flags.value == flags_not[i], f'Invalid flag at position {i}, expected {flags_not[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_nand(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through NAND operations")

    for i in range(len(ops1_nand)):
        dut.enabled.value = 1

        dut.data.value = ops1_nand[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_nand[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_nand[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_nand[i], f'Invalid result at position {i}, expected {results_nand[i]} got {dut.result.value}'
        assert dut.flags.value == flags_nand[i], f'Invalid flag at position {i}, expected {flags_nand[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_nor(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through NOR operations")

    for i in range(len(ops1_nor)):
        dut.enabled.value = 1

        dut.data.value = ops1_nor[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_nor[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_nor[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_nor[i], f'Invalid result at position {i}, expected {results_nor[i]} got {dut.result.value}'
        assert dut.flags.value == flags_nor[i], f'Invalid flag at position {i}, expected {flags_nor[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_rl(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through RL operations")

    for i in range(len(ops1_rl)):
        dut.enabled.value = 1

        dut.data.value = ops1_rl[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_rl[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_rl[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_rl[i], f'Invalid result at position {i}, expected {results_rl[i]} got {dut.result.value}'
        assert dut.flags.value == flags_rl[i], f'Invalid flag at position {i}, expected {flags_rl[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_rr(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through RR operations")

    for i in range(len(ops1_rr)):
        dut.enabled.value = 1

        dut.data.value = ops1_rr[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_rr[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_rr[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_rr[i], f'Invalid result at position {i}, expected {results_rr[i]} got {dut.result.value}'
        assert dut.flags.value == flags_rr[i], f'Invalid flag at position {i}, expected {flags_rr[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_swap(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through SWAP operations")

    for i in range(len(ops1_swap)):
        dut.enabled.value = 1

        dut.data.value = ops1_swap[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_swap[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_swap[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_swap[i], f'Invalid result at position {i}, expected {results_swap[i]} got {dut.result.value}'
        assert dut.flags.value == flags_swap[i], f'Invalid flag at position {i}, expected {flags_swap[i]} got {dut.flags.value}'

@cocotb.test()
async def tests_cmp(dut):
    dut._log.info("start")

    clock = Clock(dut.clk, 1, units="us")

    cocotb.start_soon(clock.start())

    dut._log.info("Resetting ALU")

    dut.enabled.value = 0
    dut.reset.value = 1
    await ClockCycles(dut.clk, 2)
    dut.reset.value = 0
    await ClockCycles(dut.clk, 2)

    dut._log.info("Iterate through CMP operations")

    for i in range(len(ops1_cmp)):
        dut.enabled.value = 1

        dut.data.value = ops1_cmp[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = ops2_cmp[i]
        await ClockCycles(dut.clk, 1)

        dut.data.value = opcodes_cmp[i]
        await ClockCycles(dut.clk, 2)

        dut.enabled.value = 0
        await ClockCycles(dut.clk, 1)

        assert dut.result.value == results_cmp[i], f'Invalid result at position {i}, expected {results_cmp[i]} got {dut.result.value}'
        assert dut.flags.value == flags_cmp[i], f'Invalid flag at position {i}, expected {flags_cmp[i]} got {dut.flags.value}'
