Draft black-box test cases for method <code>triangle_type</code>. This method will return following values for different arguments <kbd>a</kbd>, <kbd>b</kbd>, <kbd>c</kbd>:

*   regular triangle.
*   isosceles triangle.
*   normal triangle.
*   degenerate triangle (e.g. a + b == c).
*   not a triangle (e.g. a + b < c).

What's more, the method will raise exception under following situations:

*   zero input (one or more numbers are 0).
*   negative input (one or more numbers are negative).

Please handin your test cases in given text box. The test cases should be represented in CSV, and should contain CSV header <code>a,b,c</code>, for example:

```csv
a,b,c
1,2,3
1,3,3
```

Please upload your handin before deadline.

# Correct answer

```csv
a,b,c
5,5,5
4,4,5
4,5,4
5,4,4
3,4,5
9,4,4
4,9,4
4,4,9
8,4,4
4,8,4
4,4,8
0,4,5
4,0,5
4,5,0
0,0,0
-3,4,5
3,-4,5
3,4,-5
-3,-4,-5
```