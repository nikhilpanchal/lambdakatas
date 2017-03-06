# Functional Notes

Notes that I've accumulated as I've gone through functional programming stuff

### Principles

 - In a restrictive sense, functional programming is programming without mutation and mutable variables, assignments,
 loops and other imperative control structures
 - In a wider sense, functional programming enables the construction of elegant programs that focus on functions: 
 where functions are values that are produced, consumed and composed.
 - In a functional programming language, functions are first class citizens.
 
#### Substitution model

Functional programming works by evaluating `expressions` with the substitution model: Where expressions are evaluated 
 to and substituted by a value. In other words, the underlying idea is to reduce an expression to a value and do that
 recursively to evaluate higher expressions composed of smaller expressions. So you can have expressions that are composed of smaller expressions and you evaluate it by reducing 
 the smaller expressions to their values, substitute those values into the higher expressions, evaluate the higher expressions 
 to their values and so on (very similar to what you would do in evaluating algebraic evaluations).
 
 It's important to note that the substitution model can only be applied to expressions that have no `side effects`.
 Since side-effects cannot be expressed by the substitution model, one of the motivations to rule out side effects in
 functional programming is so we can keep to the simple substitution model to evaluate expressions.
 
 
 
### Benefits
 
 - Simpler reasoning principles
 - Better modularity
 - Good for exploiting parallelism for multi-core and cloud computing
 
 Video Available: [Working Hard to keep it simple](https://www.youtube.com/watch?v=3jg1AheF4n0)
 
 Resource: [Elements of Programming](https://www.coursera.org/learn/progfun1/lecture/vzbJj/lecture-1-2-elements-of-programming)


### Tail Recursion
Functional programming languages have tail recursion optimization available for recursive programs.

This states that when the last statement in a function is a call to a function (could be to itself or another function),
then the current execution stackframe can be re-used for the execution of that function call.
This way the overall function will execute with constant stack frame size and will operate like any iterative function.

In order to make a function tail recursive, set the calculated value to be one of the function arguments instead of the
return value. That way you are not waiting for the recursive function call stack to unravel after hitting the terminating
condition to calculate the overall result. Instead, the calculation is done with each call to the recursive step so
there is no need to create a new stack-frame.

Here is an illustration.

The code snippet below is linear recursive. Notice how it needs the return value of each call to sum_linear to be added
to f(a). That will require each call to sum_linear to be in its own stack-frame.

```python
def sum_linear(f, a, b):
    if a >= b:
        return 0

    return f(a) + sum_linear(f, (a+1), b)
```

Now look at the snippet below. 

```python
def sum_tail_recursive(f, a, b):
    def loop(accumulator, a):
        if a >= b:
            return accumulator

        return loop(f(a) + accumulator, (a+1))

    return loop(0, a)
```

This is tail recursive. Notice how the result is calculated before each call to loop and is passed as a param to the next
call to loop. This way the next call to loop does not need to operate in its own scope and can re-use the scope of the
previous call. Thus there is no need for a new stack-frame.