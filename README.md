
#PyTextArt

PyTextArt lets you generate different shapes given it's size and shape-type.
For now a bow-tie shape made of  any given characaters of  any given size can be created.

Option for hollow shape is possible using `hollow` attribute. In this case code ignores `fill_value`

#bowTie Shape Generator

For example:

`BowTie(size=7, fill_value = '#', empty_value = ' ', hollow = False).print_shape()`

Result:

<pre>

#           #
 #         # 
# #       # #
 # #     # # 
# # #   # # #
 # # # # # # 
# # # # # # #
 # # # # # # 
# # #   # # #
 # #     # # 
# #       # #
 #         # 
#           #
</pre>

Another example:

`BowTie(size=5, fill_value = '*', empty_value = '.', hollow = False).print_shape()`

<pre> 
*.......*
.*.....*.
*.*...*.*
.*.*.*.*.
*.*.*.*.*
.*.*.*.*.
*.*...*.*
.*.....*.
*.......*
</pre>

One more example:
`BowTie(size=10, fill_value = '+', empty_value = '.', hollow = True).print_shape()`

<pre>
+                 +
++               ++
+ +             + +
+  +           +  +
+   +         +   +
+    +       +    +
+     +     +     +
+      +   +      +
+       + +       +
+        +        +
+       + +       +
+      +   +      +
+     +     +     +
+    +       +    +
+   +         +   +
+  +           +  +
+ +             + +
++               ++
+                 +
</pre>