Polygon Splitting
=================

In 2D CAD-software, a lot of tools are about modifying polygons in different ways - adding segments, joining polygons, cleaning them up etc.

One specific algorithm is about splitting a polygon up into several polygons, at certain points.

In general, polygons can be made up of both straight line segments, circular arcs and even more advanced geometry like bezier splines. However, for this kata, that complexity can be ignored; just think of polygons as made up of straight lines from point A to point B to point C and so on.

The input to the algorithm is a polygon and a set of points, and the output is a set of polygons.

For example, given a single-line polygon from (0, 0) to (50, 0), and a "split point" at (25, 0), the algorithm would output two polygons:

   a polygon from point (0, 0) to point (25, 0)
   a polygon from point (25, 0) (50, 0)

The difficulty with these numerical-geometrical algorithms is thinking about how to verify the algorithms behaviour with all the "fuzzyness" involved here:

 - round-off errors from floating point arithmetic (how close is close enough for a point to "split" the polygon?)
 - what to do if input point is on end point or start point of polygon?
 - what if several points are very close to each other?

