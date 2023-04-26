import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;
import java.util.HashMap;
import java.lang.Comparable;
import java.util.stream.Collectors;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.BufferedOutputStream;
import java.lang.StringBuilder;

public class Solution {
    public static void main(String[] args) throws IOException {
        FastIO fio = new FastIO();

        TreeSet<Key> ordering = new TreeSet<>();
        HashMap<String, Key> injuryLevel = new HashMap<>();

        int numOfLines = fio.nextInt();
        StringBuilder stb = new StringBuilder();
        for(Integer i = 0; i < numOfLines; i += 1) {
            int command = fio.nextInt();
            if(command == 0) {
                String name = fio.next();
                Integer level = fio.nextInt();
                Key key = new Key(level, i, name); 
                ordering.add(key);
                injuryLevel.put(name, key);
            } else if (command == 1) {
                String name = fio.next();
                Integer levelDelta = fio.nextInt();
                Key prevKey = injuryLevel.get(name);
                Integer newLevel = prevKey.level + levelDelta;
                ordering.remove(prevKey);
                prevKey.level = newLevel;
                ordering.add(prevKey);
            } else if (command == 2) {
                String name = fio.next();
                Key key = injuryLevel.get(name);
                ordering.remove(key);
                injuryLevel.remove(name);
            } else {
                if(ordering.isEmpty()) {
                    stb.append("The clinic is empty\n");
                } else {
                    Key last = ordering.last();
                    stb.append(last.name + "\n");
                }
            }
        }
        System.out.print(stb.toString());
    }
}

class FastIO extends PrintWriter { 
    BufferedReader br; 
    StringTokenizer st;

    public FastIO() 
    { 
        super(new BufferedOutputStream(System.out)); 
        br = new BufferedReader(new
                InputStreamReader(System.in));
    } 

    String next() 
    { 
        while (st == null || !st.hasMoreElements()) { 
            try { 
                st = new StringTokenizer(br.readLine()); 
            } catch (IOException  e) { 
                e.printStackTrace(); 
            } 
        } 
        return st.nextToken(); 
    } 

    int nextInt() { 
        return Integer.parseInt(next()); 
    } 

    long nextLong() { 
        return Long.parseLong(next()); 
    } 

    double nextDouble() { 
        return Double.parseDouble(next()); 
    } 

    String nextLine() { 
        String str = ""; 
        try { 
            str = br.readLine(); 
        } catch (IOException e) { 
            e.printStackTrace(); 
        } 
        return str; 
    } 
}

class Key implements Comparable<Key> {
 
    public Integer level;
    Integer entered;
    String name;
 
    public Key(Integer level, Integer entered, String name) {
        this.level = level;
        this.entered = entered;
        this.name = name;
    }

    public String toString() {
        return this.level + " " + this.entered + " " + this.name;
    }
 
    public int compareTo(Key k) {
        if(this.name.equals(k.name)){
            return 0;
        }
        if(this.level == k.level) {
            return k.entered.compareTo(this.entered);
        }
        return this.level.compareTo(k.level);
    }
}


