//alt + insert = 소스 자동완성
//ctrl + y : redo(리도) 선택, 리도(앞으로 갈래?)
// ctrl + z 뒤로 가기
// ctrl + y 앞으로가기

public class Day {
    private String work; //하루의 할 일을 나타내는 문자열

    @Override
    public String toString() {
        return "Day{" +
                "work='" + work + '\'' +
                '}';
    }

    public String getWork() {
        return work;
    }

    public void setWork(String work) {
        this.work = work;
    }

    public void set(String work) {
        this.work = work;
    }

    public String get() {
        return work;
    }

    public void show() { //쑈함수를 호출하면 워크 값에 따라서 결과값이 나온다
        if (work == null) System.out.println("없습니다.");
        else System.out.println(work + "입니다.");
    }


}
