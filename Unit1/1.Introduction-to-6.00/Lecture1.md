------------
<h3 align="center">
Lecture 1: Introduction to 6.00                                                                                                                                           	 
</h3>
<p align="center">
<a href="http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-1-introduction-to-6.00/">MIT OpenCourseWare</a>
</p>
------------
####Declarative and Imperative Knowledge<br>
There are two main types of knowledge:  
 
**Declarative Knowledge** is composed of statements of fact.  
`y is the square root of x if and only if y * y = x`  
This says what it means to be a square root but it doesn't tell you how to find the square root.
It does tell you how to test if you have the answer to the square root.  
 
**Imperative Knowledge** tells you how to solve a problem, it is like a recipe.   
<code>1. Start with a guess, g</code><br>
<code>2. If g*g is close enough to x, then g is a good approximation of the square root of x</code><br>
<code>3. Otherwise, create a new guess by averaging g and x/g.</code><br>
<code>i.e. g<sub>new</sub> = (g<sub>old</sub>+x/g<sub>old</sub>)/2</code><br>
<code>4. Using this new guess, go back to step 2.</code><br>
 

_Example: Finding square root of 25_  
> **Iteration 1:**  
1. g = 3  
2. 3*3 = 9, not close enough to 25  
3. g<sub>new</sub> = (3+25/3)/2 = 5.66666..  
4. Try again with g = 5.67   
__Iteration 2:__  
1. g = 5.67  
2. 5.67*5.67 = 32.1489, not close enough to 25  
3. g<sub>new</sub> = (5.67+25/5.67)/2 = 5.0399  
4. Try again with g = 5.04   
**Iteration 3:**  
1. g = 5.04  
> 2. 5.04*5.04 = 25.4016, close enough to 25. <br>

* Once the program has found a solution it is said that the algorithm has _'converged'_ or halted.  
* A lot of computational techniques involve 'guess and check', this involves generating guesses and checking whether they are correct.   

####Algorithms<br>
An **algorithm** is a description of how to perform a computation. It contains:
* _Set of Instructions_
* _Flow of Control (order)_
* _Termination Condition_

**Set of Instructions:** these are the steps that can be executed.<br>
_In the example above the set of instructions is the 'recipe' of the program, the 4 steps._  
**Flow of Control:** this is the order in which the instructions are executed.<br>
_In the example above the flow of control is the order these steps are performed in, i.e 1, 2, 3, 4 repeat_  
**Termination Condition:** this tells the program when to stop. Without this the program will run to infinity.<br>
_In the example above the termination condition is that if g * g is 'close enough' to x the algorithm converges._  
 
####Fixed Program and Stored Program Computers<br>
One way to implement an algorithm would be to design a machine to perform the task. For example make a circuit that would specifically do square roots. This is the way that all computers used to work.<br>
 
**Fixed Program Computers** are machines designed to do very specific things. For example, during World War II, Alan Turing built a machine specifically designed to crack the Enigma Code. That is all the machine could do. These computers were very limited.  
 
**Stored Program Computers** were a big breakthrough in computation. The basic notion of a stored program computer is that the instructions are the same as the data. As there is no distinction between the program that implements the algorithm and the data on which the program operates, it is possible to change the program anytime you want. Machines became infinitely flexible as programs could produce programs because programs can produce data (as programs and data are the same thing).  
 
Stored Program Computers are what we use today and they are made up of: <br>
* _Memory_
* _Control Unit_
* _Arithmetic Logic Unit_
  - _Accumulator_
* _Input/Output Devices_

An **interpreter** is a program that can execute any legal set of instructions.
####Programming Language<br>
A **programming language** provides:  
* _a set of primitive instructions_
* _a set of primitive control structures._
 
So instructions and mechanisms for controlling the order in which they get executed. _And that's all._
 
What **distinguishes** one programming language from another is what these things are; 'What are your instructions?', 'What is your flow of control?', 'How do you combine them and what are the combining mechanisms?'   
More than anything it's the '_combining mechanisms_' that separate one language from another.  
 
**What defines a Programming Language?**  
* _Syntax_
* _Static Semantics_
* _Semantics_
 
**Syntax**: tells us which sequences of characters and symbols constitute a well-formed string. Well-formed does not necessarily mean meaningful. Something can be syntactically correct but may make no sense.  
**Static Semantics**: tells us which well-formed strings have meaning.  
**Semantics**: looks only at the strings that are both syntactically correct and static semantically correct. It assigns real meaning to them and removes ambiguity.  
 
####Types of Error<br>
When a program does not do what is expected it may:  
* _Crash_  
* _Infinately Loop_  
* _Incorrect Output_
 
**Crash**: when a program crashes it stops running and produces some indication that it has done so. This is the best type of error because it is obvious straight away that there is a problem with the code that needs to be fixed.  
**Infinite Loop**: sometimes a program will never stop. This can take some time to diagnose if you are unsure of how long the program is supposed to run. These errors are usually down to an error with the flow of control.  
**Incorrect Output**: these are the worst errors of all. They are often not immediately noticeable and can have devastating consequences. Ideally a program should be composed of strong static semantics to reduce the probability of it behaving unexpectedly.  
 
####Compiled vs Interpreted Language<br>
**Interpreted**: `source code -> checker -> interpreter -> output`  
* _Iterpreted Languages are easier to debug than compiled languages as the source code is interpreted and errors are described in the language of the source code (the code you wrote)._  
 
**Compiled**: `source code -> checker/compiler -> object code -> interpreter -> output`  
* _Compiled Languages first compile the code to object code. This code is closer to the language of the computer, the problem here is that the error messages are in terms of the object code and can be very obscure._   
* _The advantage of compiled code is that it is usually more efficient. They go through this extra step which means that they take less time to run._ 
