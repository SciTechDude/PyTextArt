# bowTieShapeGenerator

BowTieShapeGenerator lets you generate a bow-tie shape made of  anyu given characaters of  any given size.
You need to specify size at command line.

For example:

`BowTie(size=10, fill_value = '*', empty_value = ' ').print_shape()`

Result:

<pre>

*                                   *
  *                               *  
*   *                           *   *
  *   *                       *   *  
*   *   *                   *   *   *
  *   *   *               *   *   *  
*   *   *   *           *   *   *   *
  *   *   *   *       *   *   *   *  
*   *   *   *   *   *   *   *   *   *
  *   *   *   *   *   *   *   *   *  
*   *   *   *   *   *   *   *   *   *
  *   *   *   *       *   *   *   *  
*   *   *   *           *   *   *   *
 *   *   *               *   *   *  
*   *   *                   *   *   *
  *   *                       *   *  
*   *                           *   *
  *                               *  
*                                   *

</pre>

Another example:

`BowTie(size=5, fill_value = '?', empty_value = ' ').print_shape()`

<pre> 
?               ?
  ?           ?  
?   ?       ?   ?
  ?   ?   ?   ?  
?   ?   ?   ?   ?
  ?   ?   ?   ?  
?   ?       ?   ?
  ?           ?  
?               ?
</pre>