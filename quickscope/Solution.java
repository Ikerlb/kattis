import java.util.Stack;
import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.StringTokenizer;
import java.util.HashMap;

class Solution {
    public static String getFromContext(Stack<HashMap<String, String>> s, String iden) {
        for(int i = s.size() - 1; i >= 0; i -= 1) {
            HashMap<String, String> hm = s.get(i);
            if(hm.get(iden) != null) {
                return hm.get(iden);
            }
        }
        return null;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
  
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        Stack<HashMap<String, String>> context = new Stack<>();
        context.push(new HashMap<String, String>());

        for(int i = 0; i < n; i += 1) {
            st = new StringTokenizer(br.readLine());
            String ft = st.nextToken();
            //System.out.println(ft);
            if(ft.equals("{"))
                context.push(new HashMap<String, String>());
            else if(ft.equals("}"))
                context.pop();
            else if(ft.equals("DECLARE")) {
                String iden = st.nextToken();
                String type = st.nextToken();
                HashMap<String, String> lastScope = context.peek();
                String e = lastScope.get(iden); 
                if(e == null) {
                    lastScope.put(iden, type);
                } else {
                    System.out.println("MULTIPLE DECLARATION");
                    break;
                }
            } else if(ft.equals("TYPEOF")) {
                String iden = st.nextToken();
                String s = getFromContext(context, iden);
                if(s == null) {
                    System.out.println("UNDECLARED");
                } else {
                    System.out.println(s);
                }
            }
        }
    }
}
