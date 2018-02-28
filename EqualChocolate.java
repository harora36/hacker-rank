import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class EqualChocolate {

    static int equal(int[] arr, int min, int n) {
        int min_result = Integer.MAX_VALUE;
        for (int i = min; i >= min-2; i--) {
            int result = 0;
           for (int j = 0; j < n; j++) {
               int diff = (arr[j] - i);
               result += (arr[j] - i) /5;
               result += (arr[j] - i) % 5/2;
               result += (arr[j] - i) % 5 % 2 / 1;
           }
           min_result = Math.min(min_result, result); 
        }
        return min_result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int[] arr = new int[n];
            int min = Integer.MAX_VALUE;
            for(int arr_i = 0; arr_i < n; arr_i++){
                arr[arr_i] = in.nextInt();
                min = Math.min(min, arr[arr_i]);
            }
            int result = equal(arr, min, n);
            System.out.println(result);
        }
        in.close();
    }
}
