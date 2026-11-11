# Nand2Tetris Capstone: Make the Computer Draw a Box

Name: Kenisha Randhawa
Roll no: 2501730091
K = 91

## Box details
- Start row: 91 (address 19296 = 16384 + 32 x 91)
- Size: 64 x 20 pixels (4 words wide, 20 rows tall)
- Assembler extra feature (K mod 3 = 1): clear error messages with line numbers

## Files
- CPU.hdl, Memory.hdl, Computer.hdl: Part A, the Hack computer
- assembler.py: Part B, the Python assembler
- Box.asm, Box.hack: Part C, the box program (assembled with my own assembler)

## How to run the assembler
python assembler.py Box.asm
