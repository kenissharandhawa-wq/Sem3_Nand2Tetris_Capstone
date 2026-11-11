import sys

COMP = {'0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000',
 '!D':'0001101','!A':'0110001','-D':'0001111','-A':'0110011','D+1':'0011111',
 'A+1':'0110111','D-1':'0001110','A-1':'0110010','D+A':'0000010','D-A':'0010011',
 'A-D':'0000111','D&A':'0000000','D|A':'0010101','M':'1110000','!M':'1110001',
 '-M':'1110011','M+1':'1110111','M-1':'1110010','D+M':'1000010','D-M':'1010011',
 'M-D':'1000111','D&M':'1000000','D|M':'1010101'}
DEST = {'':'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
JUMP = {'':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}

symbols = {f'R{i}': i for i in range(16)}
symbols.update({'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576})
next_var = 16

def clean(line):
    return line.split('//')[0].replace(' ', '').replace('\t', '').strip()

def translate(l):
    
    global next_var
    if l.startswith('@'):
        s = l[1:]
        if s == '':
            raise ValueError
        if s.isdigit():
            val = int(s)
            if val > 32767:
                raise ValueError
        else:
            if s[0].isdigit():          
                raise ValueError
            if s not in symbols:
                symbols[s] = next_var
                next_var += 1
            val = symbols[s]
        return format(val, '016b')
    dest, comp, jump = '', l, ''
    if '=' in comp:
        dest, comp = comp.split('=', 1)
    if ';' in comp:
        comp, jump = comp.split(';', 1)
    
    if not set(dest) <= set('AMD') or len(set(dest)) != len(dest):
        raise ValueError
    d = ''.join(c for c in 'AMD' if c in dest)
    return '111' + COMP[comp] + DEST[d] + JUMP[jump]

def assemble(path):
    lines = [(n, clean(l)) for n, l in enumerate(open(path), 1)]
    lines = [(n, l) for n, l in lines if l]

    errors = 0
   
    code, pc = [], 0
    for n, l in lines:
        if l.startswith('('):
            if not l.endswith(')') or len(l) < 3:
                print(f'Line {n}: invalid instruction')
                errors += 1
                continue
            symbols[l[1:-1]] = pc
        else:
            code.append((n, l)); pc += 1

    
    out = []
    for n, l in code:
        try:
            out.append(translate(l))
        except (ValueError, KeyError):
            print(f'Line {n}: invalid instruction')
            errors += 1
    return out, errors

if __name__ == '__main__':
    asm = sys.argv[1]
    result, errors = assemble(asm)
    if errors:
        print(f'{errors} error(s) found. No .hack file written.')
    else:
        open(asm.replace('.asm', '.hack'), 'w').write('\n'.join(result) + '\n')
        print('Done:', asm.replace('.asm', '.hack'))