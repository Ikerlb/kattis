import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.LinkedList;

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

    public static void main(String[] args) throws IOException {
        Reader fr = new Reader();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = fr.nextInt();
        int m = fr.nextInt();

        HashMap<Integer, ArrayList<Integer>> hm = new HashMap<>();
        HashMap<Integer, Integer> indegree = new HashMap<>();

        for(int i = 0; i < m; i += 1) {
            int a = fr.nextInt() - 1;
            int b = fr.nextInt() - 1;
            if(hm.get(a) == null)
                hm.put(a, new ArrayList<Integer>()); 
            hm.get(a).add(b);
            if(indegree.get(b) == null)
                indegree.put(b, 0);
            indegree.put(b, indegree.get(b) + 1);
        }


        LinkedList<Integer> q = new LinkedList<>();

        for(int i = 0; i < n; i += 1) {
            if(indegree.get(i) == null || indegree.get(i) == 0)
                q.add(i);
        }

        //System.out.println(hm); 
        //System.out.println(indegree); 
        //System.out.println(q);

        ArrayList<String> res = new ArrayList<String>(); 

        while(q.size() > 0) {
            int node = q.pollFirst();    
            res.add(Integer.toString(node + 1));
            if(hm.get(node) != null)
                for(int nn : hm.get(node)) {
                    int id = indegree.get(nn);
                    indegree.put(nn, id - 1);
                    if(id == 1)
                        q.add(nn);
                }
        }

        if(res.size() != n) {
            bw.write("IMPOSSIBLE\n"); 
        } else {
            for(int i = 0; i < n; i += 1){
                bw.write(res.get(i) + "\n");        
            }
        }
        bw.flush();
    }
}
