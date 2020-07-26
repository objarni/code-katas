Basic Computer Graphic Functions
================================
An excercise in API design.

When doing computer graphics, there are some common functions that keeps popping up:

   - lerp. Short for Linear Interpolation. Interpolate a value between some end-points, e.g to animate a simple movement.
   - wrap. Wrap a value around edges of some interval, e.g the edges of screen.
   - crop. Clip a value so it stays inside some interval, e.g the edges of screen.
 
 Each of these can be written using functions that take values and return new values; this make them unusually well-suited for unit test.
 
 Use TDD to design a good interface, meaning that it reading code using lerp, wrap and crop is "grokkable" in the calling code.
 
 
