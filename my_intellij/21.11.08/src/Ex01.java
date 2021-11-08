import com.sun.org.apache.xpath.internal.operations.String;

import java.util.Scanner;

public class Ex01 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(system.in);
        System.out.print("이름을 성과 이름을 띄워서 ");
        String inputString = scan.nextLine();
        System.out.println("inpputString = "+ inputString);
        String ar[]=inputString.split("");
        for (String a : ar){
            System.out.println("a="+a);
        }
//        int blinkNumber = inputString.charAt(' ');
    }

}


//자바의 print dhk println 의 차이
//