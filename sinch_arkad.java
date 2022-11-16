// Read lines from stdin
import java.io.*;
import java.util.*;

// Read all lines from stdin into an array
public class sinch_arkad {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        List<String> lines = new ArrayList<String>();
        while ((line = br.readLine()) != null) {
            lines.add(line);
        }
        br.close();
        int i = 0;
        while(i < lines.size()){
            line = lines.get(i);
            String[] split = line.split(" ");
            int[][] matrix = new int[split.length][split.length];
            int k = 0;
            while(i < lines.size() && !lines.get(i).equals("")){
                split = lines.get(i).split(" ");
                for(int j = 0; j < split.length; j++){
                    matrix[k][j] = Integer.parseInt(split[j]);
                }
                i++;
                k++;
            }
            i++;
            solve(matrix);
        }
    }

    public static void solve(int[][] matrix){
        int n = matrix.length;
        int m = matrix[0].length;
        
    }
}