import os
from pathlib import Path

import cocotb
from cocotb.runner import get_runner


def test_runner(design_name):
    sim = os.getenv("SIM", "verilator")
    project_path = Path(__name__).resolve().parent.parent
    source_code = list(project_path.glob("src/*.sv"))
    runner = get_runner(sim)
    print(f"--trace {project_path}/packages/fermi32.sv")
    runner.build(
        sources=source_code,
        hdl_toplevel=f"{design_name}",
        build_dir=f"./{design_name}/sim_build",
        build_args=[
            f"--trace",
            "--trace-structs",
            "--trace",
            f"{project_path}/packages/fermi32.sv",
        ],
    )
    runner.test(
        hdl_toplevel=f"{design_name}",
        test_module=f"test_{design_name}",
        test_dir=f"./{design_name}",
    )

if __name__ == "__main__":
