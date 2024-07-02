public class Euler1 {
    public static void main(String[] args) {
        int a = 10;
        int c=10;
int t = 10;
while(t>1){
    a=a*(t-1);
    t--;
}
System.out.println(a);
    
    for(int i=1;i<10;i++){
        c = c*i;
    }
    System.out.println(c);
}
}
