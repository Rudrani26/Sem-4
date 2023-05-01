.model small
.stack 100h

.data
string db 'madam', '$'
string1 db 'String is a Palindrome', '$'
string2 db 'String is not a Palindrome', '$'

.code
mov ax, @data
mov ds, ax

call palindrome
mov ah, 4ch
int 21h
endp

palindrome proc
mov SI, offset string

loop1:
mov ax, [SI]
cmp al, '$'
je label1
inc SI
jmp loop1

label1:
mov DI, offset string
dec SI

loop2:
cmp SI, DI
jl output1
mov ax, [SI]
mov bx, [DI]
cmp al, bl
jne output2
inc DI
dec SI
jmp loop2

output1:
lea dx, string1
mov ah, 09h
int 21h
ret

output2:
lea dx, string2
mov ah, 09h
int 21h
ret

palindrome endp
end
