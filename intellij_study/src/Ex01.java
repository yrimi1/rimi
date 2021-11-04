import aa.bb.cc.AA;

// consolas d2conding
public class Ex01 {
    public static void main(String[] args) {
        System.out.println("긴데 직접 적어야 되네요..");
        System.out.println("아님 so쓰고 아래것 선택.");
        AA a1 = new AA();
        a1.doA();
        a1.doA(10);     // a: 이거 자동으로 적힙니다...
        a1.doA(11.11);
    }
}
