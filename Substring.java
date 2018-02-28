import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Substring {

    static long substrings(String balls) {
        int length = balls.length();
        long sum = 0;
        long f = 1;
        for (int i= length-1; i >= 0; i--) {
            sum = (sum + (balls.charAt(i) -'0')*f*(i+1)) % (long)(Math.pow(10,9) + 7);
            f = (f*10 + 1) % (long)(Math.pow(10,9) + 7)    ;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String balls = in.next();
        long result = substrings(balls);
        System.out.println(result);
        in.close();
    }
}
