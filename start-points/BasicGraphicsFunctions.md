Basic Computer Graphic Functions
================================
When doing computer graphics, there are some common functions that keeps popping up:

   - **wrap**. Wrap a value around edges of some interval, e.g the edges of screen. So if the screen is 800 pixels wide, and a character in PacMan is at x=810, wrapping that value would place the character at 10, and if x=-5 wrapping would result in x=795.
   - **crop**. Clip a value so it stays inside some interval, e.g the edges of screen. Typical example is playing with colors, adding them together for some explosion effect or other visuals. Then you want the R,G,B values to stay within e.g 0-255. Cropping here means that a component of value 260 would be "cropped" to 255, and a value of -50 would be cropped to 0.
   - **lerp**. Short for Linear Interpolation. Interpolates a value between some end-points (or beyond), e.g to animate a simple movement. So an animated lever from y=50 to y=150 over 10 seconds, a movement of 50 pixels, would at time=0 result in value 50, and at time=10 y=150. At the mid-time, it would be y=100.
 
 Each of these can be written using functions that take values and return new values; this make them unusually well-suited for unit test.
 
 All of the functions are often useful to extend to several dimensions, not only scalars. E.g 2D and 3D vectors would also benefit from having wrap, crop and lerp functionality, so this excercise could be extended to refactor for several dimensions.
