Given a 2D array and a number of generations, compute n timesteps of [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

The rules of the game are:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it (i.e. [Moore Neighborhood](https://en.wikipedia.org/wiki/Moore_neighborhood)). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return `[[]]`.)

For illustration purposes, 0 and 1 will be represented as `░░` and `▓▓` blocks respectively (PHP: plain black and white squares). You can take advantage of the `htmlize` function to get a text representation of the universe, e.g.:

```javascript
console.log(htmlize(cells));
````
```coffeescript
console.log htmlize(cells)
````
```python
print(htmlize(cells))
````
```haskell
trace (htmlize cells)
```
```java
System.out.println(LifeDebug.htmlize(cells));
```
```swift
print(htmlize(cells))
```
```php
echo htmlize($cells) . "\r\n";
```
```c
char *universe = htmlize(cells, rows, columns);
printf("%s", universe);
free(universe);
```
```csharp
Console.WriteLine(ConwayLife.Htmlize(cells));
```

~~~if:c
In **C**, the initial dimensions of the GoL universe are passed to your function *by reference* via the pointers `rowptr` and `colptr`. You have to update these two variables to report the dimensions of the universe you are returning.
~~~