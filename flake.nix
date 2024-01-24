{
  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/*.tar.gz";
  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
      {
        devShells = forEachSupportedSystem ({ pkgs }:
          let
          in
            {
              default = pkgs.mkShell {
                packages = with pkgs; [
                  python311       # Python 3.11
                  yosys           # RTL synthesis
                  symbiyosys      # Yosys-based formal verification flow
                  boolector       # SMT solver
                  nextpnr         # RTL synthesis to FPGA configuration
                  icestorm        # Lattice iCE40 FPGA utils
                  openfpgaloader  # Universal FPGA + flash programmer
                  openocd         # On-chip debugging
                  gtkwave         # Wave and logic analyzer
                  verilator       # Verilog simulator
                ] ++ (with pkgs.python311Packages; [
                  amaranth        # HDL toolchain for Python
                  amaranth-boards # Amaranth PCBA feature support
                  cocotb          # Python testbench library
                  numpy           # Numeric calculations
                  scipy           # Scientific calculations
                  matplotlib      # Plotting
                ]);
              };
            });
      };
}
