import random

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def load_store_test(dut):
    word = 0x123ABC00
    # Store Word
    dut.f3.value = 0b010

    for _ in range(100):
        register_data = random.randint(0, 0xFFFFFFFF)
        dut.reg_read.value = register_data
        for offset in range(4):
            dut.alu_result_address.value = word | offset
            await Timer(1, unit="ns")
            assert dut.data.value == register_data & 0xFFFFFFFF
            if offset == 0b00:
                assert dut.byte_enable.value == 0b1111
            else:
                assert dut.byte_enable.value == 0b0000

    # Store Byte
    await Timer(10, unit="ns")

    dut.f3.value = 0b000

    # TODO build SB testbench

    # Store Halfword
    await Timer(10, unit="ns")

    dut.f3.value = 0b001
