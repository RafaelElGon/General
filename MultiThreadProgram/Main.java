import java.util.concurrent.ExecutorService;

public class PrimoMain {
    public static void main(String[] args) {
        ExecutorService pool = java.util.concurrent.Executors.newCachedThreadPool();
        for(int i = 0; i < 8; i++){
            pool.execute(new PrimoThread(i));
        }
        pool.shutdown();
    }
}
