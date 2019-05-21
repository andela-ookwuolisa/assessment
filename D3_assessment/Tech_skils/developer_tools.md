# Developer tools

### Expectation
The Developer is able to demonstrate and use more complex commands on both local and remote systems (eg. xargs, expr, usage of sed and awk).

### Justification
The xargs command is used for building an execution pipeline from standard input. Using xargs allows tools like echo and rm and mkdir to accept standard input as arguments.

```
>>> echo 'project venv settings' | xargs mkdir
ls
project venv settings
```
The expr is used for evaluating integer or string expressions.

```
>>> expr 4 '*' 2 
8
```
The awk command is a powerful method for processing or analyzing text files — in particular, data files that are organized by lines (rows) and columns.

```
>>> echo '1, Python tutorial, $50, 2 months
2, Machine Learning, $40, 2 months
3, Data analysis, 40$, 2 month
4, Javascipt basic, $20, 1 month' > course.txt

>>> awk -F, '{ print $2 }' course.txt > output.txt
>>> cat output.txt
 Python tutorial 2 months
 Machine Learning 3 months
 Data analysis 1 month
 Javascipt basic 1 month
 ```

 The sed (stream editor) command is used to modify each line of a file or stream by replacing specified parts of the line. It makes basic text changes to a file or input from a pipeline.


 ```
 >>> sed 's/40/45/' course.txt > course2.txt
>>> cat course2.txt
1, Python tutorial, $50, 2 months
2, Machine Learning, $45, 2 months
3, Data analysis, 45$, 2 month
4, Javascipt basic, $20, 1 month
```
