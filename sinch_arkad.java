import java.io.*;
import java.util.*;

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
        SolverClass sc = new SolverClass();
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
            System.out.println("Current total of matrix is " + getTotal(matrix));
            sc.solve(matrix, matrix.length);
            System.out.println("NEW total of matrix is " + getTotal(matrix));
        }
    }
    public static int getTotal(int[][] matrix){
        int total = 0;
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix.length; j++){
                total += matrix[i][j];
            }
        }
        return total;
    }

}

class SolverClass{
    private int[][] matrix;

    public void setup(int size, int m){
        matrix = new int[size][size];
    }

    
    public int[][] prefixsum2d(int[][] matrix){
        int[][] result = new int[matrix.length][matrix.length];
        for(int i = 0; i < matrix.length; i++){
            int total = 0;
            for(int j = 0; j < matrix.length; j++){
                total += matrix[i][j];
                result[i][j] = total + (i > 0 ? result[i-1][j]:0);
            }
        }
        return result;
    }
    
    public int query(int[][] cs2d, int a, int b, int A, int B){
        int result = 0;
        result += cs2d[A][B];
        result += a > 0 && b > 0 ? cs2d[a-1][b-1]:0;
        result -= a > 0 ? cs2d[a-1][B]:0;
        result -= b > 0 ? cs2d[A][b-1]:0;
        return result;
    }
    
    public class Candidate{
        public int query;
        public int i;
        public int j;
        public int d;
    
        public Candidate(int query, int i, int j, int d){
            this.query = query;
            this.i = i;
            this.j = j;
            this.d = d;
        }
    
    }
    
    public int[][] solve(int[][] matrix, int m){
        int n = m;
        for(int a = 0; a < 5; a++){
            int[][] cs2d = prefixsum2d(matrix);
            List<Candidate> candidates = new ArrayList<Candidate>();
            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++){
                    for(int d = 0; d < n; d++){
                        if(i+d == n || j+d == m) break;
                        int query = -query(cs2d, i, j, i+d, j+d);
                        candidates.add(new Candidate(query, i, j, d));
                    }
                }
            }
            Candidate best = null;
            for(Candidate c: candidates){
                if(best == null || c.query > best.query){
                    best = c;
                }
            }
            for(int i = best.i; i <= best.i+best.d; i++){
                for(int j = best.j; j <= best.j+best.d; j++){
                    matrix[i][j] *= -1;
                }
            }
        }
        return matrix;
    }

}

interface Solver {
    public void setup(int size, int m);
    public List<Square> solve(int[][] matrix, int m);
    public class Square {
        private int row, col, size;
        public Square(int row, int col, int size) {
            this.row = row;
            this.col = col;
            this.size = size;
        } 
    }
}