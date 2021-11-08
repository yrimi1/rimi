

public class Ex02 {
    public static void main(String[] args) {

        // 문자열 비교 연산자는 equals 함수를 사용한다.
        String str1 = "simple String";
        String str2 = "simple String";

        String str3 = new String("simple String");
        String str4 = new String("simple String");
        
        if (str1. equals(str2))      // (str1==str2)
            System.out.println("str1 ste2 동일한 인스터스 참조 ");
        else
            System.out.println("str1 ste2 다른 인스터스 참조 ");
        if(str3.equals(str4))
            System.out.println("str3 ste4 동일한 인스터스 참조 ");
        else
            System.out.println("str3 ste4 다른 인스터스 참조 ");

    }
}
