{ pkgs, lib, ... }:
let
  buildInputs = [
    pkgs.libxcb
    pkgs.libGL
    pkgs.glib
    pkgs.stdenv.cc.cc
    pkgs.libuv
    pkgs.zlib
    pkgs.libxext
    pkgs.libx11
    pkgs.libsm
    pkgs.libice
    pkgs.zbar
  ];
in
{
  env = {
    LD_LIBRARY_PATH = "${lib.makeLibraryPath buildInputs}";
  };

  packages = [ pkgs.pandoc ];

  profiles = {
    main.module = {
      languages.python = {
        enable = true;
        uv = {
          enable = true;
          sync.enable = true;
        };
      };
    };

    marimo = {
      extends = [ "main" ];
      module = {
        scripts.run-marimo.exec = "marimo edit --no-token";
        enterShell = ''
          . .devenv/state/venv/bin/activate
          run-marimo && clear && cat ascii-art.txt
          sleep 1 && clear
        '';
      };
    };

    get-shell = {
      extends = [ "main" ];
      module = {
        enterShell = ''
          . .devenv/state/venv/bin/activate
        '';
      };
    };
  };
}
