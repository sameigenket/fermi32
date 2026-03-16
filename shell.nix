{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  packages = with pkgs; [
    verilator
    tcl
    gnumake
    nextpnr
    (pkgs.python3.withPackages (
      python-pkgs:
        with python-pkgs; [
          cocotb
          pytest
        ]
    ))
  ];
}
