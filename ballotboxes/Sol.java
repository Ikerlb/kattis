import java.util.*;
import java.io.*;

public class Sol {

    public static void main(String[] args) {
        Kattio3 input = new Kattio3(System.in,System.out);
        for(int tc = 0; tc < 3; tc += 1) {
            int cities = input.getInt();
            int ballots = input.getInt();

            if(cities == -1 && ballots == -1) {
                break;
            }

            PriorityQueue<City> pq = new PriorityQueue<City>(cities); 
            for(int i = 0; i < cities; i += 1) {
                City c = new City(input.getInt());    
                pq.add(c);
            }
            ballots -= cities;
            for(int b = 0; b < ballots; b += 1) {
                City c = pq.poll();    
                c.addBallot();
                pq.add(c);
            }
            System.out.println(pq.peek().getRatio());
        }
    }
}

class City implements Comparable<City>{
    private int population;
    private int ballots;

    public City(int population) {
        this.population = population;
        this.ballots = 1;
    }

    public void addBallot() {
        this.ballots += 1;
    }

    public int getRatio() {
        int d = this.population / this.ballots;
        int m = this.population % this.ballots;
        if(m == 0) {
            return d;
        } else {
            return d + 1;
        }
    }

    @Override
    public int compareTo(City o) {
        int result = o.getRatio() - this.getRatio();
        return result;
    }     
}

class Kattio3 extends PrintWriter {
    public Kattio3(InputStream i, OutputStream o) {
        super(new BufferedOutputStream(o));
        r = new BufferedReader(new InputStreamReader(i));
    }

    public int getInt() {
        return Integer.parseInt(nextToken());
    }



    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
        if (token == null) {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    line = r.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                }
                token = st.nextToken();
            } catch (IOException e) { }
        }
        return token;
    }

    private String nextToken() {
        String ans = peekToken();
        token = null;
        return ans;
    }
}
