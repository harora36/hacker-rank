import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static long calcCandies(int n, int[] arr) {
        // Complete this function
        long count = 0;
        long [] candies = new long[n];
        Arrays.fill(candies, 0);
        long [] left = new long[n];
        left[0] = 0;
        for (int i=1;i<n;i++) {
            if(arr[i] > arr[i-1]) {
                left[i] = left[i-1] + 1;
            }
        }
        long [] right = new long[n];
        right[n-1] = 0;
        for (int i=n-2;i>=0;i--) {
            if(arr[i] > arr[i+1]) {
                right[i] = right[i+1] + 1;
            }
        }
        for (int i=0;i<n;i++) {
            candies[i] = Math.max(left[i], right[i]) + 1;
        }
        
        for (int i =0; i<n;i++) {
            count += candies[i];
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for(int arr_i = 0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        long result = calcCandies(n, arr);
        System.out.println(result);
        in.close();
    }
}
