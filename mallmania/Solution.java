import java.util.ArrayDeque;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.util.HashSet;
import java.lang.Object;
import java.util.Objects;

public class Solution {
    static class Reader{
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader(){
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException{
            din = new DataInputStream(
                new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String readLine() throws IOException{
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    if (cnt != 0)
                        break;
                    else
                        continue;
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
        }

        public int nextInt() throws IOException{
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException{
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException{
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }

        public void close() throws IOException{
            if (din == null)
                return;
            din.close();
        }
    }

    public static int solve(ArrayDeque<Point> q, HashSet<Point> visited, HashSet<Point> m1) {
        int res = 0;
        while(q.size() > 0) {
            int sz = q.size();
            for(int i = 0; i < sz; i += 1) {
                Point p = q.poll();
                if(m1.contains(p)) {
                    return res;
                }
                for(Point pp : p.neighbors()) {
                    if(pp.inBounds() && !visited.contains(pp)) {
                        visited.add(pp);
                        q.add(pp);
                    }
                }
            }
            res += 1;
        }
        return -1;
    }

    public static void clean(boolean[][] grid) {
        for(int r = 0; r < grid.length; r += 1)
            for(int c = 0; c < grid[0].length; c += 1)
                grid[r][c] = false;
    }

    public static void main(String[] args) throws IOException {
        Reader fr = new Reader();
        while(true) {
            int p1 = fr.nextInt();
            if(p1 == 0) {
                break;
            }
            int prev = 0;
            HashSet<Point> m1 = new HashSet<>();
            for(int i = 0; i < p1; i += 1) {
                Point p = new Point(fr.nextInt(), fr.nextInt());
                m1.add(p);
            }
            int p2 = fr.nextInt();
            HashSet<Point> visited = new HashSet<>();
            ArrayDeque<Point> q = new ArrayDeque<Point>();
            for(int i = 0; i < p2; i += 1) {
                Point p = new Point(fr.nextInt(), fr.nextInt());
                q.add(p);
                visited.add(p);
            }

            System.out.println(solve(q, visited, m1));
        }
    }

}

class Point {
    public int x;
    public int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y; 
    }

    public Point[] neighbors() {
         return new Point[]{
             new Point(x + 1, y),
             new Point(x, y + 1),
             new Point(x - 1, y),
             new Point(x, y - 1)
         };
    }

    @Override
    public boolean equals(Object other) 
    {
        if (this == other)
          return true;

        if (!(other instanceof Point))
          return false;

        Point otherPoint = (Point) other;
        return otherPoint.x == x && otherPoint.y == y;
    }


    @Override
    public int hashCode() {
        int result = x;
        result = 31 * result + y;
        return result;
    }

    public boolean inBounds() {
        if(x < 0 || x > 2000) 
            return false;
        if(y < 0 || y > 2000)
            return false;
        return true;
    }
}

