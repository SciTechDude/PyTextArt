
# PyTextArt

PyTextArt lets you generate different shapes given it's size and shape-type.
For now a bow-tie shape made of  any given characaters of  any given size can be created

More shapes will be added soon.

# bowTie Shape Generator

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