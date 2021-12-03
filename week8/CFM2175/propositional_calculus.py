'''Lets look at the Lecture example.
“If the network operates abnormally but there is no technical support, then system files will be damaged”
Identify the connectives
Identify the propositions

Add the brackets if required, to group propositions that belong to the if, separate from those that belong to the then

N = the network operates normally
T = there is technical support
D = system files will be damaged

If
the network operates abnormally	 ¬N
but				^
there is no technical support	 ¬T
then				->
the system files will be damaged	D

(¬N ^ ¬S) -> D
(not n and not t) -> D'''


n = True
t = True
d = True

if not n and not t:
    d = True

