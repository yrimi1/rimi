import java.util.Scanner;

//래퍼런스 = 베리어블 = 참조변수
// alt + enter : 빠른 에러 처리
public class MonthSchedule {
    public static void main(String[] args) {
        Day days[] = new Day[30];
        Scanner sc = new Scanner(System.in);
        //데이라는 객체를 만들고 배열 만듦 0부터 29까지만듦
        //각 칸마다 하나의 객체가 들어있음  각각 변수work 함수 get ,set,show들어있음
        //객체는 값을 초기화하지않으면 nell이 들어간다.
        //칸을 만들었을뿐 처음에는 null만 들어있음
        int index = 0;
        //영번째 배열을 가리킴
        while (true) {
            System.out.println("이번달 스케쥴 관리 프로그램");
            System.out.println("할일(입력:1, 보기:2, 끝내기:3)");
//        days[0] = new Day();
//        days[1] = new Day();
//        // 생성자 호출 은 이런식으로 한다.
//        // 그러고 나면 0번배열에 work, get ,set,show 가 들어간다.
//        // 하지면 현재 0번과 1번 배열에만 들어갔을뿐이다.
//        // 2는 여전이 null값 들어있음
//
//        System.out.println("day[0]"+days[0].toString());//투스트링 생략가능
//        System.out.println("day[1]"+days[1]);
//        System.out.println("day[2]"+days[2]);// 여기는 널이라서 null.에러가 뜬다.
            int so1 = sc.nextInt();

            System.out.println("so1" + so1);
            if (so1 == 1) {
                System.out.println("날짜(1~30?)");
                int so2 = sc.nextInt();// so2가 1 이면 인덱스 0
                // so2가 30 이면 인덱스 29
                sc.nextLine();  // 입력버퍼에 ... enter키 삭제...
                days[so2 - 1] = new Day(); // 인덱스 so2번째에 객체 생성
                System.out.println("할일(빈칸없이입력)?");
                String so3 = sc.nextLine(); //넥스트라인은 문자입력받는곳
                days[so2 - 1].setWork(so3);
                System.out.println("입력이 정상적으로되었습니다.");
            }
            else if (so1 == 2) {
                for (int i = 0; i < 30; i++) {
                    if (days[i] != null){
                        System.out.println(i + "번째" + days[i]);
                }
            }
        } else if (so1 == 3) {
            System.out.println("종료됩니다.");
            break;
        }
    }


//        System.out.println("시작");
//        Day day1 = new Day();
//        day1.setWork("영화보기");
//        day1.show();

    }

}
