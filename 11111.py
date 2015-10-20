with n :
 
: num?  \ n f --   ) 
	if drop else . then ;
 
\ is m mod n 0? leave the result twice on the stack
: div? \ m n -- f f
	mod 0 = dup ;
 
: fizz? \ n -- n f
	dup 3 
	div? if "Fizz" .  then ;
 
: buzz? \ n f -- n f
	over 5 
	div? if "Buzz" .  then or ;
 
\ print a message as appropriate for the given number:
: fizzbuzz  \ n --
	fizz? buzz? num? 
	space ;
 
\ iterate from 1 to 100:
' fizzbuzz 1 100 loop 
cr bye
 