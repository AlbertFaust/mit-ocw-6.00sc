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
  
**Imperitive Knowledge** tells you how to solve a problem, it is like a recipe.   
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
  
####Fixed Program and Stored Program computers<br>
