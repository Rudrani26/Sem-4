// ADDITION OF TWO 16-BIT BCD NUMBERS

.model small

.data
a dw 1234h
b dw 5678h

.code
mov ax, @data
mov ds, ax

mov ax, a
mov bx, b

add al, bl
daa
mov bl, al

adc ah, bh
mov al, ah
daa
mov bh, al

mov cl, 04h
mov ch, 04h

loop2:
rol bx, cl
mov dl, bl
and dl, 0fh
cmp dl, 09
jbe loop4
add dl, 07

loop4:
add dl, 30h
mov ah, 02
int 21h
dec ch
jnz loop2

mov ah, 4ch
int 21h
end
