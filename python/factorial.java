package python;
import java.util.Scanner;
public class factorial {
    public static void main(String[] args) {
        System.out.println("Enter your number");
        int n;
        double fact = 1;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for(int i=1; i <=n;i++){
             fact = fact * i;
         System.out.println("i = " + i + ", fact = " + fact);
        }
        System.out.println(fact);
    }
}
