public class DisjointSetClient {

    public static void main(String[] args) {
        DisjointSet d = new DisjointSet(10);
        d.union(0, 1);
        d.union(0, 2);
        d.union(4, 5);
        System.out.println(d);
    }

}
