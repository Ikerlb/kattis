import java.util.Scanner;
import java.util.LinkedList;
import java.util.StringJoiner;

public class Solution {
    public static String format(char[][] grid) {
        StringJoiner res = new StringJoiner("\n");
        for(int r = 0; r < grid.length; r += 1) {
            StringJoiner row = new StringJoiner("");
            for(int c = 0; c < grid[r].length; c += 1)
                row.add(String.valueOf(grid[r][c]));
            res.add(row.toString());
        }
        return res.toString();
    }

    public static int solve(char[][] grid, LinkedList<Point> s, LinkedList<Point> fires) {
        int turns = 0;
        //System.out.println(turns + "\n" + format(grid) + "\n");
        while(!s.isEmpty()) {
            int lim = s.size();
            for(int ns = 0; ns < lim; ns += 1) {
                Point n = s.poll();
                if(grid[n.r][n.c] == '*')
                    continue;
                for(Point nn : n.neighbors()) {
                    if(!nn.inBounds(grid.length - 1, grid[0].length - 1)){
                        return turns + 1;
                    } else if(grid[nn.r][nn.c] == '.') {
                        grid[nn.r][nn.c] = '@';
                        s.add(nn);
                    }
                }
            }
            lim = fires.size();
            for(int nf = 0; nf < lim; nf += 1) {
                Point n = fires.poll();
                for(Point nn: n.neighbors()) {
                    if(!nn.inBounds(grid.length - 1, grid[0].length - 1)){
                        continue;
                    } else if(grid[nn.r][nn.c] != '#' && grid[nn.r][nn.c] != '*') {
                        grid[nn.r][nn.c] = '*';
                        fires.add(nn);
                    }
                }
            }
            turns += 1;
            //System.out.println(turns + "\n" + format(grid) + "\n");
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int tcs = sc.nextInt();
        for(int tc = 0; tc < tcs; tc += 1) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            char[][] grid = new char[n][m];
            LinkedList<Point> fires = new LinkedList<Point>();
            LinkedList<Point> start = new LinkedList<Point>();
            for(int r = 0; r < n; r += 1) {
                String line = sc.next();
                for(int c = 0; c < m; c += 1) {
                    grid[r][c] = line.charAt(c);
                    if(grid[r][c] == '*') 
                        fires.add(new Point(r, c)); 
                    else if(grid[r][c] == '@')
                        start.add(new Point(r, c)); 
                }
            }
            int res = solve(grid, start, fires);
            if(res == 0)
                System.out.println("IMPOSSIBLE");
            else
                System.out.println(res);
        }
        
    }
}

class Point {
    public int r;
    public int c;
 
    public Point(int r, int c) {
        this.r = r;    
        this.c = c;
    }

    public boolean inBounds(int n, int m) {
        if(r < 0 || r > n)
            return false;
        if(c < 0 || c > m)
            return false;
        return true;
    }

    public Point[] neighbors() {
         return new Point[]{
             new Point(r + 1, c),
             new Point(r, c + 1),
             new Point(r - 1, c),
             new Point(r, c - 1)
         };
    }
}
