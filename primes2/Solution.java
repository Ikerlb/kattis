import java.math.BigInteger;
import java.util.Scanner;

public class Solution {
    public static BigInteger[] convert(String s, int[] bases) {
        BigInteger[] res = new BigInteger[bases.length];
        for(int i = 0; i < bases.length; i += 1) {
            try {
                BigInteger bi = new BigInteger(s, bases[i]);
                res[i] = bi;
            } catch(Exception e) {
                res[i] = null;
                continue;
            }
        }
        return res;
    }

    public static int gcd(int a, int b) {
        if(b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    public static String lowestTerms(int a, int b) {
        int d = gcd(a, b);
        return (a / d) + "/" + (b / d);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        int tcs = sc.nextInt();

        for(int tc = 0; tc < tcs; tc += 1) {
            String s = sc.next();
            int[] bases = {2, 8, 10, 16};

            BigInteger[] conv = convert(s, bases);
            int n = 0;
            int p = 0;    
            for(BigInteger c : conv) {
                if(c != null) {
                    n += 1;
                    if(c.isProbablePrime(10))
                        p += 1;
                }
            }
            System.out.println(lowestTerms(p, n));
        }
    }
}
