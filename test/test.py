# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    dut.ui_in.value = 0b10010101
    dut.uio_in.value = 0b10101010
    await ClockCycles(dut.clk, 1)
    assert dut.uio_oe.value == 0b00000000

    dut.ui_in.value = 0b10010110
    dut.uio_in.value = 0b11001100
    await ClockCycles(dut.clk, 1)
    assert dut.uio_oe.value == 0b00000000

    dut.ui_in.value = 0b10010111
    dut.uio_in.value = 0b11110000
    await ClockCycles(dut.clk, 1)
    assert dut.uio_oe.value == 0b00000000
    
    dut.ui_in.value = 0b00010101
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b10101010
    assert dut.uio_out.value == 0b11001100
    assert dut.uio_oe.value == 0b11111111

    dut.ui_in.value = 0b00010110
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b11001100
    assert dut.uio_out.value == 0b11110000
    assert dut.uio_oe.value == 0b11111111

