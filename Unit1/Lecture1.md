------------
<h3 align="center">
Lecture 1: Introduction to 6.00                                                                                                                                                
</h3>
<p align="center">
<a href="http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-1-introduction-to-6.00/">MIT OpenCourseWare</a>
</p>
------------
####Declarative and Imperative Knowledge.<br>
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
