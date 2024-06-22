<style type="text/css">
    table, tr, td {
        border: 0px;
    }
</style>
In a grid of 6 by 6 squares you want to place a skyscraper in each square with only some clues:
<ul>
    <li>The height of the skyscrapers is between 1 and 6</li>
    <li>No two skyscrapers in a row or column may have the same number of floors</li>
    <li>A clue is the number of skyscrapers that you can see in a row or column from the outside</li>
    <li>Higher skyscrapers block the view of lower skyscrapers located behind them</li>
</ul>
<br>
Can you write a program that can solve each 6 by 6 puzzle?
<br>
<br>
<b style="font-size:16px">Example:</b>
<br>
<br>
To understand how the puzzle works, this is an example of a row with 2 clues. Seen from the left there are 6 buildings visible while seen from the right side only 1:
<br>
<br>
<table style="width: 276px">
    <tr>
        <td style="text-align:center;height:16px;"> 6</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center;height:16px;"> 1</td>
    </tr>
</table>
<br>
There is only one way in which the skyscrapers can be placed. From left-to-right all six buildings must be visible and no building may hide behind another building:
<br>
<br>
<table style="width: 276px">
    <tr>
        <td style="text-align:center;height:16px;"> 6</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 1</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 5</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 6</td>
        <td style="text-align:center;height:16px;"> 1</td>
    </tr>
</table>
<br>
Example of a 6 by 6 puzzle with the solution:
<br>
<br>
<table style="width: 276px">
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;"> 6</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;"> 3</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center;height:16px;"> 4</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
</table>
<br>
<table style="width: 276px">
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 5</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 6</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 1</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 1</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 6</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 5</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 6</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 1</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 5</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 4</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 6</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 5</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 1</td>
        <td style="text-align:center; border: 0px;height:16px;"> 6</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 1</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 5</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 6</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 3</td>
        <td style="text-align:center; border: 0px;height:16px;"> 3</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 3</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 4</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 2</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 5</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 1</td>
        <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;"> 6</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
    <tr>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center;height:16px;"> 4</td>
        <td style="height:16px;">&nbsp;&nbsp;</td>
        <td style="text-align:center; border: 0px;height:16px;">&nbsp;&nbsp;</td>
    </tr>
</table>
<br>
<b style="font-size:16px">Task:</b>
<br>
<br>

<ul>
    <li>Finish:</li>
</ul>

```javascript
function solvePuzzle(clues)
```    
```csharp
public static int[][] SolvePuzzle(int[] clues)
```
```java
public static int[][] solvePuzzle(int[] clues)
```
```c
int **SolvePuzzle(int *clues);
```
```cpp
std::vector<std::vector<int>> SolvePuzzle(const std::vector<int> &clues);
```
```clojure
(defn solve-puzzle [clues])
```
```fsharp
solvePuzzle (clues : int[]) : int[][]
```
<ul>
    <li>
        Pass the clues in an array of 24 items. The clues are in the array around the clock. Index:
        <br>
        <table style="width: 276px">
            <tr>
                <td style="text-align:center; border: 0px;height:16px;">  </td>
                <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 0</td>
                <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 1</td>
                <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 2</td>
                <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 3</td>
                <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 4</td>
                <td style="text-align:center; border-bottom: solid 1px;height:16px;border-color:gray;"> 5</td>
                <td style="text-align:center; border: 0px;height:16px;">  </td>
            </tr>
            <tr>
                <td style="text-align:center; border: 0px;height:16px;"> 23</td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: 0px;height:16px;"> 6</td>
            </tr>
            <tr>
                <td style="text-align:center; border: 0px;height:16px;"> 22</td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: 0px;height:16px;"> 7</td>
            </tr>
            <tr>
                <td style="text-align:center; border: 0px;height:16px;"> 21</td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: 0px;height:16px;"> 8</td>
            </tr>
            <tr>
                <td style="text-align:center; border: 0px;height:16px;"> 20</td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: 0px;height:16px;"> 9</td>
            </tr>
            <tr>
                <td style="text-align:center; border: 0px;height:16px;"> 19</td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: 0px;height:16px;"> 10</td>
            </tr>
            <tr>
                <td style="text-align:center; border: 0px;height:16px;"> 18</td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: solid 1px;height:16px;border-color:gray;">  </td>
                <td style="text-align:center; border: 0px;height:16px;"> 11</td>
            </tr>
            <tr>
                <td style="text-align:center; border: 0px;height:16px;">  </td>
                <td style="text-align:center;'height:16px;'">17</td>
                <td style="text-align:center;height:16px;">16</td>
                <td style="text-align:center;height:16px;">15</td>
                <td style="text-align:center;height:16px;">14</td>
                <td style="text-align:center;height:16px;">13</td>
                <td style="text-align:center;height:16px;">12</td>
                <td style="text-align:center; border: 0px;height:16px;">  </td>
            </tr>
        </table>
    </li>
    <li>If no clue is available, add value `0`</li>
    <li>Each puzzle has only one possible solution</li>
    <li>`SolvePuzzle()` returns matrix `int[][]`. The first indexer is for the row, the second indexer for the column. Python returns a 6-tuple of 6-tuples, Ruby a 6-Array of 6-Arrays.</li>
</ul>