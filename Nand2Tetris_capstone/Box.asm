(LOOP)
    @KBD
    D=M
    @DRAW
    D;JNE
    @color
    M=0          // no key -> white
    @PAINT
    0;JMP
(DRAW)
    @color
    M=-1         // key -> black
(PAINT)
    @19296       // 16384 + 32*91
    D=A
    @addr
    M=D
    @20          // 20 rows
    D=A
    @rows
    M=D
(ROWLOOP)
    @4           // width = 4 words
    D=A
    @cols
    M=D
    @addr
    D=M
    @ptr
    M=D
(COLLOOP)
    @color
    D=M
    @ptr
    A=M
    M=D
    @ptr
    M=M+1
    @cols
    M=M-1
    D=M
    @COLLOOP
    D;JGT
    @32
    D=A
    @addr
    M=D+M
    @rows
    M=M-1
    D=M
    @ROWLOOP
    D;JGT
    @LOOP
    0;JMP