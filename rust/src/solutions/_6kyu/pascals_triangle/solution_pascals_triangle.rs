/*
 * https://www.codewars.com/kata/5226eb40316b56c8d500030f
 */

pub fn pascals_triangle(n: usize) -> Vec<usize> {
    let mut triangle: Vec<Vec<usize>> = vec![];

    for i in 0..n {
        let mut row = vec![1; i + 1];

        for j in 1..i {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }

        triangle.push(row);
    }

    triangle.into_iter().flatten().collect()
}
