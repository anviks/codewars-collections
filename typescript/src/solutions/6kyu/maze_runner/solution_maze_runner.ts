/*
 * https://www.codewars.com/kata/58663693b359c4a6560001d6
 */

const moves = {
    N: [-1, 0],
    S: [1, 0],
    E: [0, 1],
    W: [0, -1]
};

export function mazeRunner(maze: number[][], directions: string[]): string {
    let currentLocation = [0, 0];

    outerLoop:
        for (let i = 0; i < maze.length; i++) {
            for (let j = 0; j < maze[i].length; j++) {
                if (maze[i][j] === 2) {
                    currentLocation = [i, j];
                    break outerLoop;
                }
            }
        }

    while (directions.length) {
        let instruction = directions.shift() as 'N' | 'S' | 'E' | 'W';
        currentLocation = [currentLocation[0] + moves[instruction][0], currentLocation[1] + moves[instruction][1]];

        if (
            currentLocation[0] < 0
            || currentLocation[0] >= maze.length
            || currentLocation[1] < 0
            || currentLocation[1] >= maze[0].length
        ) {
            return 'Dead';
        }

        let currentCell: number = maze[currentLocation[0]][currentLocation[1]];

        if (currentCell === 1) {
            return 'Dead';
        } else if (currentCell === 3) {
            return 'Finish';
        }
    }

    return 'Lost';
}
